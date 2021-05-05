from werkzeug.exceptions import BadRequest
from .api import fetch_random_joke
from flask import jsonify
import random

jokes = [
    {"id":255,"type":"general","setup":"What is a vampire's favorite fruit?","punchline":"A blood orange."},
    {"id":221,"type":"general","setup":"What do you call a group of killer whales playing instruments?","punchline":"An Orca-stra."},
    {"id":37,"type":"general","setup":"Why did the mushroom get invited to the party?","punchline":"Because he was a fungi."},
    {"id":60,"type":"programming","setup":"A user interface is like a joke.","punchline":"If you have to explain it then it is not that good."},
    {"id":126,"type":"general","setup":"How do you get a baby alien to sleep?","punchline":" You rocket."},
    {"id":289,"type":"general","setup":"What’s brown and sounds like a bell?","punchline":"Dung!"},
    {"id":294,"type":"general","setup":"When do doctors get angry?","punchline":"When they run out of patients."},
    {"id":134,"type":"general","setup":"How does a dyslexic poet write?","punchline":"Inverse."},
    {"id":114,"type":"general","setup":"How are false teeth like stars?","punchline":"They come out at night!"},
    {"id":180,"type":"general","setup":"What did the Buffalo say to his little boy when he dropped him off at school?","punchline":"Bison."}]


def show(req):
    # joke = fetch_random_joke()
    joke = random.choice(jokes)
    return joke, 200

    #return jsonify({'id': joke.get_id}), 200
    # import of api request for random joke 


def find_by_uid(uid):
    try:
        return next(joke for joke in jokes if joke['id'] == uid)
    except:
        raise BadRequest(f"We don't have that cat with id {uid}!")