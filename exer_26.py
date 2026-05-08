  
def fun(row, kwargs):
        for x,y in kwargs.items():
            if  str(y) in str(row[x]):
                return True
            else:
                return False
def fun_get(row, kwargs):
        
        for x,y in kwargs.items():
            if  y == row[x]:
                return True
            else:
                return False
            
class ObjectNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Model:
    __store = []
    _id = 0
              
    @classmethod
    def create(cls, **fields):
        cls.__store.append(fields)
        cls._id += 1

    @classmethod
    def all(cls):
        return cls.__store
    
 
    
    @classmethod
    def filter(cls,**kwargs):
        return list(filter(lambda x: fun(x,kwargs),cls.__store))
    
    @classmethod
    def get(cls,**kwargs):
        con = list(filter(lambda x: fun_get(x,kwargs),cls.__store))
        if len(con) == 1:
            return con
        elif len(con) == 0:
            (key, value), = kwargs.items()
            raise ObjectNotFound(f"No User matches {key}='{value}'")
        else:
            raise ObjectNotFound("An error occured")
        
   

class User(Model):
    def __init__(self,name,email,is_active=True) -> None:
        super().__init__()
        self.name = name
        self.email = email
        self.is_active = is_active
        super().create(name=self.name,email=self.email,is_active=self.is_active)

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}',email='{self.email}',is_active='{self.is_active}')"


    

    
    

    


    
user1 = User(name = "jupete",email = "bohdzomo3@gmail.com")
user2 = User(name = "mark",email = "markangel7@gmail.com")
user1 = User(name = "peter",email = "bobpeter2@gmail.com")
user2 = User(name = "eugene",email = "eugene6@gmail.com")
user1 = User(name = "angel",email = "angelle2@gmail.com")

print(user1)




