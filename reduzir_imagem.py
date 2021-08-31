import boto3
import os
import sys

from PIL import Image

s3_client = boto3.client("s3")


def reduzir_tamanho_imagem(input_dir, output_dir):

    with Image.open(input_dir) as imagem:
        imagem_resize = imagem.resize((300, 300))
        imagem_resize.save(output_dir)


def handler(event, context):
    print(event)
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]
        download_path = "/tmp/{}".format(key)
        upload_path = "/tmp/resized-{}".format(key)

        s3_client.download_file(bucket, key, download_path)
        reduzir_tamanho_imagem(download_path, upload_path)
        s3_client.upload_file(upload_path, "{}-resized".format(bucket), key)
