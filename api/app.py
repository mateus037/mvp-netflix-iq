from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from model.modelo import Model

app = Flask(__name__)
CORS(app)  #habilita CORS para todas as rotas
swagger = Swagger(app)  # Ativa o Swagger UI

modelo = Model()

# Carrega o modelo de classificação
modelo_classification = modelo.carrega_modelo('./MachineLearning/models/netflix_classification.pkl')

# Carrega dados e matriz de similaridade
data = modelo.carrega_modelo('./MachineLearning/models/dados_netflix.pkl')
cosine_sim = modelo.carrega_modelo('./MachineLearning/models/cosine_sim.pkl')
vectorizer = modelo.carrega_modelo('./MachineLearning/models/vectorizer.pkl')

# Recomendação por campos se o título não existir
def recomendar_por_campos(fields, top_n=5):
    campos = [
        fields.get('country', ''),
        fields.get('listed_in', '')
    ]
    conteudo_novo = ' '.join(campos)
    vetor = vectorizer.transform([conteudo_novo])
    tfidf_matrix = vectorizer.transform(data['conteudo'])
    sim_scores = cosine_similarity(vetor, tfidf_matrix).flatten()
    indices = np.argsort(sim_scores)[::-1][:top_n]
    return data[['title', 'type', 'release_year']].iloc[indices].to_dict(orient='records')

@app.route('/predict', methods=['POST'])
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
    if req['title'] not in data['title'].values:
        recomendados = recomendar_por_campos(req)
        return jsonify({'recomendados': recomendados})
    
    idx = data[data['title'] == req['title']].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    indices = [i[0] for i in sim_scores]

    recomendados = data[['title', 'type', 'release_year']].iloc[indices]
    return jsonify({'prediction': prediction[0], 'recomendados': recomendados.to_dict(orient='records')})

if __name__ == '__main__':
    app.run(debug=True)
