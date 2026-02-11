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
