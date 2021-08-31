import os
from PIL import Image

def reduzir_imagem (input_dir, output_dir):
    arquivo  = input_dir.split('/')
    img = arquivo[len(arquivo)-1]
    del arquivo[-1]
    pasta = '/'.join(arquivo)
    if pasta == 'imagem':
        output_dir_300 = '{}/300'.format(pasta)
        output_dir_100 = '{}/100'.format(pasta)
        print(output_dir_100)
        print(output_dir_300)
        with Image.open(input_dir) as imagem:
            imagem_resize_300 = imagem.resize((300,300))
            imagem_resize_300.save(os.path.join(output_dir_300, img))
            imagem_resize_100 = imagem.resize((100,100))
            imagem_resize_100.save(os.path.join(output_dir_100, img))
    else:
        print('Diretorio errado!')

if __name__ == '__main__':
    diretorio = 'imagem'
    diretorio2 = 'imagem/100/71002.jpg'

    reduzir_imagem(diretorio2, '')
