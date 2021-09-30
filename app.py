# Importando as bibliotecas
from flask import Flask, request, render_template
from flask_restful import Api
from joblib import load

# Iniciando o Flask e especificando o repositorio dos templates
app = Flask(__name__, template_folder="template")

import preprocessamento

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
       negotiation_type = int(request.args.get('negotiation_type'))  # Obter os parâmetros para Negotiation_Type
       condo = int(request.args.get('condo'))  # Obter os parâmetros para Condo
       size = int(request.args.get('size'))  # Obter os parâmetros para Size
       rooms = int(request.args.get('rooms'))  # Obter os parâmetros para Rooms
       toilets = int(request.args.get('toilets'))  # Obter os parâmetros para Toilets
       suites = int(request.args.get('suites'))  # Obter os parâmetros para Suites
       parking = int(request.args.get('parking'))  # Obter os parâmetros para Parking
       elevator = int(request.args.get('elevator'))  # Obter os parâmetros para Elevator
       furnished = int(request.args.get('furnished'))  # Obter os parâmetros para Furnished
       swimming_pool = int(request.args.get('swimming_pool'))  # Obter os parâmetros para Swimming_Pool
       new = int(request.args.get('new'))  # Obter os parâmetros para New
       bairro = request.args.get('bairro')  # Obter os parâmetros para Bairro

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
                                                                             furnished, swimming_pool, new, bairro)))
           # Exibindo a previsão na página web output
           return render_template('output.html', previsao=previsao)
   except:
       'Error'

# Executar o servidor Flask
if(__name__== '__main__'):
    app.run()
