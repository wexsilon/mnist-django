from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse

import numpy as np
import tensorflow as tf
import cv2


def guess_number(image):
    img = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2GRAY)
    array = tf.keras.utils.normalize([img], axis = 1)
    for i in array:
        np.expand_dims(i,axis = 0)
    new_model = tf.keras.models.load_model('mnist_save.model')
    new_model.load_weights('mnist.model.weights.best.hdf5')
    predictions = new_model.predict(array)
    return np.argmax(predictions[0])


def show_form(request: WSGIRequest):
    return render(request, 'input-image.html')

def get_result(request: WSGIRequest):
    if request.method == 'POST':
        image = request.FILES['image']
        with open(image.name, 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)
        context = {
            'num': guess_number(image.name)
        }
        return render(request, 'result.html', context)
        