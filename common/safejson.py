import json
from datetime import datetime

# ************************************************************
def dumps(obj):
    return json.dumps(obj, default = custom_converted)

# ************************************************************        
def loads(obj):
    return json.loads(obj)
    
# ************************************************************
def custom_converted(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]