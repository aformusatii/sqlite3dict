from .crud.insert import Insert
from .crud.query import Query
from .crud.delete import Delete
from .crud.update import Update

# ******************************************************************************
# * Collection Class
# ******************************************************************************
class Collection:
    
    # ==========================================================================
    def __init__(self, storage, table_name, table_meta):
        self.table_name = table_name
        self.storage = storage
        self.table_meta = table_meta
        
    # ==========================================================================
    def insert(self, entity):
        return Insert(self.table_name, self.table_meta, self.storage).insert(entity)
        
    # ==========================================================================
    def query(self):
        return Query(self.table_name, self.table_meta, self.storage)
        
    # ==========================================================================
    def delete(self):
        return Delete(self.table_name, self.storage)
        
    # ==========================================================================
    def update(self):
        return Update(self.table_name, self.table_meta, self.storage)


