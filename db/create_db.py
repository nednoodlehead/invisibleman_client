import sqlite3

def create_db():
     conn = sqlite3.connect("main.db") # creates if not created already
     conn.execute("""
               CREATE TABLE IF NOT EXISTS main (
                    name text,
                    serial text,
                    manufacturer text,
                    price decimal (6, 2),
                    assetcategory text,  
                    assettype text,
                    assignedto text,
                    assetlocation text,
                    purchasedate datetime,
                    installdate datetime,
                    replacementdate datetime,
                    notes mediumtext,
                    status bool,                    
                    uniqueid text PRIMARY KEY
                  )


                       
                  """)
