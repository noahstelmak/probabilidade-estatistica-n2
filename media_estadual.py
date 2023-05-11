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

    estados = {}
    for estacao in estacoes:
        if(estados.get(estacao.uf)):
            estados.update({estacao.uf: estados.get(estacao.uf) + [o.temperatura for o in estacao.data]})
        else:
            estados.update({estacao.uf: [o.temperatura for o in estacao.data]})

    with open('dados_sc.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['estacao', 'media', 'moda', 'mediana', 'desvio padrao', 'variancia', 'desvio padrao populacional', 'variancia populacional'])

        for k, v in estados.items():
           writer.writerow([k, f'{mean(v)}'.replace('.', ','),  f'{mode(v)}'.replace('.', ','),  f'{median(v)}'.replace('.', ','),  f'{stdev(v)}'.replace('.', ','),  f'{variance(v)}'.replace('.', ','),  f'{pstdev(v)}'.replace('.', ','),  f'{pvariance(v)}'.replace('.', ',')])
    
class MediaEstadual(Scene):
    def construct(self):

        fileObject = open('dados_extraidos.bin', 'rb')
        estacoes: list[EstacaoMeteorologica] = pickle.load(fileObject)

        estados = {}
        for estacao in estacoes:
            if(estados.get(estacao.uf)):
                estados.update({estacao.uf: estados.get(estacao.uf) + [o.temperatura for o in estacao.data]})
            else:
                estados.update({estacao.uf: [o.temperatura for o in estacao.data]})
        values: list[float] = []
        bar_names: list[str]= []
        for key, value in list(estados.items())[:14]:
            values.append(round(mean(value), 2))
            bar_names.append(key)

        chart = BarChart(
            bar_stroke_width=1,
            bar_width=0.7,
            values=values,
            bar_names=bar_names,
            y_range=[0, 30, 5],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 20},
            y_axis_config={"font_size": 20},
        )

        c_bar_lbls = chart.get_bar_labels(font_size=24)

        self.add(chart, c_bar_lbls)

class MediaEstadualB(Scene):
    def construct(self):

        fileObject = open('dados_extraidos.bin', 'rb')
        estacoes: list[EstacaoMeteorologica] = pickle.load(fileObject)

        estados = {}
        for estacao in estacoes:
            if(estados.get(estacao.uf)):
                estados.update({estacao.uf: estados.get(estacao.uf) + [o.temperatura for o in estacao.data]})
            else:
                estados.update({estacao.uf: [o.temperatura for o in estacao.data]})
        values: list[float] = []
        bar_names: list[str]= []
        for key, value in list(estados.items())[14:]:
            values.append(round(mean(value), 2))
            bar_names.append(key)

        chart = BarChart(
            bar_stroke_width=1,
            bar_width=0.7,
            values=values,
            bar_names=bar_names,
            y_range=[0, 30, 5],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 20},
            y_axis_config={"font_size": 20},
        )

        c_bar_lbls = chart.get_bar_labels(font_size=20)

        self.add(chart, c_bar_lbls)

           
           

       
        



if __name__ == "__main__":
    main() 
           