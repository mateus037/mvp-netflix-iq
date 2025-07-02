from model.modelo import Model
modelo = Model()

modelo_classification = modelo.carrega_modelo('./MachineLearning/models/netflix_classification.pkl')
data = modelo.carrega_modelo('./MachineLearning/models/dados_netflix.pkl')
cosine_sim = modelo.carrega_modelo('./MachineLearning/models/cosine_sim.pkl')
vectorizer = modelo.carrega_modelo('./MachineLearning/models/vectorizer.pkl')
