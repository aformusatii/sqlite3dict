import sqlite3

from .collection import Collection

class Storage:
    
    # ==========================================================================
    def __init__(self, db_file):
        self.data = []
        self.db_file = db_file
    
    # ========================================================================== 
    def connect(self):
        self.conn = sqlite3.connect(self.db_file)
        self.__load_table_meta()
        
    # ==========================================================================
    def close(self):
        self.conn.commit()
        self.conn.close()
    
    # ==========================================================================    
    def __enter__(self):
        self.connect()
        return self
    
    # ==========================================================================        
    def __exit__(self, type, value, traceback):
        self.close()
    
    # ==========================================================================    
    def __load_table_meta(self):
        cursor = self.conn.cursor()
        
        self.table_meta = {}
        
        # Find all tables in database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        
        for table in tables:
            t_name = table[0]
            
            t_meta = {"columns":{}}
            self.table_meta[t_name] = t_meta
            
            # Find all columns for given table
            cursor.execute("SELECT name, type FROM pragma_table_info('{}')".format(t_name))
            columns = cursor.fetchall()
            for column in columns:
                c_name = column[0]
                c_type = column[1]
                t_meta["columns"][c_name] = c_type
    
    # ==========================================================================
    def __table_exists(self, table_name):
        return table_name in self.table_meta
        
    # ==========================================================================
    def __create_table(self, table_name, definitions):
        cursor = self.conn.cursor()
        
        col_builder = "ID CHAR(36) PRIMARY KEY"
        columns = []
        
        for definition in definitions:
            col_builder = col_builder + ", {} {}".format(definition, definitions[definition])
            columns.append(definition)
        
        col_builder = col_builder + ", JSON_DATA TEXT NOT NULL"
        
        cursor.execute("CREATE TABLE {} ({})".format(table_name, col_builder))
        
        cursor.execute("CREATE INDEX index_{} ON {}({})".format(table_name, table_name, ",".join(columns)))
        
        self.conn.commit()
        
        self.__load_table_meta()

    # ==========================================================================
    def __delete_table(self, table_name):
        cursor = self.conn.cursor()
        cursor.execute("DROP TABLE {}".format(table_name))
        self.conn.commit()

    # ==========================================================================
    def init_collection(self, collection, definitions):
        if not self.__table_exists(collection):
            self.__create_table(collection, definitions)   
            
        return Collection(self, collection, self.table_meta[collection])
            
    # ==========================================================================
    def delete_collection(self, collection):
        self.__delete_table(collection)
        
    # ==========================================================================
    def query_native(self, sql):
        cursor = self.conn.cursor()

        cursor.execute(sql)
        rows = cursor.fetchall()
        
        names = [description[0] for description in cursor.description]
        
        result_list = []
        for row in rows:
            item = {}
            for index in range(len(row)):
                key = names[index]
                item[key] = row[index]
                
            result_list.append(item)        
            
        return result_list    
    