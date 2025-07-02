# 🎬 MVP Netflix IQ

Sistema inteligente de **classificação e recomendação de títulos da Netflix** com aplicação Full Stack.

---

## 📌 Funcionalidades

- Classifica se um título é **Filme** ou **Série**
- Recomenda títulos similares com base em conteúdo (elenco, país e categorias)
- Aplicação Full Stack (Flask + HTML/CSS com Bootstrap)
- Testes automatizados com **PyTest**
- Documentação da API com **Swagger**

---

## 🚀 Tecnologias utilizadas

- **Python** (Flask, Scikit-learn, Pandas, NumPy)
- **Bootstrap 5**
- **PyTest**
- **Swagger**

---

## 🧠 Modelo de Machine Learning

- Classificação com:
  - KNN
  - Decision Tree
  - Naive Bayes
  - SVM
- Pipeline de pré-processamento
- Otimização de hiperparâmetros com `GridSearchCV`(que por baixo dos panos usa cross_val_score)
- Avaliação com **cross-validation**
- Sistema de recomendação baseado em **similaridade de cosseno** usando TF-IDF

---

## 📂 Estrutura do projeto

```bash
mvp-netflix-iq/
├── api/                  # Back-end Flask
│   ├── app.py
│   └── MachineLearning/  # Machine Learning
│       ├── models/
│       ├── notebook/
│       └── test/
├── web/                  # Front-end com Bootstrap
│   ├── index.html
│   └── script.js
├── .gitignore
└── README.md
```
---

## 📥 Download dos Modelos (.pkl)

Para que a aplicação funcione corretamente, é necessário ter os arquivos `.pkl` gerados pelo processo de machine learning.

### 🔗 1. Faça o download dos modelos prontos

Acesse o link abaixo para baixar os arquivos já treinados:

➡️ [Google Drive - Modelos treinados (.pkl)](https://drive.google.com/drive/u/0/folders/1eWPmx9D2BefFV8brRQpG4Y6Y_XBzkY7g)

---

### 📂 2. Coloque os arquivos no diretório correto

Após o download, mova todos os arquivos `.pkl` para o seguinte diretório:
```bash
api/MachineLearning/models
```
---

### ⚙️ Alternativa: Gerar os modelos executando os notebooks

Se preferir (ou quiser treinar novamente), você pode executar os notebooks disponíveis no projeto. Eles irão:

- Treinar os modelos do zero;
- Exportar automaticamente os arquivos `.pkl` para a pasta `models`.

---

## 📦 Instalação e execução

1. **Crie e ative o ambiente virtual**.
> Windows
```bash
python -m venv venv
venv\Scripts\activate
```
>macOS/Linux
```bash
python -m venv venv
source venv/bin/activate
```
2. **Entre no diretório do back-end**
```bash
cd api/
```
3. **Instale as dependências**
```bash
pip install -r requirements.txt
```
4. **Inicie o servidor**
```bash
python app.py
```

---

## 🧪 Testes automatizados
>Testes com PyTest para verificar a acurácia mínima do modelo antes do deploy.
1. **Instale o PyTest (caso ainda não tenha)**
```bash
pip install pytest
```
2. **Execute os testes**
```bash
cd api/MachineLearning/test
pytest test_modelo.py
```