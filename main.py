import os
from PIL import Image

def reduzir_tamanho_imagem(input_dir) :
    path = input_dir.split('/')
    if path[0]  == 'imagem':
        print('caminho correto!')
        output_dir_300 = '{}/300'.format(path[0])
        output_dir_100 = '{}/100'.format(path[0])
        print(output_dir_100)
        print(output_dir_300)
        with Image.open(input_dir) as imagem:

            # imagem_resize_300 = imagem.thumbnail((300,300))
            imagem.show()
            # imagem_resize_300.save(os.path(output_dir_300))
            imagem_resize_100 = imagem.resize((100,100))
            # imagem_resize_100.save(os.path(output_dir_100))
    else:
        print('caminho errado!')



if __name__ == '__main__':
    diretorio = '/home/marcelo/Imagens'
    diretorio2 = 'imagem/71002.jpg'
    reduzir_tamanho_imagem(diretorio2)
