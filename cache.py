from os import listdir
import pickle
from os.path import isfile, join
from statistics import mean, mode, median, stdev, variance, pstdev, pvariance
from model import EstacaoMeteorologica


mypath = "dados/"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

estacoes: list[EstacaoMeteorologica] = []
for f in files:
    file = mypath + f
    estacoes.append(EstacaoMeteorologica(file))

fileObject = open('dados_extraidos.bin', 'wb')
pickle.dump(estacoes, fileObject)

# carregar dados com:
# fileObject = open('dados_extraidos.bin', 'rb')
# estacoes: list[EstacaoMeteorologica] = pickle.load(fileObject)