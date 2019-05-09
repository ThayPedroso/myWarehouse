import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("Products.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS product (id INTEGER PRIMARY KEY, description text, manufacturer text, quantity integer, code text, barCode integer)")
        self.conn.commit()

    def insert(self,description,manufacturer,quantity,code,barCode):
        self.cur.execute("INSERT INTO product VALUES (NULL,?,?,?,?,?)",(description,manufacturer,quantity,code,barCode))
        self.conn.commit() 

    def view(self):
        self.cur.execute("SELECT * FROM product")
        rows=self.cur.fetchall()   
        return rows

    def search(self, description="",manufacturer="",quantity="",code="",barCode=""):
        self.cur.execute("SELECT * FROM product WHERE description=? OR manufacturer=? OR quantity=? OR code=? OR barCode=?",(description,manufacturer,quantity,code,barCode))
        rows=self.cur.fetchall()
        return rows  

    def delete(self, id):
        self.cur.execute("DELETE FROM product WHERE id=?",(id,))
        self.conn.commit() 

    def update(self, id,description,manufacturer,quantity,code,barCode):
        self.cur.execute("UPDATE product SET description=?, manufacturer=?, quantity=?, code=?, barCode=? WHERE id=?",(description,manufacturer,quantity,code,barCode,id))
        self.conn.commit()

    def advancedSearch(self,description="",code=""):
        counterArgs = 0
        descriptionStr = description
        codeStr = code
        if description != "":
            descriptionStr = '%'+description+'%'
            counterArgs += 1
        if code != "":
            codeStr = '%'+code+'%'
            counterArgs += 1 

        if counterArgs == 0:
            self.cur.execute("SELECT * FROM product WHERE description LIKE ?",('%'))    
        if counterArgs == 1:
            self.cur.execute("SELECT * FROM product WHERE description LIKE ? OR code LIKE ?",(descriptionStr,codeStr,))
        if counterArgs == 2:
            self.cur.execute("SELECT * FROM product WHERE description LIKE ? AND code LIKE ?",(descriptionStr,codeStr,))
        rows=self.cur.fetchall()
        return rows

    def __del__ (self):
        self.conn.close()

