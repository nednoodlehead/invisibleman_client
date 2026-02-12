# the purpose of this file is to take an export from intune (full data) and insert into invisman
# it will be a non-invasive insert, so no overwritting existing devices
# a report will be generated afterwards for any types that exist in both invis (before insert) and in the supplied xlsx file
# this will hopefully eliviate instances where partial data is inserted beforehand, and intune has more data, but due to the non-invasiveness, it will not overwrite with new data
# the report will be generated in the same manner to the reports, opening in default report directory and opening according to the suer preferences
import openpyxl
import re
from datetime import datetime
from util.export import export_all, export_extra_intune_data
from util.data_types import create_inventory_object
from db.fetch import fetch_all_serial
from volatile.write_to_volatile import read_from_config
from dateutil.relativedelta import relativedelta
from db.insert import new_entry

def import_intune(nst, intune_file, dir, time_stamp, csv: bool):
    # nst is the `self` of the program
    # if intune_file should probably check if this can be empty. ughghg
    # sort of unsure to have this directly mapped to the columns because microsoft loves changing stuff.
    # sort of realizing if we base this on column names, that is just as likely to be changed as the order or whaetever. hardcoding is easier
    intune_list = []
    # also annoying news we need to read the config file for time...
    # assume everything is user hardware??
    y = openpyxl.open(intune_file)
    wb = y.active
    
    def convert(name, sn, manu, model, management_name, prim_user): # not importing for type hinting. util\data_ytpes.py InventoryObjec
        assettype = None
        cost = 0
        pattern = r'(\d{1,2})\/(\d{1,2})\/(\d{4})'
        matches = re.findall(pattern, management_name)[0]
        deployment_date = datetime(month=int(matches[0]), day=int(matches[1]), year=int(matches[2])).date()
        replacement_date = deployment_date + relativedelta(years=5)
        status = "active"
        return create_inventory_object(
            assettype,
            manu,
            sn,
            model,
            cost,
            prim_user,
            name,
            "",
            "",
            deployment_date,
            replacement_date,
            None,
            "",
            status,
            False
            
        )
        

            
    count = 1
    while True:
        count += 1
        if not wb[f"A{count}"].value:
            break
        intune_list.append(convert(wb[f'B{count}'].value, wb[f'I{count}'].value, wb[f'J{count}'].value, wb[f'K{count}'].value, wb[f'X{count}'].value, wb[f'AC{count}'].value))
    # wait here to continue and insert just incase there are errors, don't want half of them inserting.
    # first, we make a backup for the user.
    existing_entries = []
    serials = fetch_all_serial(nst.connection)
    export_all(nst, csv, dir, time_stamp)
    for obj in intune_list:
        if obj.serial in serials:
            # we found this list already...
            existing_entries.append([*obj])
        else:
            # insert into db
            print("GONNA INSERT", obj.name)
            new_entry(nst.connection, obj)
    export_extra_intune_data(nst, csv, dir, time_stamp, existing_entries)    
            

        

        
