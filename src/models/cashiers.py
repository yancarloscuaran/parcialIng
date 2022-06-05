from src.config.db import DB
class cashierModel():
    def listCashiers(self, period):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM cashiers WHERE period_id = ?',(period,))
        arrCashiers = cursor.fetchall()
        cursor.close()
        return arrCashiers
    
    def findCashiers(self, idCashier):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM cashiers WHERE id = ?',(idCashier,))
        client = cursor.fetchone()
        cursor.close()
        return client
    
    def createCashiers(self,data):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO cashiers(identification,name,contact,direction,arrival_time,departure_time,period_id) VALUES (?,?,?,?,?,?,?)',
        (data['identification'], data['name'], data['contact'], data['direction'], data['arrival_time'], data['departure_time'], data['period_id'],))
        cursor.close()

    def removeCashiers(self,idCashier):
        cursor = DB.cursor()
        cursor.execute('DELETE FROM cashiers WHERE id = ?',(idCashier,))
        cursor.close()
    
    def editCashiers(self,data):
        cursor = DB.cursor()
        cursor.execute('UPDATE cashiers SET identification = ?, name = ?, contact = ?, direction = ?, arrival_time = ?, departure_time = ?, period_id = ? WHERE id = ?',
        (data['identification'], data['name'], data['contact'], data['direction'], data['arrival_time'], data['departure_time'], data['period_id'], data['id'],))
        cursor.close()