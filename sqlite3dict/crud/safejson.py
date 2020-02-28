import json

from datetime import datetime

class SafeJsonClass:

    # ************************************************************
    def dumps(self, obj):
        return json.dumps(obj, default = custom_converted)
    
    # ************************************************************        
    def loads(self, obj):
        return json.loads(obj)

# ************************************************************        
SafeJson = SafeJsonClass()
        
# ************************************************************
def custom_converted(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]