from src.config.db import DB
class saleModel():
    def listSales(self, idPeriod):
        cursor = DB.cursor()
        cursor.execute('SELECT sales.id, cashiers.name, clients.name, products.name, sales.amount, sales.value, sales.purchase_date FROM sales INNER JOIN cashiers ON sales.cashier_id = cashiers.id INNER JOIN clients ON sales.client_id = clients.id INNER JOIN products ON sales.product_id = products.id INNER JOIN periods ON sales.period_id = periods.id WHERE sales.period_id = ?',(idPeriod,))
        arrSales = cursor.fetchall()
        cursor.close()
        return arrSales
    
    def findSales(self, idSale):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM sales WHERE id = ?',(idSale,))
        sale = cursor.fetchone()
        cursor.close()
        return sale

    def imprimirSales(self, idSale):
        cursor = DB.cursor()
        cursor.execute('SELECT sales.id, cashiers.name, clients.name, products.name, sales.amount, sales.value, sales.purchase_date FROM sales INNER JOIN cashiers ON sales.cashier_id = cashiers.id INNER JOIN clients ON sales.client_id = clients.id INNER JOIN products ON sales.product_id = products.id WHERE sales.id = ?',(idSale,))
        sale = cursor.fetchone()
        cursor.close()
        return sale
    
    def createSales(self,data):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO sales(cashier_id,client_id,product_id,amount,value,purchase_date,period_id) VALUES (?,?,?,?,?,?,?)',
        (data['cashier_id'], data['client_id'],data['product_id'], data['amount'], data['value'],data['purchase_date'],data['period_id'],))
        cursor.close()

    def removeSales(self,idSale):
        cursor = DB.cursor()
        cursor.execute('DELETE FROM sales WHERE id = ?',(idSale,))
        cursor.close()
    
    def editSales(self,data):
        cursor = DB.cursor()
        cursor.execute('UPDATE sales SET cashier_id = ?, client_id = ?, product_id = ?, amount = ?, value = ?, purchase_date = ?, period_id = ? WHERE id = ?',
        (data['cashier_id'], data['client_id'],data['product_id'], data['amount'],data['value'],data['purchase_date'],data['period_id'], data['id']))
        cursor.close()