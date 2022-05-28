from flask import render_template, request, redirect, url_for, flash
from src import app
import src.controllers.period as Global
from src.models.suppliers import supplierModel
from src.models.periods import periodsModel
SUPPLIERMODEL = supplierModel()
PERIODMODEL = periodsModel()
@app.route('/suppliers', methods=['GET','POST'])
def indexSuppliers():
    if request.method == 'GET':
        return render_template('suppliers/indexSuppliers.html', periods = PERIODMODEL.listPeriods(), suppliers = SUPPLIERMODEL.listSuppliers(Global.session['period']), pd = int(Global.session['period']) )
    Global.session['period'] = request.form.get('period')
    return redirect(url_for('indexSuppliers'))

@app.route('/Create/suppliers', methods=['GET','POST'])
def createSuppliers():
    if request.method == 'GET':
        return render_template('suppliers/createSuppliers.html')
    data = {
        'name' : request.form.get('name'),
        'contact' : request.form.get('contact'),
        'email' : request.form.get('email'),
        'period_id': Global.session['period']
    }
    SUPPLIERMODEL.createSuppliers(data)
    return redirect(url_for('indexSuppliers'))

@app.route('/Edit/suppliers/<idSupplier>', methods=['GET','POST'])
def editSuppliers(idSupplier):
    if request.method == 'GET':
        return render_template('suppliers/editSuppliers.html', supplier = SUPPLIERMODEL.findSuppliers(idSupplier))
    data = {
        'id' : idSupplier,
        'name' : request.form.get('name'),
        'contact' : request.form.get('contact'),
        'email' : request.form.get('email'),
        'period_id': Global.session['period']
    }
    SUPPLIERMODEL.editSuppliers(data)
    return redirect(url_for('indexSuppliers'))

@app.route('/Remove/suppliers/<idSupplier>')
def removeSuppliers(idSupplier):
    SUPPLIERMODEL.removeSuppliers(idSupplier)
    return redirect(url_for('indexSuppliers'))