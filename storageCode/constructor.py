from abc import ABC, abstractmethod


class selectApp(ABC):
    
    @abstractmethod
    def caminho_app(self,w,t) : 
        self.w = w
        self.t = t
        