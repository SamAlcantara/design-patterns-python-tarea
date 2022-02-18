
"""
SingleTon design pattern
"""

class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        print(cls.__instances)
        return cls.__instances[cls]

    
class DBConnector(metaclass=SingletonMeta):
    def __init__(self):
        self.status = "No conectada"

    def desconectada(self):
        self.status = "desconectada"

    def conectada(self):
        self.status = "Conectada"


cliente1 = DBConnector()
print("Cliente 1 ", cliente1)
print(cliente1.status)

cliente2 = DBConnector()
print("Cliente 2 ", cliente2)
cliente2.conectada()
print(cliente1.status)

cliente1.desconectada()
print(cliente2.status)

input()
