from collections import defaultdict

class Indexer:
    def __init__(self):
        self.index_dict=defaultdict(int)
    
    def add_words(self, words_list):
        for word in words_list:
            self.index_dict[word]+=1
    
    def get_count(self, word):
        return self.index_dict.get(word, 0)
    
    def __repr__(self):
        return str(self.index_dict)