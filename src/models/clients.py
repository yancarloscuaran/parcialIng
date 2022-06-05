from src.config.db import DB
class clientModel():
    def listClients(self, period):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM clients WHERE period_id = ?',(period,))
        arrClients = cursor.fetchall()
        cursor.close()
        return arrClients
    
    def findClients(self, idClient):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM clients WHERE id = ?',(idClient,))
        client = cursor.fetchone()
        cursor.close()
        return client
    
    def createClients(self,data):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO clients(identification,name,contact,period_id) VALUES (?,?,?,?)',
        (data['identification'], data['name'], data['contact'], data['period_id'],))
        cursor.close()

    def removeClients(self,idClient):
        cursor = DB.cursor()
        cursor.execute('DELETE FROM clients WHERE id = ?',(idClient,))
        cursor.close()
    
    def editClients(self,data):
        cursor = DB.cursor()
        cursor.execute('UPDATE clients SET identification = ?, name = ?, contact = ?, period_id = ? WHERE id = ?',
        (data['identification'], data['name'], data['contact'], data['period_id'], data['id'],))
        cursor.close()