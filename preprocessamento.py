import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def tratamento(negotiation_type, condo, size, rooms, toilets, suites, parking, elevator, furnished, swimming_pool,
               new, bairro):
    # Instanciando o MinMaxScaler
    nm = MinMaxScaler()
    if negotiation_type == 0:
        lista_rent = pd.DataFrame({'Condo': condo,
                       'Size': size,
                       'Rooms': rooms,
                       'Toilets': toilets,
                       'Suites': suites,
                       'Parking': parking,
                       'Elevator': elevator,
                       'Furnished': furnished,
                       'Swimming Pool': swimming_pool,
                       'New': new,
                       'Grupo 1': 0,
                       'Grupo 10': 0,
                       'Grupo 11': 0,
                       'Grupo 12': 0,
                       'Grupo 2': 0,
                       'Grupo 3': 0,
                       'Grupo 4': 0,
                       'Grupo 5': 0,
                       'Grupo 6': 0,
                       'Grupo 7': 0,
                       'Grupo 8': 0,
                       'Grupo 9': 0})

        # Aplicando as transformações nas colunas numéricas no dataset de alugueis
        lista_rent['Condo'] = nm.fit_transform(lista_rent['Condo'].values.reshape(-1, 1))
        lista_rent['Size'] = nm.fit_transform(lista_rent['Size'].values.reshape(-1, 1))
        lista_rent['Rooms'] = nm.fit_transform(lista_rent['Rooms'].values.reshape(-1, 1))
        lista_rent['Toilets'] = nm.fit_transform(lista_rent['Toilets'].values.reshape(-1, 1))
        lista_rent['Suites'] = nm.fit_transform(lista_rent['Suites'].values.reshape(-1, 1))
        lista_rent['Parking'] = nm.fit_transform(lista_rent['Parking'].values.reshape(-1, 1))

        grupo1_rent = ['Artur Alvim', 'Cidade Líder', 'Itaim Paulista', 'Jardim Helena',
                        'José Bonifácio', 'Lajeado', 'Ponte Rasa', 'Grajaú', 'Jaçanã',
                        'Guaianazes', 'Jardim São Luis']
        grupo2_rent = ['Cangaíba', 'Cidade Tiradentes', 'Ermelino Matarazzo', 'Itaquera',
                       'Parque do Carmo', 'Penha', 'Sapopemba', 'São Lucas', 'São Mateus',
                       'São Miguel', 'São Rafael', 'Vila Jacuí', 'Vila Matilde',
                       'Campo Limpo', 'Capão Redondo', 'Cidade Ademar', 'Cidade Dutra',
                       'Jardim Ângela', 'Pedreira', 'Brasilândia', 'Cachoeirinha',
                       'Freguesia do Ó', 'Limão', 'Pirituba', 'Bom Retiro', 'Sé',
                       'Mandaqui', 'Tremembé', 'Vila Maria', 'Medeiros', 'Aricanduva']
        grupo3_rent = ['Belém', 'Carrão', 'Tatuapé', 'Vila Curuçá', 'Vila Formosa',
                       'Vila Prudente', 'Campo Grande', 'Cursino', 'Jabaquara', 'Morumbi',
                       'Sacomã', 'Socorro', 'Vila Andrade', 'Vila Sônia', 'Butantã',
                       'Jaguaré', 'Jaraguá', 'Raposo Tavares', 'Rio Pequeno', 'Pari',
                       'Santana', 'Tucuruvi', 'Vila Guilherme', 'Mooca']
        grupo4_rent = ['Cambuci', 'Ipiranga', 'Saúde', 'Lapa', 'Brás', 'Liberdade', 'Casa Verde', 'Água Rasa']
        grupo5_rent = ['Anhanguera', 'Perdizes', 'Vila Leopoldina', 'República', 'Santa Cecília']
        grupo6_rent = ['Santo Amaro', 'Vila Mariana', 'Alto de Pinheiros', 'Barra Funda', 'Bela Vista']
        grupo7_rent = ['Jardim Paulista']
        grupo8_rent = ['Campo Belo', 'Moema', 'Vila Madalena']
        grupo9_rent = ['Consolação']
        grupo10_rent = ['Pinheiros', 'Brooklin']
        grupo11_rent = ['Itaim Bibi']
        grupo12_rent = ['Iguatemi', 'Vila Olimpia']

        if bairro in grupo1_rent:
            lista_rent['Grupo 1'].replace({0: 1}, inplace=True)
            return lista_rent
        elif bairro in grupo2_rent:
            lista_rent['Grupo 2'].replace({0: 1}, inplace=True)
            return lista_rent
        elif bairro in grupo3_rent:
            lista_rent['Grupo 3'].replace({0: 1}, inplace=True)
            return lista_rent
        elif bairro in grupo4_rent:
            lista_rent['Grupo 4'].replace({0: 1}, inplace=True)
            return lista_rent
        elif bairro in grupo5_rent:
            lista_rent['Grupo 4'].replace({0: 1}, inplace=True)
            return lista_rent
        elif bairro in grupo6_rent:
            lista_rent['Grupo 4'].replace({0: 1}, inplace=True)
            return lista_rent
        elif bairro in grupo7_rent:
            lista_rent['Grupo 4'].replace({0: 1}, inplace=True)
            return lista_rent
        elif bairro in grupo8_rent:
            lista_rent['Grupo 4'].replace({0: 1}, inplace=True)
            return lista_rent
        elif bairro in grupo9_rent:
            lista_rent['Grupo 4'].replace({0: 1}, inplace=True)
            return lista_rent
        elif bairro in grupo10_rent:
            lista_rent['Grupo 4'].replace({0: 1}, inplace=True)
            return lista_rent
        elif bairro in grupo11_rent:
            lista_rent['Grupo 4'].replace({0: 1}, inplace=True)
            return lista_rent
        elif bairro in grupo12_rent:
            lista_rent['Grupo 4'].replace({0: 1}, inplace=True)
            return lista_rent

    elif negotiation_type == 1:
        lista_sale = pd.DataFrame({'Condo': 0,
                       'Size': 0,
                       'Rooms': 0,
                       'Toilets': 0,
                       'Suites': 0,
                       'Parking': 0,
                       'Elevator': 0,
                       'Furnished': 0,
                       'Swimming Pool': 0,
                       'New': 0,
                       'Grupo 1': 0,
                       'Grupo 10': 0,
                       'Grupo 11': 0,
                       'Grupo 12': 0,
                       'Grupo 13': 0,
                       'Grupo 14': 0,
                       'Grupo 15': 0,
                       'Grupo 16': 0,
                       'Grupo 17': 0,
                       'Grupo 18': 0,
                       'Grupo 19': 0,
                       'Grupo 2': 0,
                       'Grupo 3': 0,
                       'Grupo 4': 0,
                       'Grupo 5': 0,
                       'Grupo 6': 0,
                       'Grupo 7': 0,
                       'Grupo 8': 0,
                       'Grupo 9': 0})

        # Aplicando as transformações nas colunas numéricas no dataset de vendas
        lista_sale['Condo'] = nm.fit_transform(lista_sale['Condo'].values.reshape(-1, 1))
        lista_sale['Size'] = nm.fit_transform(lista_sale['Size'].values.reshape(-1, 1))
        lista_sale['Rooms'] = nm.fit_transform(lista_sale['Rooms'].values.reshape(-1, 1))
        lista_sale['Toilets'] = nm.fit_transform(lista_sale['Toilets'].values.reshape(-1, 1))
        lista_sale['Suites'] = nm.fit_transform(lista_sale['Suites'].values.reshape(-1, 1))
        lista_sale['Parking'] = nm.fit_transform(lista_sale['Parking'].values.reshape(-1, 1))

        grupo1_sale = ['Cidade Tiradentes']
        grupo2_sale = ['Artur Alvim', 'Itaim Paulista', 'Lajeado', 'São Rafael', 'Guaianazes']
        grupo3_sale = ['Cidade Líder', 'Itaquera', 'Parque do Carmo', 'São Mateus',
                       'São Miguel', 'Capão Redondo', 'Grajaú', 'Medeiros',
                       'Jardim São Luis']
        grupo4_sale = ['Cangaíba', 'Ermelino Matarazzo', 'Jardim Helena',
                       'José Bonifácio', 'Vila Curuçá', 'Vila Jacuí', 'Campo Limpo',
                       'Jardim Ângela', 'Pedreira', 'Brasilândia', 'Raposo Tavares',
                       'Perus']
        grupo5_sale = ['Penha', 'Ponte Rasa', 'Sapopemba', 'São Lucas', 'Cidade Ademar',
                      'Cidade Dutra', 'Cachoeirinha', 'Jaçanã', 'Aricanduva']
        grupo6_sale = ['Vila Matilde', 'Morumbi', 'Sacomã', 'Socorro', 'Vila Andrade',
                       'Pirituba', 'Bom Retiro']
        grupo7_sale = ['Carrão', 'Cambuci', 'Campo Grande', 'Freguesia do Ó', 'Limão',
                       'Rio Pequeno', 'Brás', 'Tucuruvi', 'Vila Maria', 'São Domingos']
        grupo8_sale = ['Belém', 'Vila Formosa', 'Vila Prudente', 'Cursino', 'Jabaquara',
                       'Vila Sônia', 'Anhanguera', 'Jaguaré', 'Liberdade', 'Pari', 'Sé',
                       'Mandaqui', 'Tremembé', 'Vila Guilherme']
        grupo9_sale = ['Tatuapé', 'Butantã', 'República', 'Casa Verde', 'Santana', 'Água Rasa', 'Mooca']
        grupo10_sale = ['Santo Amaro', 'Jaraguá', 'Lapa', 'Barra Funda']
        grupo11_sale = ['Ipiranga', 'Saúde', 'Bela Vista', 'Santa Cecília']
        grupo12_sale = ['Perdizes']
        grupo13_sale = ['Vila Leopoldina']
        grupo14_sale = ['Vila Mariana', 'Consolação']
        grupo15_sale = ['Campo Belo', 'Brooklin']
        grupo16_sale = ['Jardim Paulista', 'Moema', 'Pinheiros']
        grupo17_sale = ['Vila Madalena']
        grupo18_sale = ['Alto de Pinheiros']
        grupo19_sale = ['Itaim Bibi', 'Vila Olimpia']
        grupo20_sale = ['Iguatemi']

        if bairro in grupo1_sale:
            lista_sale['Grupo 1'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo2_sale:
            lista_sale['Grupo 2'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo3_sale:
            lista_sale['Grupo 3'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo4_sale:
            lista_sale['Grupo 4'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo5_sale:
            lista_sale['Grupo 5'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo6_sale:
            lista_sale['Grupo 6'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo7_sale:
            lista_sale['Grupo 7'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo8_sale:
            lista_sale['Grupo 8'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo9_sale:
            lista_sale['Grupo 9'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo10_sale:
            lista_sale['Grupo 10'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo11_sale:
            lista_sale['Grupo 11'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo12_sale:
            lista_sale['Grupo 12'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo13_sale:
            lista_sale['Grupo 13'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo14_sale:
            lista_sale['Grupo 14'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo15_sale:
            lista_sale['Grupo 15'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo16_sale:
            lista_sale['Grupo 16'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo17_sale:
            lista_sale['Grupo 17'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo18_sale:
            lista_sale['Grupo 18'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo19_sale:
            lista_sale['Grupo 19'].replace({0: 1}, inplace=True)
            return lista_sale
        elif bairro in grupo20_sale:
            lista_sale['Grupo 20'].replace({0: 1}, inplace=True)
            return lista_sale
