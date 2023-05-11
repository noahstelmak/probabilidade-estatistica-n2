import decimal
from os import listdir
from os.path import isfile, join
from statistics import mean, mode, median, stdev, variance, pstdev, pvariance
from model import *
import pickle
from manim import *

def main():
    #mypath = "dados/"
    #files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    fileObject = open('dados_extraidos.bin', 'rb')
    estacoes: list[EstacaoMeteorologica] = pickle.load(fileObject)
    #for f in files:
    #    file = mypath + f
    #    estacoes.append(EstacaoMeteorologica(file))

    filtrados = {}
    for estacao in estacoes:
        if(estacao.uf == 'SC'):
            filtrados.update({estacao.estacao: [o.temperatura for o in estacao.data]})

    with open('dados_sc.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['estacao', 'media', 'moda', 'mediana', 'desvio padrao', 'variancia', 'desvio padrao populacional', 'variancia populacional'])

        for k, v in filtrados.items():
           writer.writerow([k, f'{mean(v)}'.replace('.', ','),  f'{mode(v)}'.replace('.', ','),  f'{median(v)}'.replace('.', ','),  f'{stdev(v)}'.replace('.', ','),  f'{variance(v)}'.replace('.', ','),  f'{pstdev(v)}'.replace('.', ','),  f'{pvariance(v)}'.replace('.', ',')])

if __name__ == "__main__":
    main() 