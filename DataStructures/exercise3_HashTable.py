class HashTable:
    def __init__(self, MAX):
        self.MAX=MAX
        self.arr=[[] for _ in range(MAX)]
    
    def get_hash(self, key):
        h=0
        if isinstance(key, str):
            for ch in key:
                h+=ord(ch)
            h%=self.MAX
        elif isinstance(key, int):
            h=key%self.MAX
        return h
    def add(self, key, val):
        index=self.get_hash(key)
        for i, e in enumerate(self.arr[index]):
            if e[0]==key:
                self.arr[index][i]=(key, val)
                return
        self.arr[index].append((key, val))
        
    def get(self, key):
        index=self.get_hash(key)
        for i, e in enumerate(self.arr[index]):
            if e[0]==key:
                return e[1]
        return None
    
    def delete(self, key):
        index=self.get_hash(key)
        for i, e in enumerate(self.arr[index]):
            if e[0]==key:
                del self.arr[index][i]
                return True
        return False

    def __setitem__(self, key, value):
        self.add(key, value)
    
    def __getitem__(self, key):
        r=self.get(key)
        if r is None:
            raise KeyError(key)
        return r
    
h=HashTable(10)
for i in range(20):
    h[i]=float(i/100)
for i in range(20):
    u=h[i]
    print(u, end=" ")

    
