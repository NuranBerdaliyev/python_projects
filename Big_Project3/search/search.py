from BigProjects.Big_Project3.index.indexation import d
def search(query, index):
    return index.get(query.lower(), 0)
if __name__=='__main__':
    t=search('null', d)
    print(t)
