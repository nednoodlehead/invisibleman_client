# inventory / asset management application
from db import create_db
from db import insert
from util.data_types import create_inventory_object
import datetime

m = create_inventory_object("namer", "serial :DD", "asus?", 10.00, "HARDWARE", "computer",
                            "nedly", "gov", datetime.date.today(), datetime.date.today(), "no notes here..")
insert.new_entry(m)
