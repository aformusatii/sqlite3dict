
# ******************************************************************************
# * Delete Class
# ******************************************************************************
class Delete:
    
    # ==========================================================================
    def __init__(self, table_name, storage):
        self.table_name = table_name
        self.storage = storage
        self.p_where = None
        
    # ==========================================================================
    def byId(self, _id):
        return self.where("ID = '{}'".format(_id))
        
    # ==========================================================================
    def where(self, p_where):
        self.p_where = p_where
        return self
    
    # ==========================================================================
    def __build_query(self):
        sql = "DELETE FROM " + self.table_name

        if self.p_where is not None:
            sql = sql + " WHERE " + self.p_where
        
        return sql
        
    # ==========================================================================
    def execute(self):
        sql = self.__build_query()
        
        cursor = self.storage.conn.cursor()
        cursor.execute(sql)
        
        self.storage.conn.commit()
        
        return True