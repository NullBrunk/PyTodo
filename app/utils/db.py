import sqlite3

class Db:

    """
    Class pour simplifier la connection a la database et simplifier
    les intéraction avec elle

    
    CREATE TABLE py(
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `task` TEXT NOT NULL,
        `done` BOOLEAN
    ); 
    
    """

    def __init__(self):
        self.connection = sqlite3.connect("db/db.sqlite")
        self.cursor = self.connection.cursor()

    def list(self):
        res = self.cursor.execute("SELECT * FROM py")
        return res.fetchall()
    
    def add(self, task):
        
        self.cursor.execute("INSERT INTO py(`id`, `task`, `done`) VALUES(NULL, ?, ?)", (task, 0))
        self.connection.commit()




if __name__ == "__main__":
    print("This is part of the TODO List app and is a module used by the main.py file.")
