from typing import TypeVar,Callable,Generic

T = TypeVar('T')

class Observer(Generic[T]):
    def __init__(self,func:Callable[[T],None]):
        self.on_changed_func = func

    def on_changed(self,value:T):
        self.on_changed_func(value)
