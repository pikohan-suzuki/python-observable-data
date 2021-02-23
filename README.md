# python-observable_data
## Overview
This package provides the feature to notify you of data changes.

## Observer Class  
In this class, set the callback when the change of ObservableData is notified.

### method  
- Observer **.__init__(self, func:Callable[[T], None]**  
    Set the callback to be executed when a data change is notified.
- Observer **.on_changed()**  
    This method is executed when ObservableData changes are notified and is usually not executed manually.
  
##  ObservableData Class
This class holds the data and sends a notification to the configured observer when the data changes.  

### property  
- **.value**  
      Data held by the class. 
### methods
- ObservableData **.__init__(self, data: T)**  
    In the argument data, set the data to be monitored.
- ObservableData **.observe(self, Observer)**  
    Add an Observer to send notifications when data changes.
    
## Sample
### python code  
```
def on_data_changed(value):
    print(f"data changed to {value} !!")

observable_data = ObservableData("egg")
observable_data.observe(Observer(on_data_changed))
observable_data.value = "chicken"
```
### output  
```
data changed to chicken !!
```
