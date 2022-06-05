from itertools import product
from flask import render_template, request, redirect, url_for, flash
from src import app
from src.controllers import categories
import src.controllers.period as Global
from src.models.products import productModel
from src.models.periods import periodsModel
from src.models.categories import categoryModel
from src.models.suppliers import supplierModel
SUPPLIERMODEL = supplierModel()
CATEGORYS = categoryModel()
PRODUCTMODEL = productModel()
PERIODMODEL = periodsModel()
@app.route('/products', methods=['GET','POST'])
def indexProducts():
    if request.method == 'GET':
        if not 'period' in Global.session:
            Global.session['period'] = 1
        return render_template('products/indexProducts.html', periods = PERIODMODEL.listPeriods(), products=PRODUCTMODEL.listProducts(Global.session['period']), pd = int(Global.session['period']))
    Global.session['period'] = request.form.get('period')
    return redirect(url_for('indexProducts'))
    

@app.route('/Create/products', methods=['GET','POST'])
def createProducts():
    if request.method == 'GET':
        if not 'period' in Global.session:
            Global.session['period']=1
        return render_template('products/createProducts.html', periods = PERIODMODEL.listPeriods(), categories = CATEGORYS.listCategories(Global.session['period']), suppliers = SUPPLIERMODEL.listSuppliers(Global.session['period']) ,pt = int(Global.session['period']))
        # return render_template('products/createProducts.html')
    data = {
        'category_id' : request.form.get('category_id'),
        'supplier_id' : request.form.get('supplier_id'),
        'name' : request.form.get('name'),
        'description' : request.form.get('description'),
        'value' : request.form.get('value'),
        'date_admission' : request.form.get('date_admission'),
        'due_date' : request.form.get('due_date'),
        'period_id' : Global.session['period']
    }
    PRODUCTMODEL.createProduct(data)
    return redirect(url_for('indexProducts'))

@app.route('/Edit/products/<idProduct>', methods=['GET','POST'])
def editProducts(idProduct):
    if request.method == 'GET': 
        return render_template('products/editProducts.html', product = PRODUCTMODEL.findProduct(idProduct), periods = PERIODMODEL.listPeriods(), categories = CATEGORYS.listCategories(Global.session['period']), pt = int(Global.session['period']))
    data = {
        'category_id' : request.form.get('category_id'),
        'supplier_id' : request.form.get('supplier_id'),
        'name' : request.form.get('name'),
        'description' : request.form.get('description'),
        'value' : request.form.get('value'),
        'date_admission' : request.form.get('date_admission'),
        'due_date' : request.form.get('due_date'),
        'period_id' : Global.session['period'],
        'id': idProduct
    }
    PRODUCTMODEL.editProduct(data)
    return redirect(url_for('indexProducts'))
    

@app.route('/Remove/products/<idProduct>')
def removeProducts(idProduct):
    PRODUCTMODEL.removeProduct(idProduct)
    return redirect(url_for('indexProducts'))



