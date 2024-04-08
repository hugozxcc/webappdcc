from flask import Flask

app = Flask(__name__)

# Endpoint 1
@app.route('/', methods=['GET'])
def hello():
    return 'Halo, ini web service simple saya'

# Endpoint 2
@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return f'Halo, {name}!'

# nambah2
@app.route('/greet', methods=['GET'])
def greet_myself():
    my_name = 'nama saya Fadil'
    return f'Halo, {my_name}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
