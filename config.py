import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'very-obscure-key'

basedir = os.path.abspath(os.path.dirname(__file__))

BINGAPI = 'a7ec019ba2cc4014ace305f9c83354b8'
save_image_location = os.path.abspath(os.path.dirname(__file__)) + '\\app\\static\\'
