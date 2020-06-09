from flask_script import Manager
from flask_contents import app

from flask_contents.script.db import InitDB

if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command("init_db",InitDB())
    manager.run()
