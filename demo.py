from os import listdir, remove
from os.path import isfile, join
from statistics import mean, mode, median, stdev, variance, pstdev, pvariance

from model import *

def main():
    mypath = "dados/"
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    for f in files:

        file = mypath + f
        t5n = EstacaoMeteorologica(file)        
        
        media = mean([o.temperatura for o in t5n.data])
        moda = mode([o.temperatura for o in t5n.data])
        mediana = median([o.temperatura for o in t5n.data])
        desvio = stdev([o.temperatura for o in t5n.data])
        variancia = variance([o.temperatura for o in t5n.data])
        desvio_populacional = pstdev([o.temperatura for o in t5n.data])
        variancia_populacional = pvariance([o.temperatura for o in t5n.data])

        
        print(f"{t5n.estacao}")
        print(f"media: {media}")
        print(f"mediana: {mediana}")
        print(f"moda: {moda}")
        print(f"desvio: {desvio}")
        print(f"variancia: {variancia}")
        print(f"desvio populacional: {desvio_populacional}")
        print(f"variancia populacional: {variancia_populacional}")

if __name__ == "__main__":
    main() 
           