import json


class ReadFile:

    '''
    This class is for reading a the planetarySystem.json file and returns the
    contents of it. Specifically a Json file containing
     a dictionary -> list -> dictionary.
    '''

    def __init__(self):
        '''
        Creates an instance variable that contains a list. 
        '''
        self.data = []

    def read_json(self, path_to_json):
        '''
        Opens the planetarySystem.json, and returns the planet list.        
        '''
        with open(path_to_json) as f:
            self.data = json.load(f)['planets']

        return self.data
