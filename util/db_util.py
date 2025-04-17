# this is to fix the fact that there is no replacementdate in the table, but there is a deployment date
# okay, ive changed my mind. We will store unknown dates as Null, when we import them into the 'update' view,
# we will set their dates = 2000/01/01. If a date is stored as 2000/01/01, it will be parsed into Null.
# easy workaround..

def patch_dates(conn, mapping):
    # we will try to do this in one sql statement...?
    cur = conn.cursor()
    cur.execute("SELECT * from main;")
    before = cur.fetchall()
    for count, row in enumerate(before):
        deploy = row[9]
        if not deploy or deploy == "SKIP!":
            # i guess we just skip them?
            print(f'skipping {count}')
            continue
        asset_type = row[8]
        print(mapping)
        new_year_amount = f'{mapping[str(asset_type)]} year'
        cur.execute("UPDATE main set replacementdate = deploymentdate + interval %s", (new_year_amount,))
        print(f'fixed: {count}')
    conn.commit()

# we ran this in ui_functions.py after making the connection:
        # patch_dates(self.connection, self.fetch_categories_and_years()) # was a o
    
