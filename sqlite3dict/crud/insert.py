import uuid

from .safejson import SafeJson as json

# ******************************************************************************
# * Insert Class
# ******************************************************************************
class Insert:
    
    # ==========================================================================
    def __init__(self, table_name, table_meta, storage):
        self.table_name = table_name
        self.storage = storage
        self.table_meta = table_meta
    
    # ==========================================================================
    def insert(self, entity):
        cursor = self.storage.conn.cursor()
        
        columns = []
        marks = []
        params = []
        _id = None

        for column in self.table_meta["columns"]:
            if column in entity:
                params.append(entity[column])
                
                if column == "ID":
                    _id = entity[column]
                
            elif column == "ID":
                _id = str(uuid.uuid1())
                params.append(_id)
                
            elif column == "JSON_DATA":
                params.append(json.dumps(entity))
                
            else:
                continue
            
            columns.append(column)
            marks.append("?")
        
        sql = "INSERT INTO {}({}) VALUES({})".format(self.table_name, ",".join(columns), ",".join(marks))
        
        cursor.execute(sql, params)
        
        self.storage.conn.commit()
        
        return _id