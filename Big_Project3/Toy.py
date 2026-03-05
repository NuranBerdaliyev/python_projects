class Toy:
    _owner='Nuran'
    def __init__(self, name, price, type):
        self._name=name
        self._price=price
        self._type=type
    
    

class Doll(Toy):
    def __init__(self, name, price, type, kind):
        if self.valid_type(type):
            super().__init__(name, price, type.lower().strip())
            self.__kind=kind
            self.__password=None
        else: 
            raise ValueError
    def valid_type(self, type):
        return isinstance(type, str) and type.lower().strip()=='doll'
    def __repr__(self):
        return f'Name: {self._name}\nPrice: {self._price}\nType: {self._type}\nKind: {self.__kind}'
    def change_password(self):
        ownerr=input("Say toys owner's name to change password: ")
        if ownerr!=Doll._owner:
            raise ValueError("Wrong answer")
        self.__password=input("Set the new password: ").strip()
example=Doll("Pennywise", 1200, "  DOLl    ", "The Dancing Clown")
while True:
    try:
        i=int(input("You can either find out toy data(1) or change its password(2) if you are owner. Or get the fuck out!(0)"))
    except (ValueError, TypeError):
        print("Choose one of 0 1 2, you're stupid bitch")
        continue
    if i==0:
        break
    elif i==1:
        print(example)
    elif i==2:
        try:
            example.change_password()
        except ValueError as v:
            print(v)
            continue
        
        print("Ok")



    

        
    
    
    