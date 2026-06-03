from util.data_types import InventoryObject, ExtraObject


def new_entry(conn, insert: InventoryObject):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO main (assettype, manufacturer, serial, model, cost, assignedto, name, assetlocation, assetcategory, deploymentdate, replacementdate, retirementdate, notes, status, uniqueid, is_local, loandate, returndate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
         (insert.assettype, insert.manufacturer, insert.serial, insert.model, insert.cost, insert.assignedto, insert.name, insert.assetlocation, insert.assetcategory, insert.deploymentdate, insert.replacementdate, insert.retirementdate, insert.notes, insert.status, insert.uniqueid, insert.is_local, insert.loandate, insert.returndate))
    conn.commit()

def new_extra(conn, obj: ExtraObject) -> None:
    cur = conn.cursor()
    cur.execute("insert into extras values (%s, %s, %s, %s, %s, %s, %s);", (obj.item, obj.manufacturer, obj.count, obj.low_amount, obj.reserved, obj.notes, obj.uniqueid))
    conn.commit()

def bulk_insert(conn, list_of_objs: list[InventoryObject]):
    cur = conn.cursor()
    for obj in list_of_objs:
        cur.execute(
            "INSERT INTO main (assettype, manufacturer, serial, model, cost, assignedto, name, assetlocation, assetcategory, deploymentdate, replacementdate, retirementdate, notes, status, uniqueid, is_local, loandate, returndate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
             (obj.assettype, obj.manufacturer, obj.serial, obj.model, obj.cost, obj.assignedto, obj.name, obj.assetlocation, obj.assetcategory, obj.deploymentdate, obj.replacementdate, obj.retirementdate, obj.notes, obj.status, obj.uniqueid, obj.is_local, obj.loandate, obj.returndate))
    conn.commit()
