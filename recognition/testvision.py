
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
import re

def detect_face(face_file):
    client = vision.ImageAnnotatorClient()
    content = face_file.read()
    image = types.Image(content=content)

    response = client.label_detection(image=image, max_results=20)
    labels = response.label_annotations
    isPorsche = False
    listaData = []
    for label in labels:
        data = label.description
        data = data.lower()
        listTemp = re.split(' ', data)
        if 'porsche' in listTemp:
            listaData.append(data)
            isPorsche = True
    return isPorsche, listaData

def highlight_obj(image, output_filename):
    im = Image.open(image)
    im.save("static/"+output_filename)


def StartDetec(image, output_filename="result.jpg"):
#    with open(input_filename, 'rb') as image:  #NO LO USAMOS PORQUE COMO RECIBE LE IMAGEN
#ESTA YA VIENE ABIERTA, SI FUERA UNA URL SI TENDRIAMOS QUE HABRIRLO PARA PROCEZARLO.
    porsche, listaData = detect_face(image)
    image.seek(0)
    highlight_obj(image, output_filename)
    if porsche:
        listaData.insert(0, 'Es Porche Modelo:')
        resultado = (listaData)
    else:
        resultado = (['No es Porsche'])
    return resultado
