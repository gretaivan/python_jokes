class Joke(): 

    def __init__(self, data): 
        print(data)
        # self._id = data['id']
        self._type = data['type'] 
        self._setup = data['setup']
        self._punchline = data['punchline']
        
    @property
    def get_id(self): 
        return self._id