# python-observable_data
## Overview
This package provides the feature to notify you of data changes.

## Observer Class  
In this class, set the callback when the change of ObservableData is notified.

### method  
- Observer **.on_changed()**  
    This method is executed when ObservableData changes are notified and is usually not executed manually.
  
##  ObservableData Class
This class holds the data and sends a notification to the configured observer when the data changes.  

### property  
- **.value**  
      Get and change data.
### method
- ObservableData **.observe(Observer)**  
      
    
