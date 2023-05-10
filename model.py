import csv 

class EstacaoMeteorologica: # escrito errado pois o gustavo quis.
    def __init__(self, path) -> None:
        with open(path) as file:

            # linhas 0 até 7:
            # ['REGIAO:', 'CO']
            # ['UF:', 'DF']
            # ['ESTACAO:', 'BRASILIA']
            # ['CODIGO (WMO):', 'A001']
            # ['LATITUDE:', '-15,78944444']
            # ['LONGITUDE:', '-47,92583332']
            # ['ALTITUDE:', '1160,96']
            # ['DATA DE FUNDACAO:', '07/05/00']

            matriz = list(csv.reader(file, delimiter=";"))

            self.regiao: str = matriz[0][1]
            self.uf: str = matriz[1][1]
            self.estacao: str = matriz[2][1]
            self.codigo: str = matriz[3][1]
            self.latitude: float = float(matriz[4][1].replace(",", "."))
            self.longitude: float = float(matriz[5][1].replace(",", "."))
            self.altitude: float = float(matriz[6][1].replace(",", "."))
            self.fundacao = matriz[7][1]

            # linha 8 é o cabeçalho

            # colunas a partir da linha 9:
            # [
            # 0  'Data,
            # 1  'Hora UTC,
            # 2  'PRECIPITAÇÃO TOTAL, HORÁRIO (mm),
            # 3  'PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB),
            # 4  'PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB),
            # 5  'PRESSÃO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB),
            # 6  'RADIACAO GLOBAL (Kj/m²),
            # 7  'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C),
            # 8  'TEMPERATURA DO PONTO DE ORVALHO (°C),
            # 9  'TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C),
            # 10 'TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C),
            # 11 'TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (°C),
            # 12 'TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (°C),
            # 13  'UMIDADE REL. MAX. NA HORA ANT. (AUT) (%),
            # 14  'UMIDADE REL. MIN. NA HORA ANT. (AUT) (%),
            # 15  'UMIDADE RELATIVA DO AR, HORARIA (%),
            # 16  'VENTO, DIREÇÃO HORARIA (gr) (° (gr)),
            # 17  'VENTO, RAJADA MAXIMA (m/s),
            # 18  'VENTO, VELOCIDADE HORARIA (m/s),
            #   ''
            # ]

            data: list[Medicao] = []
            for d in matriz[9:]:
                if d[7]:
                    data.append(Medicao(d))

            self.data: list[Medicao] = data

    

class Medicao:
    def __init__(self, coluna) -> None:
        self.dia: str = coluna[0]
        self.hora: str = coluna[1]
        #self.precipitacao: float = (coluna[2].replace(",", "."))
        #self.pressao_atmosferica: float = float(coluna[3].replace(",", "."))
        #self.umidade : float = float(coluna[15].replace(",", "."))
        #self.vento_velocidade: float  = float(coluna[18].replace(",", "."))
        #self.vento_direcao: str =  float(coluna[16].replace(",", "."))
        self.temperatura: float = float(coluna[7].replace(',','.'))
        

