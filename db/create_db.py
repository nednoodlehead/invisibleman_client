import psycopg2

# this is not used anymore, we will leave this here though, since it shows our table
def create_db(conn):
    # honestly there is probably some merit in messing with the nullif keywrods to store null better (and handle it better in invisman)
    # is_local is for computers that are not registered in intune. primarily adding so we can view the intune report more accurately
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
                     is_local bool,
                     loandate date,
                     returndate date
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

"""
Everything in this section are additional tables and triggers that need to be configured.
This comprises of two primary functions. One that creates the tables (which will also run alongside create_db(), and one to create triggers)
The tables can be ran normall, but the triggers will require the installation of plpython3u on the server
Typically it would seem advantageous to automate such a task, but i sort of dislike the prospect of the function being untrusted in the sense of anyone connected can run anything.

Yeah, I know anyone added to this program will be trusted, that is the entire point, but I still don't love the idea. Even from a "compromised credentials" view. (I'm not even sure if that is a valid complaint or not tbh)
So I'd rather recommend just copy pasting the stuff in. it is also how it is being run initially, since I'm fixing things and adapating on the fly!
"""
# def create_auditing_trigger_and_function(conn):
    # we don't need to audit the delete functions since there isn't any deleting operations in the database 
    

"""
create table audit (
    id serial primary key,
    uniqueid text REFERENCES main,
    is_update_function boolean, -- true if it is an update operation, false if it is an insert. delete does not exist and will not be tracked
    user text CURRENT_USER,
    changed_at timestamp CURRENT_TIMESTAMP,
    changed json,
)

create or replace function audit_trigger_func()
returns trigger as $$
declare
changed_json JSON := '{}'::JSON;
key TEXT;
old_val JSON;
new_val JSON;
begin
if TG_OP = 'UPDATE' THEN
    FOR key in SELECT json_object_keys(to_json(NEW))
    LOOP
    old_val := to_json(OLD)->key;
    new_val := to_json(NEW)->key;
        IF old_val is DISTINCT FROM new_val THEN
            SELECT json_build_object(key, json_build_array(old_val, new_val)) INTO changes_json;
        END IF;
    END LOOP; 
    if changes_json != '{}'::JSON THEN
    insert into audit (is_update_function, uniqueid) values (true, NEW.uniqueid)
    RETURN NEW;
ELSIF TG_OP = 'INSERT' THEN
    insert into audit (is_update_function, uniqueid, changed) VALUES
        (false, NEW.uniqueid, to_json(NEW))
    RETURN NEW;
ELSE
    RETURN OLD;
END IF;
    
"""
