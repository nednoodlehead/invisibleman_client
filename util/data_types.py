import datetime
from dateutil.relativedelta import relativedelta
import json
from uuid import uuid4

# should match the schema of /db/create_db.create_db()
class InventoryObject:
     def __init__(self, name: str, serial: str, manufacturer: str, price: float, assetcategory: str, assettype: str, assignedto: str, assetlocation: str, purchasedate: datetime.date, installdate: datetime.date, replacementdate: datetime.date, notes: str, status: bool, uniqueid: str):
          self.name = name  # name of device. e.g. SPENCER-APC
          self.serial = serial  # serial number of device
          self.manufacturer = manufacturer  # manufacturer of the device
          self.price = price  # cost of device at time of purchase
          self.assetcategory = assetcategory  # general category of object (network, security, software, printing)
          self.assettype = assettype  # what type of asset is it? (router, switch, all-in-one)
          self.assignedto = assignedto  # what person / dept is asset assigned to?
          self.assetlocation = assetlocation  # where is the asset? e.g. GOVH, HLTH (enum to pick from)
          self.purchasedate = purchasedate  # day item was purchased
          self.installdate = installdate  # day item was installed,
          self.replacementdate = replacementdate  # day the item should be replaced (years ahead from installdate. hardware = 4yr, print = 5yr)
          self.notes = notes  # other notes about the item
          self.status = status  # is item in production? bool. False = not in use, True = In use
          self.uniqueid = uniqueid  # uuid-4 for the device
     def __iter__(self):
         yield self.name 
         yield self.serial   
         yield self.manufacturer  
         yield self.price 
         yield self.assetcategory
         yield self.assettype
         yield self.assignedto 
         yield self.assetlocation
         yield self.purchasedate 
         yield self.installdate  
         yield self.replacementdate 
         yield self.notes
         yield self.status  
         yield self.uniqueid           
     def __str__(self):
          return f"Inventory_Object: {self.name} id: {self.uniqueid}"          
     def __repr__(self):
          return f"Inventory_Object: {self.name} id: {self.uniqueid}"          
def create_inventory_object(name: str, serial: str, manufacturer: str, price: float, assetcategory: str, assettype: str, assignedto: str, assetlocation: str, purchasedate: datetime.date, installdate: datetime.date, replacementdate: datetime.date, notes: str, status: str) -> InventoryObject:     
     with open(".\\volatile\\assetcategory.json") as f:
          raw_json = json.load(f)
     id = str(uuid4())
     if status == "Enabled":
          stat = True
     else:
          stat = False
     return InventoryObject(name, serial, manufacturer, price, assetcategory, assettype, assignedto, assetlocation, purchasedate, installdate, replacementdate, notes, stat, id)
     
class TableObject:
     # same as inventory object, but no self.enabled
     def __init__(self, name: str, serial: str, manufacturer: str, price: float, assetcategory: str, assettype: str, assignedto: str, assetlocation: str, purchasedate: datetime.date, installdate: datetime.date, replacementdate: datetime.date, notes: str, uniqueid: str):
          self.name = name  # name of device. e.g. SPENCER-APC
          self.serial = serial  # serial number of device
          self.manufacturer = manufacturer  # manufacturer of the device
          self.price = price  # cost of device at time of purchase
          self.assetcategory = assetcategory  # general category of object (network, security, software, printing)
          self.assettype = assettype  # what type of asset is it? (router, switch, all-in-one)
          self.assignedto = assignedto  # what person / dept is asset assigned to?
          self.assetlocation = assetlocation  # where is the asset? e.g. GOVH, HLTH (enum to pick from)
          self.purchasedate = purchasedate  # day item was purchased
          self.installdate = installdate  # day item was installed,
          self.replacementdate = replacementdate  # day the item should be replaced (years ahead from installdate. hardware = 4yr, print = 5yr)
          self.uniqueid = uniqueid
          self.notes = notes  # Will either be something (which will become a button to view notes), or nothing, that will be "No Notes"
          # similar to 
     def __iter__(self):
         yield self.name 
         yield self.serial   
         yield self.manufacturer  
         yield self.price 
         yield self.assetcategory
         yield self.assettype
         yield self.assignedto 
         yield self.assetlocation
         yield self.purchasedate 
         yield self.installdate  
         yield self.replacementdate 
         yield self.notes
         yield self.uniqueid
     def __len__(self):
          return 13
     def __str__(self):
          return f"Inventory_Object: {self.name}"          
     def __repr__(self):
          return f"Inventory_Object: {self.name}"          
                    
