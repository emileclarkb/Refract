# ASSETS
from flask import Flask
from flask import render_template as render

# configure flask app
app = Flask('Refract')
# change folder locations
app.template_folder = 'Core/Templates'
app.static_folder = 'Core/Static'

# ROUTES
@app.route('/')
@app.route('/home')
def index():
    return render("index.html")

@app.route('/portrait')
def portrait():
    return render("portrait.html")

@app.route('/loading')
def loading():
    return render('loading.html')

def main():
    # run on localhost
    app.run(host='127.0.0.1', port=5000)

if __name__ == '__main__':
    main()
