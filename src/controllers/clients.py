from flask import render_template, request, redirect, url_for, flash
from src import app
import src.controllers.period as Global
from src.models.periods import periodsModel
from src.models.clients import clientModel
CLIENTMODEL = clientModel()
PERIODMODEL = periodsModel()
@app.route('/clients', methods=['GET','POST'])
def indexClients():
    if request.method == 'GET':
        return render_template('clients_/indexClients.html', periods = PERIODMODEL.listPeriods(), clients= CLIENTMODEL.listClients(Global.session['period']), pd = int(Global.session['period']) )
    Global.session['period'] = request.form.get('period')
    return redirect(url_for('indexClients'))


@app.route('/Create/clients', methods=['GET','POST'])
def createClients():
    if request.method == 'GET':
        return render_template('clients_/createClients.html')
    data = {
        'identification' : request.form.get('identification'),
        'name' : request.form.get('name'),
        'contact' : request.form.get('contact'),
        'period_id': Global.session['period']
    }
    CLIENTMODEL.createClients(data)
    return redirect(url_for('indexClients'))

@app.route('/Edit/clients/<idClient>', methods=['GET','POST'])
def editClients(idClient):
    if request.method == 'GET':
        return render_template('clients_/editClients.html', client = CLIENTMODEL.findClients(idClient))
    data = {
        'identification' : request.form.get('identification'),
        'name' : request.form.get('name'),
        'contact' : request.form.get('contact'),
        'period_id': Global.session['period'],
        'id' : idClient
    }
    CLIENTMODEL.editClients(data)
    return redirect(url_for('indexClients'))

@app.route('/Remove/clients/<idClient>')
def removeClients(idClient):
    CLIENTMODEL.removeClients(idClient)
    return redirect(url_for('indexClients'))