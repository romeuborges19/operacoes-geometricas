import numpy as np


class OperacaoAritmetica:

    def __init__(self, imagem_1, imagem_2):
        self.imagem_1 = np.array(imagem_1)
        self.imagem_2 = np.array(imagem_2)

    def __verificar_tamanho_soma(self, matriz_verificada):
        # Verificar matriz para valores maiores que 255
        for i in range(len(matriz_verificada)):
            for j in range(len(matriz_verificada[0])):
                if matriz_verificada[i][j] > 255:
                    matriz_verificada[i][j] = 255

        return matriz_verificada

    def __verificar_tamanho_substracao(self, matriz_verificada):
        # Verificar matriz para valores menores que 0
        for i in range(len(matriz_verificada)):
            for j in range(len(matriz_verificada[0])):
                if matriz_verificada[i][j] < 0:
                    matriz_verificada[i][j] = 0

        return matriz_verificada

    def __adicao(self):
        return self.__verificar_tamanho_soma(self.imagem_1 + self.imagem_2)

    def __subtracao(self):
        return self.__verificar_tamanho_substracao(self.imagem_1 - self.imagem_2)

    def operacao_aritmetica(self):
        resultado_soma = self.__adicao()
        resultado_subtracao = self.__subtracao()
        return np.matrix(resultado_soma), np.matrix(resultado_subtracao)
