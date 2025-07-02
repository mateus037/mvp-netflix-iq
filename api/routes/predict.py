from flask import Blueprint, request, jsonify
import pandas as pd
from services.model_service import modelo_classification, data, cosine_sim, vectorizer
from services.recommendation_service import recomendar_por_campos

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    """
    Faz a predição do tipo de conteúdo e recomenda similares
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - title
            - country
            - release_year
            - rating
            - listed_in
            - duration_int
          properties:
            title:
              type: string
              example: Naruto
            country:
              type: string
              example: Japan
            release_year:
              type: integer
              example: 2006
            rating:
              type: string
              example: TV-14
            listed_in:
              type: string
              example: Anime Series, International TV Shows
            duration_int:
              type: integer
              example: 9
    responses:
      200:
        description: Resultado da predição e recomendações
        schema:
          type: object
          properties:
            prediction:
              type: string
            recomendados:
              type: array
              items:
                type: object
    """
    req = request.get_json()
    df = pd.DataFrame([req])
    prediction = modelo_classification.predict(df)
    if prediction is None or len(prediction) == 0:
        return jsonify({'erro': 'Erro ao fazer a previsão'}), 500

    # Se o título não estiver nos dados, retorna a previsão e uma lista vazia de recomendados
    if req['title'].lower() not in data['title'].str.lower().values:
        recomendados = recomendar_por_campos(req)
        return jsonify({'prediction': prediction[0], 'recomendados': recomendados})

    idx = data[data['title'].str.lower() == req['title'].lower()].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    indices = [i[0] for i in sim_scores]

    recomendados = data[['title', 'type', 'release_year']].iloc[indices]
    return jsonify({'prediction': prediction[0], 'recomendados': recomendados.to_dict(orient='records')})