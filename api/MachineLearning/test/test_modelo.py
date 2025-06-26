import pickle
import pandas as pd
from sklearn.metrics import accuracy_score

# Carrega o modelo treinado
with open('../models/netflix_classification.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Lista de casos simulados
casos_de_teste = [
    {
        "entrada": {
            'country': 'United States',
            'release_year': 2022,
            'rating': 'PG-13',
            'listed_in': 'Action & Adventure, Thrillers',
            'duration_int': 130
        },
        "esperado": 'Movie'
    },
    {
        "entrada": {
            'country': 'India',
            'release_year': 2021,
            'rating': 'TV-14',
            'listed_in': 'Dramas, International TV Shows',
            'duration_int': 3
        },
        "esperado": 'TV Show'
    },
    {
        "entrada": {
            'country': 'Japan',
            'release_year': 2020,
            'rating': 'TV-PG',
            'listed_in': 'Anime Features, Sci-Fi & Fantasy',
            'duration_int': 90
        },
        "esperado": 'Movie'
    },
    {
        "entrada": {
            'country': 'Brazil',
            'release_year': 2019,
            'rating': 'TV-MA',
            'listed_in': 'Comedies, International TV Shows',
            'duration_int': 1
        },
        "esperado": 'TV Show'
    },
    {
        "entrada": {
            'country': 'France',
            'release_year': 1995,
            'rating': 'R',
            'listed_in': 'Classic Movies, Dramas',
            'duration_int': 105
        },
        "esperado": 'Movie'
    }
]

def test_modelo_em_predicoes_individuais():
    for i, caso in enumerate(casos_de_teste):
        entrada_df = pd.DataFrame([caso["entrada"]])
        predicao = modelo.predict(entrada_df)[0]
        print(f"Cenário {i+1} → Esperado: {caso['esperado']} | Previsto: {predicao}")
        assert predicao == caso["esperado"]  # verifica caso a caso

def test_accuracy_geral_dos_dados_simulados():
    entradas = pd.DataFrame([caso["entrada"] for caso in casos_de_teste])
    esperados = [caso["esperado"] for caso in casos_de_teste]
    
    previsoes = modelo.predict(entradas)
    acc = accuracy_score(esperados, previsoes)
    
    print(f"\nAcurácia nos dados simulados: {acc:.2f}")
    assert acc >= 0.80  # Limite mínimo aceitável (ajustável)
