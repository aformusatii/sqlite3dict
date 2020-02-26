from .safejson import SafeJson as json

# ******************************************************************************
# * Query Class
# ******************************************************************************
class Query:
    
    # ==========================================================================
    def __init__(self, table_name, storage):
        self.table_name = table_name
        self.storage = storage
        self.order_list = []
        self.p_where = None
        self.p_limit = None
        self.p_offset = None

    # ==========================================================================
    def byId(self, _id):
        return self.where("ID = '{}'".format(_id))
    
    # ==========================================================================
    def where(self, p_where):
        self.p_where = p_where
        return self
        
    # ==========================================================================
    def limit(self, p_limit):
        self.p_limit = p_limit
        return self
        
    # ==========================================================================
    def offset(self, p_offset):
        self.p_offset = p_offset
        return self
        
    # ==========================================================================
    def order(self, order_column, order_dir = "ASC"):
        self.order_list.append((order_column, order_dir))
        return self
    
    # ==========================================================================
    def __build_query(self):
        sql = "SELECT ID, JSON_DATA FROM " + self.table_name

        if self.p_where is not None:
            sql = sql + " WHERE " + self.p_where
            
        if len(self.order_list) > 0:
            orders = ["%s %s" % order for order in self.order_list]
            sql = sql + " ORDER BY " + ",".join(orders)
        
        if self.p_limit is not None:
            sql = sql + " LIMIT " + str(self.p_limit)
            
        if self.p_offset is not None:
            sql = sql + " OFFSET " + str(self.p_offset)
        
        return sql
        
    # ==========================================================================
    def execute(self):
        sql = self.__build_query()
        
        cursor = self.storage.conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        
        result_list = []
        for row in rows:
            _id = row[0]
            _obj = json.loads(row[1])
            _obj["id"] = _id
            result_list.append(_obj)
        
        return result_list