from storage.storage import Storage

from datetime import datetime

# ******************************************************************************
# * Test
# ******************************************************************************
with Storage("test.sqlite") as store:

    definitions = {
        "name": "TEXT", 
        "age": "INTEGER", 
        "amount": "DOUBLE", 
        "createdate": "DATETIME",
        "resident": "BOOLEAN"
    }

    collection = store.init_collection("main", definitions)
    
    collection.insert({
        "name": "John Doe", 
        "age": 25, 
        "amount": 100.23, 
        "createdate": datetime.now(),
        "resident": True
    })
    
    collection.insert({
        "name": "John Doe", 
        "age": 10, 
        "amount": 100.00, 
        "createdate": datetime.now(),
        "resident": True
    })
    
    # list = collection.query().where("col1 = 'test adfdsaf'").limit(10).order("ID", "DESC").execute()
    
    collection.update().data({
        "createdate": datetime.now(), 
        "age": 15, 
        "amount": 99.38, 
        "resident": False
    }).where("age = 10").execute()
    
    list = collection.query().execute()
    for item in list:
        print("item:", item)
    
    # collection.delete().where("col1 = 'test adfdsaf'").execute()
    
    items = store.query_native("select * from main")
    for item in items:
        print("native item:", item)
        
    store.delete_collection("main")    
    