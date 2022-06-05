from flask import render_template, request, redirect, url_for, flash
from src import app
from src.controllers import categories
import src.controllers.period as Global
from src.models.products import productModel
from src.models.periods import periodsModel
from src.models.clients import clientModel
from src.models.cashiers import cashierModel
from src.models.sales import saleModel
CLIENTMODEL = clientModel()
SALEMODEL = saleModel()
CASHIERMODEL = cashierModel()
PRODUCTMODEL = productModel()
PERIODMODEL = periodsModel()
@app.route('/sales', methods=['GET','POST'])
def indexSales():
    if request.method == 'GET':
        if not 'period' in Global.session:
            Global.session['period'] = 1
        return render_template('sales/indexSales.html', periods = PERIODMODEL.listPeriods(), sales = SALEMODEL.listSales(Global.session['period']), pd = int(Global.session['period']))
    Global.session['period'] = request.form.get('period')
    return redirect(url_for('indexSales'))
    

@app.route('/Create/sales', methods=['GET','POST'])
def createSales():
    if request.method == 'GET':
        if not 'period' in Global.session:
            Global.session['period'] = 1
        return render_template('sales/createSales.html', periods = PERIODMODEL.listPeriods(), cashiers = CASHIERMODEL.listCashiers(Global.session['period']), clients = CLIENTMODEL.listClients(Global.session['period']), products = PRODUCTMODEL.listProducts(Global.session['period']) ,pt = int(Global.session['period']))
    data = {
        'cashier_id' : request.form.get('cashier_id'),
        'client_id' : request.form.get('client_id'),
        'product_id' : request.form.get('product_id'),
        'amount' : request.form.get('amount'),
        'value' : request.form.get('value'),
        'purchase_date' : request.form.get('purchase_date'),
        'period_id' : Global.session['period']
    }
    SALEMODEL.createSales(data)
    return redirect(url_for('indexSales'))

@app.route('/Edit/sales/<idSale>', methods=['GET','POST'])
def editSales(idSale):
    if request.method == 'GET': 
        return render_template('sales/editSales.html', sale = SALEMODEL.findSales(idSale), periods = PERIODMODEL.listPeriods())
    data = {
        'cashier_id' : request.form.get('cashier_id'),
        'client_id' : request.form.get('client_id'),
        'product_id' : request.form.get('product_id'),
        'amount' : request.form.get('amount'),
        'value' : request.form.get('value'),
        'purchase_date' : request.form.get('purchase_date'),
        'period_id' : Global.session['period'],
        'id': idSale
    }
    SALEMODEL.editSales(data)
    return redirect(url_for('indexSales'))

@app.route('/Imprimir/sales/<idSale>', methods=['GET','POST'])
def imprimirSales(idSale):
    if request.method == 'GET': 
        return render_template('sales/imprimirSales.html', sale = SALEMODEL.imprimirSales(idSale), periods = PERIODMODEL.listPeriods())
    return redirect(url_for('indexSales'))

@app.route('/Remove/sales/<idSale>')
def removeSales(idSale):
    SALEMODEL.removeSales(idSale)
    return redirect(url_for('indexSales'))

