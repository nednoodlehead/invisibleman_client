from gui.start import main
from db.create_db import create_db
import os
# asset management tracker!
# built with PyQt5 (<3 Qtdesigner) & Sqlite
# this is where the program begins
if not os.path.exists("main.db"):
    create_db()

main()
