import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'some-key-here'

basedir = os.path.abspath(os.path.dirname(__file__))

BINGAPI = os.environ['BINGAPIV7']
save_image_location = os.path.abspath(os.path.dirname(__file__)) + '/app/static/'
