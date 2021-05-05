from werkzeug.exceptions import BadRequest
from .api import fetch_random_joke

def show(req):
    return 'JOKES', 200
    # import of api request for random joke 
