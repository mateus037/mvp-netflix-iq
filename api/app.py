from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from routes.predict import predict_bp

app = Flask(__name__)
CORS(app)  #habilita CORS para todas as rotas
swagger = Swagger(app)  # Ativa o Swagger UI

app.register_blueprint(predict_bp)

if __name__ == '__main__':
    app.run(debug=True)
