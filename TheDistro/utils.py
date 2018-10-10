from .models import Data

def get_data(query):
    
    data = Data.objects.filter(id=1)
    
    if data.exists():
        data = data.first().as_dict(query=query)
        
    else:
        data = {}
        
    return data