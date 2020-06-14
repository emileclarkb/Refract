# ASSETS
from os import listdir
from os.path import isfile, join
import random

# Flask
from flask import Flask
from flask import render_template as render

# configure flask app
app = Flask('Refract')
# change folder locations
app.template_folder = 'Core/Templates'
app.static_folder = 'Core/Static'



# ROUTES
# default page
@app.route('/')
@app.route('/home')
def index():
    return render("index.html")

# portrait mode
@app.route('/portrait')
def portrait():
    # path to images
    path = 'Core/Static/imgs'

    # get all images
    imgs = []
    for file in listdir(path):
        if isfile(join(path, file)):
            imgs.append(file)

    # select random image
    img = random.choice(imgs)

    return render("portrait.html", img=)

# loading page
@app.route('/loading')
def loading():
    return render('loading.html')


# run flask app
def main():
    # run on localhost
    app.run(host='127.0.0.1', port=5000)

if __name__ == '__main__':
    main()
