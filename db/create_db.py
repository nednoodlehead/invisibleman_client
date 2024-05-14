import sqlite3


def create_db():
    with sqlite3.connect("main.db") as conn:  # creates if not created already
        conn.execute(
            """
                    CREATE TABLE IF NOT EXISTS main (
                         name text,
                         serial text,
                         manufacturer text,
                         model text,
                         price decimal (6, 2),
                         assetcategory text,  
                         assettype text,
                         assignedto text,
                         assetlocation text,
                         purchasedate date,
                         installdate date,
                         replacementdate date,
                         notes mediumtext,
                         status bool,                    
                         uniqueid text PRIMARY KEY
                       )
                       """
        )
        conn.commit()
