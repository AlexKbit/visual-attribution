import argparse
import io
import json
import numpy as np
import boto3
from PIL import Image

from flask import Flask, request


def load_dict(path):
    with open(path) as f:
        return json.load(f)


encoding_length_dict = load_dict('length_dict.json')
encoding_dress_type_dict = load_dict('dress_type_dict.json')
encoding_color_dict = load_dict('color_dict.json')
encoding_material_dict = load_dict('material_dict.json')


# AWS
aws_region = None

# SageMaker endpoints
color_endpoint_name = None
dress_type_endpoint_name = None
length_endpoint_name = None
material_endpoint_name = None


def decode_length(class_index):
    return encoding_length_dict[class_index]


def decode_dress_type(class_index):
    return encoding_dress_type_dict[class_index]


def decode_color_type(class_index):
    return encoding_color_dict[class_index]


def decode_material_type(class_index):
    return encoding_material_dict[class_index]


def image_to_byte_array(image: Image):
    io_byte = io.BytesIO()
    image.save(io_byte, format=image.format)
    byte_arr = io_byte.getvalue()
    return byte_arr


def call_predict_class(session, endpoint_name, blob_img):
    response = session.invoke_endpoint(EndpointName=endpoint_name,
                                       ContentType='application/x-image',
                                       Body=blob_img)
    body = response['Body'].read().decode('utf-8')
    result = json.loads(body)
    return np.argmax(result)


app = Flask(__name__, static_url_path="", static_folder="static")


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/predict', methods=['POST'])
def get_prediction():
    bim = request.files['image'].stream
    img = Image.open(bim)
    img_arr = image_to_byte_array(img)

    session = boto3.Session().client(service_name='runtime.sagemaker', region_name=aws_region)

    color = call_predict_class(session, color_endpoint_name, img_arr)
    dress_type = call_predict_class(session, dress_type_endpoint_name, img_arr)
    length = call_predict_class(session, length_endpoint_name, img_arr)
    material = call_predict_class(session, material_endpoint_name, img_arr)

    return json.dumps({'color': decode_color_type(color),
                       'length': decode_length(length),
                       'dress_type': decode_dress_type(dress_type),
                       'material': decode_material_type(material)})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--web_app_port', default='9000')
    parser.add_argument('--aws_region', required=True)
    parser.add_argument('--color_endpoint_name', required=True)
    parser.add_argument('--dress_type_endpoint_name', required=True)
    parser.add_argument('--length_endpoint_name', required=True)
    parser.add_argument('--material_endpoint_name', required=True)
    args = parser.parse_args()
    color_endpoint_name = args.color_endpoint_name
    dress_type_endpoint_name = args.dress_type_endpoint_name
    length_endpoint_name = args.length_endpoint_name
    material_endpoint_name = args.material_endpoint_name
    aws_region = args.aws_region
    app.run(host='0.0.0.0', port=args.web_app_port)
