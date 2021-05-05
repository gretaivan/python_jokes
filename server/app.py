from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions
from controllers import jokes
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'hamiltonpearl@gmail.com'
# app.config['MAIL_PASSWORD'] = None
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '50813edb3f7d55'
app.config['MAIL_PASSWORD'] = '9a5d5ab3695617'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
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

# @app.route('/jokes')
# def get_joke(): 
#     return jokes.show

@app.route('/email')
def email_handler():
    msg = Message("Hello", sender='50813edb3f7d55', recipients=["kaketi7058@drluotan.com", "faisaly1234@outlook.com"])
    msg.body = "This is a message"
    mail.send(msg)
    
    return jsonify({'message': 'Email has been sent!'}), 200

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404


if __name__ == "__main__":
    app.run(debug=True)
