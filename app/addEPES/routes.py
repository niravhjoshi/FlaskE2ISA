from app import app,db
from flask import render_template,flash, redirect, url_for, request
from app.earnings.forms import EarningEntryForm
from flask_login import current_user, login_user,logout_user,login_required
from werkzeug.urls import url_parse
from datetime import datetime
from app.addEPES import bp
from app.tables.personTable import PersonResults
from app.models.Person_model import Persons

#This deocrator function will ensure that if page is served it must have authenticated users
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.ladate = datetime.utcnow()
        db.session.commit()

#This function will add person name into DB
@bp.route('/addEPES/addPersons',methods =['GET','POST'])
@login_required
def addPersonNames():
    pass
#This function will  show currently added person into DB it can show you grid to edit it.
@bp.route('/addEPES/EditPersons',methods =['GET','POST'])
@login_required
def EditPersonsNames():
    personresults=[]
    personresults = Persons.query.all()
    if not personresults:
        flash("We are sorry there are no persons in table please add it.")
        return redirect('/')
    else:
        #display results in table
        table = PersonResults(personresults)
        table.border = True
        return render_template('persons/person_addView.html',table=table)