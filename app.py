from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions
from controllers import jokes

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Joke API!'}), 200

@app.route('/jokes', methods=['GET', 'POST'])
def jokes_handler(): 
    fns = {
        'GET': jokes.show
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code



@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404


if __name__ == "__main__":
    app.run(debug=True)
