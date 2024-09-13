from operacao_aritmetica import OperacaoAritmetica
from operacao_geometrica import Reflexao

# from skimage.io import imread, imshow
from PIL import Image


def main():
    img = Image.open("imagens/image-1.png")
    img = img.convert("L")

    op_geometrica = Reflexao(img)
    img_refletida = op_geometrica.vertical_reflection()

    img_refletida = Image.fromarray(img_refletida)
    img_refletida.save("resultado-reflexao-v.png")

    op_geometrica = Reflexao(img)
    img_refletida = op_geometrica.horizontal_reflection()

    img_refletida = Image.fromarray(img_refletida)
    img_refletida.save("resultado-reflexao-h.png")

    img_2 = Image.open("imagens/image-2.jpeg")
    img_2 = img_2.convert("L")

    op_aritmetica = OperacaoAritmetica(imagem_1=img, imagem_2=img_2)
    soma, subtracao = op_aritmetica.operacao_aritmetica()

    soma = Image.fromarray(soma)
    soma.save("resultados/resultado-soma.png")

    subtracao = Image.fromarray(subtracao)
    subtracao.save("resultados/resultado-subtracao.png")

if __name__ == "__main__":
    main()
