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


"""
Here is the 'changed' table
It is a table of devices that have had their location / name changed, so we can update external trackers accurately
this is sort of an optional tracker? other organizations probably dont have this need, maybe make this configurable somewhere...

weirdly enough I don't see a reason for a pk. we are querying only by month, never updating this...
if a change happens twice (lpt -> lpt2 2021/01/01. lpt2 -> lpt3 2021/01/05), only the recent one is pulled?

create table changed
    old_name text,
    new_name text,
    old_location text,
    new_location text,
    edit_date date

"""
