from flask import render_template, request, redirect, url_for, flash
from src import app
import src.controllers.period as Global
from src.models.periods import periodsModel
from src.models.cashiers import cashierModel
CASHIERMOEL = cashierModel()
PERIODMODEL = periodsModel()
@app.route('/cashiers', methods=['GET','POST'])
def indexCashiers():
    if request.method == 'GET':
        return render_template('cashiers/indexCashiers.html', periods = PERIODMODEL.listPeriods(), cashiers= CASHIERMOEL.listCashiers(Global.session['period']), pd = int(Global.session['period']) )
    Global.session['period'] = request.form.get('period')
    return redirect(url_for('indexCashiers'))


@app.route('/Create/cashiers', methods=['GET','POST'])
def createCashiers():
    if request.method == 'GET':
        return render_template('cashiers/createCashiers.html')
    data = {
        'identification' : request.form.get('identification'),
        'name' : request.form.get('name'),
        'contact' : request.form.get('contact'),
        'direction' : request.form.get('direction'),
        'arrival_time' : request.form.get('arrival_time'),
        'departure_time' : request.form.get('departure_time'),
        'period_id': Global.session['period']
    }
    CASHIERMOEL.createCashiers(data)
    return redirect(url_for('createSales'))

@app.route('/Edit/cashiers/<idCashier>', methods=['GET','POST'])
def editCashiers(idCashier):
    if request.method == 'GET':
        return render_template('cashiers/editCashiers.html', cashier = CASHIERMOEL.findCashiers(idCashier))
    data = {
        'identification' : request.form.get('identification'),
        'name' : request.form.get('name'),
        'contact' : request.form.get('contact'),
        'direction' : request.form.get('direction'),
        'arrival_time' : request.form.get('arrival_time'),
        'departure_time' : request.form.get('departure_time'),
        'period_id': Global.session['period'],
        'id' : idCashier
    }
    CASHIERMOEL.editCashiers(data)
    return redirect(url_for('indexCashiers'))

@app.route('/Remove/cashiers/<idCashier>')
def removeCashiers(idCashier):
    CASHIERMOEL.removeCashiers(idCashier)
    return redirect(url_for('indexCashiers'))