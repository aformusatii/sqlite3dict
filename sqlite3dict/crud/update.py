from .query import Query
from .safejson import SafeJson as json

# ******************************************************************************
# * Update Class
# ******************************************************************************
class Update:
    
    # ==========================================================================
    def __init__(self, table_name, table_meta, storage):
        self.table_name = table_name
        self.table_meta = table_meta
        self.storage = storage
        self.p_where = None
        self.p_data = None
        
    # ==========================================================================
    def byId(self, _id):
        return self.where("ID = '{}'".format(_id))
        
    # ==========================================================================
    def where(self, p_where):
        self.p_where = p_where
        return self
        
    # ==========================================================================
    def data(self, p_data):
        self.p_data = p_data
        return self
    
    # ==========================================================================
    def __build_query(self, columns):
        cols = ["{} = ?".format(column) for column in columns]
        
        sql = "UPDATE " + self.table_name + " SET " + ",".join(cols)

        if self.p_where is not None:
            sql = sql + " WHERE " + self.p_where
        
        return sql
        
    # ==========================================================================
    def execute(self):
        
        query = Query(self.table_name, self.table_meta, self.storage)
        
        items = query.where(self.p_where).execute()
        
        for item in items:
            columns = []
            params = []
    
            for column in self.table_meta["columns"]:
                if column in self.p_data:
                    columns.append(column)
                    params.append(self.p_data[column])
            
            item.update(self.p_data)
            
            columns.append("JSON_DATA")
            params.append(json.dumps(item))
            
            self.byId(item["id"])

            sql = self.__build_query(columns)
            
            cursor = self.storage.conn.cursor()
            cursor.execute(sql, params)
        
            self.storage.conn.commit()
        
        return True