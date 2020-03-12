from flask import Flask, request, send_file, jsonify
from PIL import Image
import base64
from flask_swagger import swagger

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello world!"

# @app.route("/spec")
# def spec():
#     return jsonify(swagger(app))


@app.route('/img', methods=['POST'])
def img():

    filename = 'dogs.png'
    final_filename = 'edit.png'

    request_data = request.json                 # get client's request data
    print(request_data)

    encoded_img = request_data['image']         # decode image
    decoded_img = base64.b64decode(encoded_img)

    img_handler = open(filename, "wb+")         # write image to file
    img_handler.write(decoded_img)
    img_handler.close()

    del request_data['image']                   # delete image str - no longer needed

    process_img(request_data, filename)         # process img based on operations

    return send_file(final_filename, mimetype='image/gif')


def process_img(operations, fname):

    img = Image.open(fname)
    final_fname = 'edit.png'

    if 'flip' in operations:
        img = flip(img, operations['flip'])

    if 'rotate' in operations:
        img = rotate(img, operations['rotate'])

    if 'gray' in operations:

        img = gray(img, operations['gray'])

    if 'resize' in operations:
        img = resize(img, operations['resize'])

    if ('thumbnail' in operations) and (operations['thumbnail'] == 'true'):
        img = thumbnail(img)

    if 'rotateLeft' in operations:             #TODO: add check to see if true
        img = rotate_left(img)

    if 'rotateRight' in operations:           #TODO: add check to see if true
        img = rotate_right(img)

    img.save(final_fname)

    return


def flip(img, op):

    if op == 'vertical':
        return img.transpose(Image.FLIP_LEFT_RIGHT)
    elif op == 'horizontal':
        return img.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        return img


def rotate(img, op):

    return img.rotate(op)


def gray(img, op):

    if op == "true":
        return img.convert('LA')
    else:
        return img


def resize(img, op):

    dims = (op[0], op[1])
    return img.resize(dims)


def thumbnail(img):

    MAX_SIZE = (100, 100)
    img.thumbnail(MAX_SIZE)
    return img


def rotate_left(img):

    return img.rotate(90)


def rotate_right(img):

    return img.rotate(-90)


if __name__ == '__main__':
    app.run(host="localhost", port=5555, debug=True)
