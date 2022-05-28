from src.config.db import DB
class supplierModel():
    def listSuppliers(self, period):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM suppliers WHERE period_id = ?',(period,))
        arrSuppliers = cursor.fetchall()
        cursor.close()
        return arrSuppliers
    
    def findSuppliers(self, idSupplier):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM suppliers WHERE id = ?',(idSupplier,))
        supplier = cursor.fetchone()
        cursor.close()
        return supplier
    
    def createSuppliers(self,data):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO suppliers(name,contact,email,period_id) VALUES (?,?,?,?)',
        (data['name'], data['contact'], data['email'], data['period_id'],))
        cursor.close()

    def removeSuppliers(self,idSupplier):
        cursor = DB.cursor()
        cursor.execute('DELETE FROM suppliers WHERE id = ?',(idSupplier,))
        cursor.close()
    
    def editSuppliers(self,data):
        cursor = DB.cursor()
        cursor.execute('UPDATE suppliers SET name = ?, contact = ?, email = ?, period_id = ? WHERE id = ?',
        (data['name'], data['contact'], data['email'], data['period_id'], data['id'],))
        cursor.close()