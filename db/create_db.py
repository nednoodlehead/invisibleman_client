import sqlite3


# this is not used anymore, we will leave this here though, since it shows our table
def create_db():
    with sqlite3.connect("main.db") as conn:  # creates if not created already
        conn.execute(
            """
             CREATE TABLE IF NOT EXISTS main (
                         assettype text,
                         manufacturer text,
                         serial text,
                         model text,
                         cost decimal (6, 2),
                         assignedto text,
                         name text,
                         assetlocation text,
                         assetcategory text,
                         deploymentdate date,
                         replacementdate date,
                         retirementdate date,
                         notes mediumtext,
                         status bool,
                         uniqueid text PRIMARY KEY
                       )
                       """
        )
        conn.commit()
