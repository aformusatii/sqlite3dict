from .storage import Storage

from datetime import datetime

# ******************************************************************************
# * Test
# ******************************************************************************
with Storage("test.sqlite") as store:

    print('sadfdsaf')

    definitions = {
        "name": "TEXT", 
        "age": "INTEGER", 
        "amount": "DOUBLE", 
        "createdate": "DATETIME",
        "resident": "BOOLEAN"
    }

    # This creates the table (collection) only if it does not exist already
    collection = store.init_collection("test", definitions)
    
    # Insert data
    collection.insert({
        "name": "John Doe", 
        "age": 25, 
        "amount": 100.23, 
        "createdate": datetime.now(),
        "resident": True,
        "additional": {
            "prop1": 1,
            "prop2": 1,
            "other": ["A", "B"]
        }
    })
    
    collection.insert({
        "name": "John Doe", 
        "age": 10, 
        "amount": 100.00, 
        "createdate": datetime.now(),
        "resident": True
    })
    
    # Update inserted data by given criteria
    collection.update().data({
        "createdate": datetime.now(), 
        "age": 15, 
        "amount": 99.38, 
        "resident": False
    }).where("age = 25").execute()
    
    # Simple query for data
    list = collection.query().where("age = ? or age = ?", [10, 15]).limit(10).offset(0).order("createdate", "ASC").order("ID").execute()
                     
    for item in list:
        print("item:", item)
    
    # Delete data by given criteria
    collection.delete().where("age = 15").execute()
    
    # Native SQL query in case you still need it
    items = store.query_native("select * from test")
    for item in items:
        print("native item:", item)
    
    # Drop table (collection)    
    store.delete_collection("test") 
    