from collections import defaultdict
from BigProjects.Big_Project3.parser.parser import text_extracted
def build_index(words):
    index=defaultdict(int)
    for text in words:
        index[text]+=1
    return index
d=build_index(text_extracted)
if __name__=='__main__':
    
    print(d)