from abc import ABCMeta, abstractmethod
from .DTO import User
class BaseModel(metaclass=ABCMeta):

    """
    User를 DB에 삽입하는 메소드
    """
    @abstractmethod
    def create_user(self, user:User):
        pass
    
    """
    id 중복 조회를 위한 메소드
    id를 통해 User를 읽는 메소드
    """
    @abstractmethod
    def read_user(self, id):
        pass
    
    """
    
    id에 해당하는 User의 key 정보를 value로 변경하는 메소드
    """
    @abstractmethod
    def update_user(self, id, key, value):
        pass
    
    @abstractmethod
    def delete_user(self, ):
        pass