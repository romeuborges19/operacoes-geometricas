from operacao_aritmetica import OperacaoAritmetica
from operacao_geometrica import Reflexao  
from skimage.io import imread, imshow

def main():

    # arquivo_matriz = 'matriz.txt'
    # op_aritmetica = OperacaoAritmetica(arquivo_matriz)
    # matrizes_somadas, matrizes_subtraidas = op_aritmetica._operacao_aritmetica()
    
    img = imread('image.png')
    op_geometrica = Reflexao(img)
    img_refletida = op_geometrica._vertical_reflection()
    

    # arquivo_saida = 'matrizes.txt'
    # interpolador.salvar_matrizes_em_arquivo(matrizes_reduzidas, matrizes_ampliadas, arquivo_saida)

if __name__ == "__main__":
    main()