from typing import TypeVar,Callable,Generic,List
from observer import Observer

T = TypeVar('T')
class ObservableData(Generic[T]):
    def __init__(self,data:T) -> None:
        self.data = data
        self.observers:List[Observer] = []
    
    @property
    def value(self) -> T:
        print("value_getter")
        return self.data

    @value.setter
    def value(self,value:T):
        self.data = value
        self.__notificate()

    def observe(self,observer:Observer):
        self.observers += [observer]

    def __notificate(self):
        for observer in self.observers:
            observer.on_changed(self.data)
