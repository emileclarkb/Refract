# ASSETS
from flask import Flask
from flask import render_template as render

app = Flask('Refract')

@app.route('/')
@app.route('/home')
def index():
    return render("index.html")


def main():
    # run on localhost
    app.run(host='127.0.0.1', port=5000)

if __name__ == '__main__':
    main()
