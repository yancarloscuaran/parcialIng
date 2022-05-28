from sre_parse import CATEGORIES
from flask import render_template, request, redirect, url_for, flash
from src import app
import src.controllers.period as Global
from src.models.categories import categoryModel
from src.models.periods import periodsModel
CATEGORYMODEL = categoryModel()
PERIODMODEL = periodsModel()
@app.route('/categories', methods=['GET','POST'])
def indexCategories():
    if request.method == 'GET':
        return render_template('categories/indexCategories.html', periods = PERIODMODEL.listPeriods(), categories= CATEGORYMODEL.listCategories(Global.session['period']), pd = int(Global.session['period']) )
    Global.session['period'] = request.form.get('period')
    return redirect(url_for('indexCategories'))


@app.route('/Create/categories', methods=['GET','POST'])
def createCategories():
    if request.method == 'GET':
        return render_template('categories/createCategories.html')
    data = {
        'name' : request.form.get('name'),
        'barcode' : request.form.get('barcode'),
        'period_id': Global.session['period']
    }
    CATEGORYMODEL.createCategories(data)
    return redirect(url_for('indexCategories'))

@app.route('/Edit/categories/<idCategory>', methods=['GET','POST'])
def editCategories(idCategory):
    if request.method == 'GET':
        return render_template('categories/editCategories.html', category = CATEGORYMODEL.findCategories(idCategory))
    data = {
        'id' : idCategory,
        'name' : request.form.get('name'),
        'barcode' : request.form.get('barcode'),
        'period_id': Global.session['period']
    }
    CATEGORYMODEL.editCategories(data)
    return redirect(url_for('indexCategories'))

@app.route('/Remove/categories/<idCategory>')
def removeCategories(idCategory):
    CATEGORYMODEL.removeCategories(idCategory)
    return redirect(url_for('indexCategories'))