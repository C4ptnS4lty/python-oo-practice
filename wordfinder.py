"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Initializes with a text document dictionary
    
    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat' or 'porcupine' or 'dog'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """

    def __init__(self, file) -> None:
        self.list = self.create(file)

        return f'{len(self.list)} words read'
    
    def create(file):
        items = []

        with open(file, 'r') as file:
            for line in file:
                items.append(line)

        return items

    def random(self):
        """Returns a random instance from the list"""
        import random
        return (random.choice(self.list))
    
"""Child of wordFinder. 
    Makes sure to avoid empty strings
    or strings starting with #
"""
class SpecialWordFinder(WordFinder):
    
    def create(file):

        items = []

        with open(file, 'r') as file:
            for line in file:
                if((not len(line) == 0) or (not line[0] == '#')):
                    items.append(line)

        return items

    

        

