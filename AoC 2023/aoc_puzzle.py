# Basic puzzle class to help handel AoC puzzles
import os
from IPython.display import Markdown, display


class AocPuzzle():
    
    def __init__(self, data = None):
        if data:
            if os.path.exists(data):
                self.load_data(data)
            else:
                self.parse_data(data)
        else:
            self.data = data
        
    def load_data(self, path):
        with open(path) as file:
            raw_data = file.read()
        self.parse_data(raw_data)

    def run(self, testing=False):
        self.testing = testing
        result = self.solve()
        if not testing:
            display(Markdown(f'### Result is `{result}`'))            
        return result
