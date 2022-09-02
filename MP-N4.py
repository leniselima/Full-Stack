from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


class Grafico:
    def __init__(self, lista_despesas):
        self.lista_despesas=lista_despesas
        self.imprimir_graficos()

    def padrao_do_grafico(self):
        plt.xlabel('DIAS')
        plt.ylabel('VALORES ($)')
        plt.title('GRÁFICOS DE DESPESAS')

    def imprimir_graficos(self):
        self.padrao_do_grafico()
        for despesa in self.lista_despesas:
            mLista = despesa.dicionario.items()
            cor = despesa.cor
            nome = despesa.nome
            x, y = zip(*mLista)
            plt.plot(x, y, label=nome, marker='o',
               markerfacecolor='blue',
               markersize=12,
               color=cor,
               linewidth=4)
        plt.legend()
        plt.show()

    def regressao_linear(self, id_grafico):
        despesa = self.lista_despesas[id_grafico]
        mLista = despesa.dicionario.items()
        cor = despesa.cor
        nome = despesa.nome
        dias, valores = zip(*mLista)
        dias = np.array(dias)
        valores = np.array(valores)
        dias = dias.reshape(-1, 1)
        valores = valores.reshape(-1, 1)
        regr = LinearRegression()
        regr.fit(X=dias, y=valores)
        plt.plot(dias, regr.predict(dias),
             color='blue',
             label = "Regressão Linear")

        x, y = zip(*mLista)
        plt.plot(x, y, label=nome+str(" - original"),
             marker='o',
             markerfacecolor='olive',
             markersize=12,
             color=cor,
             linewidth=4)

        plt.legend()
        plt.show()


class Despesa:
    def __init__(self, dicionario, cor, nome):
        self.dicionario = dicionario
        self.cor = cor
        self.nome = nome


maio = Despesa({1:130, 7:430, 16:80, 19:270, 27:580},'skyblue','maio')
junho = Despesa({1:60, 5:256, 13:295, 22:690, 29:280},'red','junho')
julho = Despesa({1:100, 4:790, 14:218, 26:479, 30:386},'olive','julho')
lista_despesas = [maio, junho, julho]

grafico = Grafico(lista_despesas)

id_maio = 0
grafico.regressao_linear(id_maio)

id_junho = 1
grafico.regressao_linear(id_junho)

id_julho = 2
grafico.regressao_linear(id_julho)