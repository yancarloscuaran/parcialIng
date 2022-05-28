#Academicspaces
from unicodedata import category
from src.config.db import DB
class categoryModel():
    def listCategories(self, period):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM categories WHERE period_id = ?',(period,))
        arrCategories = cursor.fetchall()
        cursor.close()
        return arrCategories
    
    
    def createCategories(self, data):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO categories (period_id,name,barcode) VALUES(?,?,?)',(data['period_id'], data['name'], data['barcode'],))
        cursor.close()
    
    def findCategories(self, idCategories):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM categories WHERE id = ?',(idCategories,))
        category = cursor.fetchone()
        cursor.close()
        return category

    def editCategories(self, data):
        cursor = DB.cursor()
        cursor.execute("UPDATE categories SET period_id = ?, name = ?, barcode = ? WHERE id = ?",(data['period_id'], data['name'], data['barcode'],data['id'],))
        cursor.close()
    
    def removeCategories(self,idCategory):
        cursor = DB.cursor()
        cursor.execute('DELETE FROM categories WHERE id = ?',(idCategory,))
        cursor.close()