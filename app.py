# Importando as bibliotecas
from flask import Flask, request, render_template, jsonify
from flask_restful import Resource, Api
from joblib import load
import preprocessamento

# Iniciando o Flask e especificando o repositorio dos templates
app = Flask(__name__, template_folder="template")

# iniciando a API
api = Api(app)

# Carregando os modelos
model_rent = load('Modelos/model_rent.joblib')
model_sale = load('Modelos/model_sale.joblib')

# Rota padrão setada para home
@app.route('/home')
def home():
    return render_template('home.html')  # Rendezirar o template

# Rota 'predict' aceita GET request
@app.route('/predict', methods=['POST', 'GET'])
def predict_price():
    negotiation_type = request.args.get('negotiation_type')  # Get parameters for Negotiation_Type
    condo = request.args.get('condo')  # Get parameters for Condo
    size = request.args.get('size')  # Get parameters for petal length
    rooms = request.args.get('rooms')  # Get parameters for petal width
    toilets = request.args.get('toilets')  # Get parameters for Toilets
    suites = request.args.get('suites')  # Get parameters for Suites
    parking = request.args.get('parking')  # Get parameters for Parking
    elevator = request.args.get('elevator')  # Get parameters for Elevator
    furnished = request.args.get('furnished')  # Get parameters for Furnished
    swimming_pool = request.args.get('swimming_pool')  # Get parameters for Swimming_Pool
    new = request.args.get('new')  # Get parameters for New
    bairro = request.args.get('bairro')  # Get parameters for Bairro

    list = (negotiation_type, condo, size, rooms, toilets, suites, parking, elevator, furnished, swimming_pool,
                new, bairro)

    # Separando os modelos para aluguel e venda
    if negotiation_type == 0:
        # Get the output from the model
        previsao = model_rent.predict(preprocessamento.tratamento(list))
        return render_template('output.html', previsao=previsao)

    elif negotiation_type == 1:
        # Get the output from the model
        previsao = model_sale.predict(preprocessamento.tratamento(list))
        # Render the output in new HTML page
        return render_template('output.html', previsao=previsao)

# Executar o servidor Flask
if(__name__== '__main__'):
    app.run(debug=True)
