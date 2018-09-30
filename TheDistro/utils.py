from .models import Data

def get_data():
    
    data = Data.objects.filter(id=1)
    
    if data.exists():
        data = data.first().as_dict()
        
    else:
        data = {}
        
    return data