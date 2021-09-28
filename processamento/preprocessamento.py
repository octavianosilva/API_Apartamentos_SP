# Importando as bibliotecas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Lendo os arquivos .csv
bairros_aluguel = pd.read_csv(r"C:\Users\octav\PycharmProjects\Deploy_ML\processamento\bairros_aluguel.csv")
bairros_venda = pd.read_csv(r"C:\Users\octav\PycharmProjects\Deploy_ML\processamento\bairros_venda.csv")
df_aluguel = pd.read_csv(r"C:\Users\octav\PycharmProjects\Deploy_ML\processamento\df_aluguel.csv")
df_venda = pd.read_csv(r"C:\Users\octav\PycharmProjects\Deploy_ML\processamento\df_venda.csv")

# Dropando as colunas Unnamed que apareceram com a importação
bairros_aluguel.drop('Unnamed: 0', axis=1, inplace=True)
bairros_venda.drop('Unnamed: 0', axis=1, inplace=True)
df_aluguel.drop('Unnamed: 0', axis=1, inplace=True)
df_venda.drop('Unnamed: 0', axis=1, inplace=True)

# Realizando o tratamento dos dados para previsão de acordo com o modelo: aluguel ou venda
def tratamento(negotiation_type, condo, size, rooms, toilets, suites, parking, elevator, furnished, swimming_pool,
               new, bairro):

    # Separando a coluna alvo do restante dos dados - dataset algueis
    X_aluguel = df_aluguel.drop('Price', axis=1)
    y_aluguel = df_aluguel['Price']  # variável alvo

    # Separando entre dados de treino e teste - dataset alugueis
    X_aluguel_train, X_aluguel_test, y_aluguel_train, y_aluguel_test = train_test_split(X_aluguel, y_aluguel,
                                                                                        test_size=0.20,
                                                                                        shuffle=True)
    # Normalizando os dados
    nm_aluguel = MinMaxScaler().fit(X_aluguel_train)

    # Separando a coluna alvo do restante dos dados - dataset vendas
    X_venda = df_venda.drop('Price', axis=1)
    y_venda = df_venda['Price']  # variável alvo

    # Separando entre dados de treino e teste - dataset vendas
    X_venda_train, X_venda_test, y_venda_train, y_venda_test = train_test_split(X_venda, y_venda, test_size=0.20,
                                                                                shuffle=True)
    # Normalizando os dados
    nm_venda = MinMaxScaler().fit(X_venda_train)

    if negotiation_type == 0:
        lista_aluguel = pd.DataFrame({'Condo': condo,
                                    'Size': size,
                                    'Rooms': rooms,
                                    'Toilets': toilets,
                                    'Suites': suites,
                                    'Parking': parking,
                                    'Elevator': elevator,
                                    'Furnished': furnished,
                                    'Swimming Pool': swimming_pool,
                                    'New': new,
                                    'Price/Size': 0,
                                    'District_Alto de Pinheiros': 0,
                                    'District_Anhanguera': 0,
                                    'District_Aricanduva': 0,
                                    'District_Artur Alvim': 0,
                                    'District_Barra Funda': 0,
                                    'District_Bela Vista': 0,
                                    'District_Belém': 0,
                                    'District_Bom Retiro': 0,
                                    'District_Brasilândia': 0,
                                    'District_Brooklin': 0,
                                    'District_Brás': 0,
                                    'District_Butantã': 0,
                                    'District_Cachoeirinha': 0,
                                    'District_Cambuci': 0,
                                    'District_Campo Belo': 0,
                                    'District_Campo Grande': 0,
                                    'District_Campo Limpo': 0,
                                    'District_Cangaíba': 0,
                                    'District_Capão Redondo': 0,
                                    'District_Carrão': 0,
                                    'District_Casa Verde': 0,
                                    'District_Cidade Ademar': 0,
                                    'District_Cidade Dutra': 0,
                                    'District_Cidade Líder': 0,
                                    'District_Cidade Tiradentes': 0,
                                    'District_Consolação': 0,
                                    'District_Cursino': 0,
                                    'District_Ermelino Matarazzo': 0,
                                    'District_Freguesia do Ó': 0,
                                    'District_Grajaú': 0,
                                    'District_Guaianazes': 0,
                                    'District_Iguatemi': 0,
                                    'District_Ipiranga': 0,
                                    'District_Itaim Bibi': 0,
                                    'District_Itaim Paulista': 0,
                                    'District_Itaquera': 0,
                                    'District_Jabaquara': 0,
                                    'District_Jaguaré': 0,
                                    'District_Jaraguá': 0,
                                    'District_Jardim Helena': 0,
                                    'District_Jardim Paulista': 0,
                                    'District_Jardim São Luis': 0,
                                    'District_Jardim Ângela': 0,
                                    'District_Jaçanã': 0,
                                    'District_José Bonifácio': 0,
                                    'District_Lajeado': 0,
                                    'District_Lapa': 0,
                                    'District_Liberdade': 0,
                                    'District_Limão': 0,
                                    'District_Mandaqui': 0,
                                    'District_Medeiros': 0,
                                    'District_Moema': 0,
                                    'District_Mooca': 0,
                                    'District_Morumbi': 0,
                                    'District_Pari': 0,
                                    'District_Parque do Carmo': 0,
                                    'District_Pedreira': 0,
                                    'District_Penha': 0,
                                    'District_Perdizes': 0,
                                    'District_Pinheiros': 0,
                                    'District_Pirituba': 0,
                                    'District_Ponte Rasa': 0,
                                    'District_Raposo Tavares': 0,
                                    'District_República': 0,
                                    'District_Rio Pequeno': 0,
                                    'District_Sacomã': 0,
                                    'District_Santa Cecília': 0,
                                    'District_Santana': 0,
                                    'District_Santo Amaro': 0,
                                    'District_Sapopemba': 0,
                                    'District_Saúde': 0,
                                    'District_Socorro': 0,
                                    'District_São Lucas': 0,
                                    'District_São Mateus': 0,
                                    'District_São Miguel': 0,
                                    'District_São Rafael': 0,
                                    'District_Sé': 0,
                                    'District_Tatuapé': 0,
                                    'District_Tremembé': 0,
                                    'District_Tucuruvi': 0,
                                    'District_Vila Andrade': 0,
                                    'District_Vila Curuçá': 0,
                                    'District_Vila Formosa': 0,
                                    'District_Vila Guilherme': 0,
                                    'District_Vila Jacuí': 0,
                                    'District_Vila Leopoldina': 0,
                                    'District_Vila Madalena': 0,
                                    'District_Vila Maria': 0,
                                    'District_Vila Mariana': 0,
                                    'District_Vila Matilde': 0,
                                    'District_Vila Olimpia': 0,
                                    'District_Vila Prudente': 0,
                                    'District_Vila Sônia': 0,
                                    'District_Água Rasa': 0}, index=[0])

        # Convertendo o valor da coluna do bairro passado para 1
        lista_aluguel[bairro].replace({0: 1}, inplace=True)

        # Obtendo o valor do preço médio por metro quadrado do bairro passado
        price = bairros_aluguel['Média dos Preços'].loc[bairros_aluguel['Bairros'] == bairro].item()

        # Convertendo o valor da coluna Price/Size para o valor obtido acima
        lista_aluguel['Price/Size'].replace({0: price}, inplace=True)

        # Aplicando as transformações no dataset de alugueis
        lista_aluguel = nm_aluguel.transform(lista_aluguel)
        return lista_aluguel

    elif negotiation_type == 1:
        lista_venda = pd.DataFrame({'Condo': condo,
                                    'Size': size,
                                    'Rooms': rooms,
                                    'Toilets': toilets,
                                    'Suites': suites,
                                    'Parking': parking,
                                    'Elevator': elevator,
                                    'Furnished': furnished,
                                    'Swimming Pool': swimming_pool,
                                    'New': new,
                                    'Price/Size': 0,
                                    'District_Alto de Pinheiros': 0,
                                    'District_Anhanguera': 0,
                                    'District_Aricanduva': 0,
                                    'District_Artur Alvim': 0,
                                    'District_Barra Funda': 0,
                                    'District_Bela Vista': 0,
                                    'District_Belém': 0,
                                    'District_Bom Retiro': 0,
                                    'District_Brasilândia': 0,
                                    'District_Brooklin': 0,
                                    'District_Brás': 0,
                                    'District_Butantã': 0,
                                    'District_Cachoeirinha': 0,
                                    'District_Cambuci': 0,
                                    'District_Campo Belo': 0,
                                    'District_Campo Grande': 0,
                                    'District_Campo Limpo': 0,
                                    'District_Cangaíba': 0,
                                    'District_Capão Redondo': 0,
                                    'District_Carrão': 0,
                                    'District_Casa Verde': 0,
                                    'District_Cidade Ademar': 0,
                                    'District_Cidade Dutra': 0,
                                    'District_Cidade Líder': 0,
                                    'District_Cidade Tiradentes': 0,
                                    'District_Consolação': 0,
                                    'District_Cursino': 0,
                                    'District_Ermelino Matarazzo': 0,
                                    'District_Freguesia do Ó': 0,
                                    'District_Grajaú': 0,
                                    'District_Guaianazes': 0,
                                    'District_Iguatemi': 0,
                                    'District_Ipiranga': 0,
                                    'District_Itaim Bibi': 0,
                                    'District_Itaim Paulista': 0,
                                    'District_Itaquera': 0,
                                    'District_Jabaquara': 0,
                                    'District_Jaguaré': 0,
                                    'District_Jaraguá': 0,
                                    'District_Jardim Helena': 0,
                                    'District_Jardim Paulista': 0,
                                    'District_Jardim São Luis': 0,
                                    'District_Jardim Ângela': 0,
                                    'District_Jaçanã': 0,
                                    'District_José Bonifácio': 0,
                                    'District_Lajeado': 0,
                                    'District_Lapa': 0,
                                    'District_Liberdade': 0,
                                    'District_Limão': 0,
                                    'District_Mandaqui': 0,
                                    'District_Medeiros': 0,
                                    'District_Moema': 0,
                                    'District_Mooca': 0,
                                    'District_Morumbi': 0,
                                    'District_Pari': 0,
                                    'District_Parque do Carmo': 0,
                                    'District_Pedreira': 0,
                                    'District_Penha': 0,
                                    'District_Perdizes': 0,
                                    'District_Perus': 0,
                                    'District_Pinheiros': 0,
                                    'District_Pirituba': 0,
                                    'District_Ponte Rasa': 0,
                                    'District_Raposo Tavares': 0,
                                    'District_República': 0,
                                    'District_Rio Pequeno': 0,
                                    'District_Sacomã': 0,
                                    'District_Santa Cecília': 0,
                                    'District_Santana': 0,
                                    'District_Santo Amaro': 0,
                                    'District_Sapopemba': 0,
                                    'District_Saúde': 0,
                                    'District_Socorro': 0,
                                    'District_São Domingos': 0,
                                    'District_São Lucas': 0,
                                    'District_São Mateus': 0,
                                    'District_São Miguel': 0,
                                    'District_São Rafael': 0,
                                    'District_Sé': 0,
                                    'District_Tatuapé': 0,
                                    'District_Tremembé': 0,
                                    'District_Tucuruvi': 0,
                                    'District_Vila Andrade': 0,
                                    'District_Vila Curuçá': 0,
                                    'District_Vila Formosa': 0,
                                    'District_Vila Guilherme': 0,
                                    'District_Vila Jacuí': 0,
                                    'District_Vila Leopoldina': 0,
                                    'District_Vila Madalena': 0,
                                    'District_Vila Maria': 0,
                                    'District_Vila Mariana': 0,
                                    'District_Vila Matilde': 0,
                                    'District_Vila Olimpia': 0,
                                    'District_Vila Prudente': 0,
                                    'District_Vila Sônia': 0,
                                    'District_Água Rasa': 0}, index=[0])

        # Convertendo o valor da coluna do bairro passado para 1
        lista_venda[bairro].replace({0: 1}, inplace=True)

        # Obtendo o valor do preço médio por metro quadrado do bairro passado
        price = bairros_aluguel['Média dos Preços'].loc[bairros_aluguel['Bairros'] == bairro].item()

        # Convertendo o valor da coluna Price/Size para o valor obtido acima
        lista_venda['Price/Size'].replace({0: price}, inplace=True)

        # Aplicando as transformações no dataset de venda
        lista_venda = nm_venda.transform(lista_venda)
        return lista_venda
