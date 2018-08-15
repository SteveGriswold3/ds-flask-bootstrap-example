from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/layout')
def layout_example():
    return render_template('layout_example.html')


app.run(host='0.0.0.0', port='8080', debug=True)
