import numpy as np


class OperacaoAritmetica:

    def __init__(self, arquivo_matriz):
        self.matrizes = self._ler_matrizes(arquivo_matriz)

    def _ler_matrizes(self, arquivo):
        matrizes = []
        with open(arquivo, 'r') as f:
            conteudo = f.read()
            matrizes_txt = conteudo.strip().split('\n\n')

            for mariz_txt in matrizes_txt:
                linhas = mariz_txt.split('\n')  
                matriz = [] 
                
                for linha in linhas:
                    elementos = linha.split()  
                    linha_inteiros = []  
                    
                    for elemento in elementos:
                        linha_inteiros.append(int(elemento)) 
                    
                    matriz.append(linha_inteiros) 
                
                matrizes.append(np.array(matriz))

        return matrizes

    def __adicao(self):
        print("soma: ", self.matrizes[0] + self.matrizes[1])
        return self.__verificar_tamanho_soma(self.matrizes[0] + self.matrizes[1])
    
    def __verificar_tamanho_soma(self, matriz_verificada):
        print(matriz_verificada)
        # verificar matriz para valores maiores que 255 e menores que 0
        for i in range(len(matriz_verificada)):
            for j in range(len(matriz_verificada[0])):
                if matriz_verificada[i][j] > 255:
                    matriz_verificada[i][j] = 255

        return matriz_verificada
    
    def __verificar_tamanho_substracao(self, matriz_verificada):
        # menores que 0
        for i in range(len(matriz_verificada)):
            for j in range(len(matriz_verificada[0])):
                if matriz_verificada[i][j] < 0:
                    matriz_verificada[i][j] = 0

        return matriz_verificada
    
    def __subtracao(self):
        return self.__verificar_tamanho_substracao(self.matrizes[0] - self.matrizes[1])
    
    def _operacao_aritmetica(self):
        resultado_soma = self.__adicao()
        resultado_subtracao = self.__subtracao()
        return resultado_soma, resultado_subtracao