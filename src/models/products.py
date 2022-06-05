from itertools import product
from src.config.db import DB
class productModel():
    def listProducts(self, idPeriod):
        cursor = DB.cursor()
        cursor.execute('SELECT products.id, categories.name, suppliers.name, products.name, products.description, products.value, products.date_admission, products.due_date FROM products INNER JOIN categories ON products.category_id = categories.id INNER JOIN suppliers ON products.supplier_id = suppliers.id INNER JOIN periods ON products.period_id = periods.id WHERE products.period_id = ?',(idPeriod,))
        arrProducts = cursor.fetchall()
        cursor.close()
        return arrProducts
    
    def findProduct(self, idProduct):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM products WHERE id = ?',(idProduct,))
        product = cursor.fetchone()
        cursor.close()
        return product
    
    def createProduct(self,data):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO products(category_id,supplier_id,name,description,value,date_admission,due_date,period_id) VALUES (?,?,?,?,?,?,?,?)',
        (data['category_id'], data['supplier_id'],data['name'], data['description'], data['value'],data['date_admission'],data['due_date'],data['period_id'],))
        cursor.close()

    def removeProduct(self,idProduct):
        cursor = DB.cursor()
        cursor.execute('DELETE FROM products WHERE id = ?',(idProduct,))
        cursor.close()
    
    def editProduct(self,data):
        cursor = DB.cursor()
        cursor.execute('UPDATE products SET category_id = ?, supplier_id = ?, name = ?, description = ?, value = ?, date_admission = ?, due_date = ?, period_id = ? WHERE id = ?',
        (data['category_id'], data['supplier_id'],data['name'], data['description'], data['value'],data['date_admission'],data['due_date'],data['period_id'], data['id']))
        cursor.close()