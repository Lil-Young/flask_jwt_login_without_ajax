"""
Data Transfer Object를 정의합니다.
"""
class User:
    def __init__(self, id, pw, name, age):
        self.id = id
        self.pw = pw
        self.name = name
        self.age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age<0:
            raise ValueError('age is postive number')
        self._age=age
    
if __name__=='__main__':
    user = User('testid', 'testpw', 'test', 20)    
    print(user.__dict__)