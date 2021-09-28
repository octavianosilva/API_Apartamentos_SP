# Importando as bibliotecas
from flask import Flask, request, render_template, jsonify
from flask_restful import Resource, Api
from joblib import load

# Iniciando o Flask e especificando o repositorio dos templates
app = Flask(__name__, template_folder="template")

# Iniciando a API
api = Api(app)

# Carregando os modelos treinados
modelo_aluguel = load('modelo_alugueis.joblib')
modelo_venda = load('modelo_vendas.joblib')

# Rota padrão para home
@app.route('/')
def home():
    return render_template('home.html')  # Rendezirar o template

# Rota 'predict' aceita GET request
@app.route('/predict', methods=['GET'])
def predict_price():
   try:
       negotiation_type = int(request.args.get('negotiation_type'))  # Get parameters for Negotiation_Type
       condo = int(request.args.get('condo'))  # Get parameters for Condo
       size = int(request.args.get('size'))  # Get parameters for petal length
       rooms = int(request.args.get('rooms'))  # Get parameters for petal width
       toilets = int(request.args.get('toilets'))  # Get parameters for Toilets
       suites = int(request.args.get('suites'))  # Get parameters for Suites
       parking = int(request.args.get('parking'))  # Get parameters for Parking
       elevator = int(request.args.get('elevator'))  # Get parameters for Elevator
       furnished = int(request.args.get('furnished'))  # Get parameters for Furnished
       swimming_pool = int(request.args.get('swimming_pool'))  # Get parameters for Swimming_Pool
       new = int(request.args.get('new'))  # Get parameters for New
       bairro = request.args.get('bairro')  # Get parameters for Bairro

       bairros_sem_aluguel = ['District_Perus', 'District_São Domingos']

       # Separando os modelos para aluguel e venda
       if negotiation_type == 0:
            if bairro in bairros_sem_aluguel:
                previsao = 'O bairro informado não possui nenhuma informação no banco de dados referente ao preço de ' \
                           'aluguel.'
                return render_template('output2.html', previsao=previsao)
            else:
                # Obtendo  a previsão
                previsao = modelo_aluguel.predict(preprocessamento.tratamento(negotiation_type, condo, size, rooms,
                                                                              toilets, suites, parking, elevator,
                                                                              furnished, swimming_pool, new, bairro))
                # Exibindo a previsão na página web output
                return render_template('output.html', previsao=previsao)

       elif negotiation_type == 1:
           # Obtendo a previsão
           previsao = round(modelo_venda.predict(preprocessamento.tratamento(negotiation_type, condo, size, rooms,
                                                                             toilets, suites, parking, elevator,
                                                                             furnished, swimming_pool, new, bairro))[0])
           # Exibindo a previsão na página web output
           return render_template('output.html', previsao=previsao)
   except:
       'Error'

# Executar o servidor Flask
if(__name__== '__main__'):
    app.run(debug=True)
