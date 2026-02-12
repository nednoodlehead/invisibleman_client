# this will be setup on an opt-in basis. the user will choose a location to put the backups. It will be completely automatic
# we'll put it into a folder.
# the folder will contain 3 backups: Invisman_Daily_<date>.xlsx, Invisman_weekly_<date>.xlsx, Invisman_monthly_<date>.xlsx
# 1 monthly. taken on the next day of the earliest month
# the user will provide a directory for these to be backed up.
# the main concept is that these are to be backed up to a onedrive folder, and can be automatically uploaded to the cloud
from pathlib import Path
from os import remove
from datetime import datetime, timedelta
from dateutil import relativedelta
from time import sleep
from util.export import write_iter_into_csv

from PyQt5.QtCore import QThread, pyqtSignal

# all of this is required so we can send info back to the main thread depending on if a backup was taken, and to update the "last_x_backup" to the current date so it is accurate
class BackupThread(QThread):
    send_res = pyqtSignal(object)    
    def __init__(self, backup_path, conn, daily, weekly, monthly):
        super().__init__()
        self.backup_path = backup_path
        self.conn = conn
        self.daily = daily
        self.weekly = weekly
        self.monthly = monthly
    
    def run(self):
        # Execute the function and emit the result
        sleep(10)
        result = backup_invisman(self.backup_path, self.conn, self.daily, self.weekly, self.monthly)
        self.send_res.emit(result)

def backup_invisman(dir, conn, daily_backup, weekly_backup, monthly_backup):
    # we'll iter over the contents in the target directory. the concept is for the directory to be only invisman backups, but users probably don't care
    # we're going to sleep for a minute so the startup stuff isn't affected by this...
    # sleep(60)
    # we will attempt each type of backup. if one succeds, we will not do another (what would be the point?)
    # starting with the monthly -> weekly -> daily
    today = datetime.today().date()
    monthly = datetime.strptime(monthly_backup, "%Y-%m-%d")
    weekly = datetime.strptime(weekly_backup, "%Y-%m-%d")
    dailies = [datetime.strptime(i, "%Y-%m-%d").date() for i in daily_backup]
    when_backedup = None # the receiving functions will check if none, otherwise set config[when_backedup] = datetime.today()
    if today in dailies:
        return
    delete_oldest_daily(dir, min(dailies))
    try:
        if monthly < (today - timedelta(weeks=4)): # 4 weeks is a month idc
            make_and_write_backup(f"{dir}./invisman-monthly.csv", conn)
            when_backedup = "m"
        elif weekly < (today - timedelta(days=7)):
            make_and_write_backup(f"{dir}./invisman-weekly.csv", conn)
            when_backedup = "w"
        else:
            # sort dailies by time, so we are looking at the oldest
            oldest = dailies[0] # makes the first iteration redundant i guess. seems silly to add a skip function for the first one
            for day in dailies:
                if day < oldest:
                    oldest = day
                if day == today:
                    break
            if today not in dailies:
                time_stamp = str(datetime.now()).replace(":", "-")[:19]  # stolen right from ui_functions
                make_and_write_backup(f"{dir}./invisman-daily-{time_stamp}.csv", conn)
                when_backedup = str(oldest)
    except PermissionError:
        print(f"ERROR WRITING TO DIRECTORY (NO PERMS): {dir} ")
    return when_backedup
    

def make_and_write_backup(file_name, conn):
    # silly way to adapt to all future column changes
    cur = conn.cursor()
    cur.execute("select column_name from information_schema.columns where table_schema = 'public' and table_name = 'main';")
    columns = [x[0] for x in cur.fetchall()]
    cur.execute("select * from main")
    data = cur.fetchall()
    write_iter_into_csv(columns, data, file_name)
    
def delete_oldest_daily(dir, death_date):
    print("lowest?", death_date)
    # finds the files that matches "invisman-daily" and will choose the oldest, then remove it.
    target = f'invisman-daily-{death_date}'
    for file in Path(dir).iterdir():
        print(file.name[:25] == target, file.name[:25], target)
        if file.name[:25] == target:
            print("removing!")
            remove(file)
