import datetime
from dateutil.relativedelta import relativedelta
import json
from uuid import uuid4


# should match the schema of /db/create_db.create_db()
class InventoryObject:
    def __init__(
        self,
        assettype: str,
        manufacturer: str,
        serial: str,
        model: str,
        cost: float,
        assignedto: str,
        assetlocation: str,
        assetcategory: str,
        deploymentdate: datetime.date,
        replacementdate: datetime.date,
        retirementdate: datetime.date | None,
        notes: str,
        status: bool,
        uniqueid: str,
    ):
        self.assettype = assettype
        self.manufacturer = manufacturer
        self.serial = serial
        self.model = model
        self.cost = cost
        self.assignedto = assignedto
        self.assetlocation = assetlocation
        self.assetcategory = assetcategory
        self.deploymentdate = deploymentdate
        self.replacementdate = replacementdate
        self.retirementdate = retirementdate
        self.notes = notes  # other notes about the item
        self.status = status
        self.uniqueid = uniqueid  # uuid-4 for the device

    def __iter__(self):
        yield self.assettype
        yield self.manufacturer
        yield self.serial
        yield self.model
        yield self.cost
        yield self.assignedto
        yield self.assetlocation
        yield self.assetcategory
        yield self.deploymentdate
        yield self.replacementdate
        yield self.retirementdate
        yield self.notes  # other notes about the ite
        yield self.status
        yield self.uniqueid  # uuid-4 for the devic

    def __str__(self):
        return f"Inventory_Object: {self.serial} id: {self.uniqueid}"

    def __repr__(self):
        return f"Inventory_Object: {self.serial} id: {self.uniqueid}"


def create_inventory_object(
    assettype: str,
    manufacturer: str,
    serial: str,
    model: str,
    cost: float,
    assignedto: str,
    assetlocation: str,
    assetcategory: str,
    deploymentdate: datetime.date,
    replacementdate: datetime.date,
    retirementdate: datetime.date,
    notes: str,
    status: str,  # active | retired
) -> InventoryObject:
    # with open(".\\volatile\\assetcategory.json") as f:  # what was the purpose of this ..?
    #     raw_json = json.load(f)
    id = str(uuid4())
    if status == "Enabled":
        stat = True
    else:
        stat = False
    return InventoryObject(
        assettype, 
        manufacturer,
        serial,
        model,
        cost,
        assignedto,
        assetlocation,
        assetcategory,
        deploymentdate,
        replacementdate,
        retirementdate,
        notes,
        True if status.lower() == "active" else False,
        id
    )


class TableObject:
    # same as inventory object, but retirementdate and status are omitted
    def __init__(
        self,
        assettype: str,
        manufacturer: str,
        serial: str,
        model: str,
        cost: float,
        assignedto: str,
        assetlocation: str,
        assetcategory: str,
        deploymentdate: datetime.date,
        replacementdate: datetime.date,
        notes: str,
        uniqueid: str,  # not displayed, kept as hidden column
    ):
        self.assettype = assettype
        self.manufacturer = manufacturer
        self.serial = serial
        self.model = model
        self.cost = cost
        self.assignedto = assignedto
        self.assetlocation = assetlocation
        self.assetcategory = assetcategory
        self.deploymentdate = deploymentdate
        self.replacementdate = replacementdate
        self.notes = notes
        self.uniqueid = uniqueid

    def __iter__(self):
        yield self.assettype
        yield self.manufacturer
        yield self.serial
        yield self.model
        yield self.cost
        yield self.assignedto
        yield self.assetlocation
        yield self.assetcategory
        yield self.deploymentdate
        yield self.replacementdate
        yield self.notes
        yield self.uniqueid

    def __len__(self):
        return 13

    def __str__(self):
        return f"Inventory_Object: {self.serial}"

    def __repr__(self):
        return f"Inventory_Object: {self.serial}"
