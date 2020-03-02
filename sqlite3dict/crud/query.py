from .safejson import SafeJson as json

order_type_enum = ["ASC", "DESC"]
# ******************************************************************************
# * Query Class
# ******************************************************************************
class Query:
    
    # ==========================================================================
    def __init__(self, table_name, table_meta, storage):
        self.table_name = table_name
        self.table_meta = table_meta
        self.storage = storage
        self.order_list = []
        self.p_where = None
        self.p_where_args = None
        self.p_limit = None
        self.p_offset = None

    # ==========================================================================
    def byId(self, _id):
        return self.where("ID = '{}'".format(_id))
    
    # ==========================================================================
    def where(self, p_where, p_where_args = []):
        self.p_where = p_where
        self.p_where_args = p_where_args
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
        
        if order_dir.upper() not in order_type_enum:
            raise ValueError("Invalid order [{}] expected {}.".format(order_dir.upper(), order_type_enum))
        
        if order_column not in self.table_meta["columns"]:
            raise ValueError("Invalid column name [{}].".format(order_column))
            
        self.order_list.append((order_column, order_dir))
        return self
    
    # ==========================================================================
    def __build_query(self):
        sql_args = []
        sql = "SELECT ID, JSON_DATA FROM " + self.table_name

        if self.p_where is not None:
            sql = sql + " WHERE " + self.p_where
            sql_args.extend(self.p_where_args)
            
        if len(self.order_list) > 0:
            orders = ["%s %s" % order for order in self.order_list]
            sql = sql + " ORDER BY " + ",".join(orders)
        
        if self.p_limit is not None:
            sql = sql + " LIMIT ? "
            sql_args.append(self.p_limit)
            
        if self.p_offset is not None:
            sql = sql + " OFFSET ? "
            sql_args.append(self.p_offset)
        
        return sql, sql_args
        
    # ==========================================================================
    def execute(self):
        sql, sql_args = self.__build_query()
        
        cursor = self.storage.conn.cursor()
        cursor.execute(sql, sql_args)
        rows = cursor.fetchall()
        
        result_list = []
        for row in rows:
            _id = row[0]
            _obj = json.loads(row[1])
            _obj["id"] = _id
            result_list.append(_obj)
        
        return result_list