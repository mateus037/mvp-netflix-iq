import numpy as np
from services import *
from sklearn.metrics.pairwise import cosine_similarity

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