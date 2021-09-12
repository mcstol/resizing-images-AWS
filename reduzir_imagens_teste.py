import boto3
import os
import sys

from PIL import Image

s3_client = boto3.client("s3")


def reduzir_tamanho_imagem(input_dir, output_dir, output_dir_300):

    with Image.open(input_dir) as imagem:
        imagem_resize = imagem.resize((80, 80))
        imagem_resize.save(output_dir)
        imagem_resize_300 = imagem.resize((300, 300))
        imagem_resize.save(output_dir_300)


def handler(event, context):
    print(event)
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]
        download_path = "/tmp/{}".format(key)
        upload_path = "/tmp/resized-{}".format(key)
        upload_path_300 = '/tmp/300-{}'.format(key)

        s3_client.download_file(bucket, key, download_path)
        reduzir_tamanho_imagem(download_path, upload_path, upload_path_300)
        s3_client.upload_file(upload_path, bucket, 'imagem/{}'.format(key))
        s3_client.upload_file(upload_path_300, bucket, '300/{}'.format(key))
