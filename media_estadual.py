from os import listdir
from os.path import isfile, join
from statistics import mean, mode, median, stdev, variance, pstdev, pvariance
from model import *
import pickle

def main():
    #mypath = "dados/"
    #files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    fileObject = open('dados_extraidos.bin', 'rb')
    estacoes: list[EstacaoMeteorologica] = pickle.load(fileObject)
    #for f in files:
    #    file = mypath + f
    #    estacoes.append(EstacaoMeteorologica(file))

    estados = {}
    for estacao in estacoes:
        if(estados.get(estacao.uf)):
            estados.update({estacao.uf: estados.get(estacao.uf) + [o.temperatura for o in estacao.data]})
        else:
            estados.update({estacao.uf: [o.temperatura for o in estacao.data]})

    for key, value in estados.items():
        print (key + " %.2f" % mean(value))
           
           

       
        



if __name__ == "__main__":
    main() 
           