import boto3
import os
import sys

from PIL import Image

s3_client = boto3.client('s3')

def reduzir_imagem (input_dir, output_dir_300, output_dir_100):

    with Image.open(input_dir).convert('RGB') as imagem:
        largura_imagem = imagem.size[0]
        altura_imagem = imagem.size[1]
        percentual_largura = float(300.0)/float(largura_imagem)
        altura_desejada = int((altura_imagem*percentual_largura))
        imagem_resize_300 = imagem.resize((300,altura_desejada))
        imagem_resize_300.save(output_dir_300)
        imagem_resize_100 = imagem.resize((100,100))
        imagem_resize_100.save(output_dir_100)

def handler(event,context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        path_to_list = key.split('/')
        img = path_to_list[len(path_to_list)-1]
        del path_to_list[-1]
        path = '/'.join(path_to_list)

        if path == 'imagem/diasLiturgicos':
            download_path = '/tmp/{}'.format(img)
            upload_path_300 = '/tmp/resized_300-{}'.format(img)
            upload_path_100 = '/tmp/resized_100-{}'.format(img)

            s3_client.download_file(bucket, key, download_path)
            reduzir_imagem(download_path, upload_path_300, upload_path_100)

            s3_client.upload_file(upload_path_300,bucket, 'imagem/diasLiturgicos/300/{}'.format(img))
            s3_client.upload_file(upload_path_100, bucket, 'imagem/diasLiturgicos/80x80/{}'.format(img) )
