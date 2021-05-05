class Joke(): 

    def __init__(self, data): 
        self._id = data['id']
        self._type = data['type'] 
        self._setup = data['setup']
        self._punchline = data['punchline']
        