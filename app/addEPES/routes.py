from app import app,db
from flask import render_template,flash, redirect, url_for, request
from app.earnings.forms import EarningEntryForm
from flask_login import current_user, login_user,logout_user,login_required
from werkzeug.urls import url_parse
from datetime import datetime
from app.addEPES import bp
from app.tables.personTable import PersonResults
from app.models.Person_model import Persons
from flask_login import login_user,logout_user,current_user
from forms import PersonsAddEntryForm,PersonEditForm
import dateutil.parser

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
    form =PersonsAddEntryForm()
    if form.validate_on_submit():
        person = Persons(u_id=current_user.id,per_name = form.Person_Name.data,per_bdate=form.Per_Bdate.data,per_sex=form.Per_Sex.data)
        db.session.add(person)
        db.session.commit()
        flash("Person Name is saved")
        return redirect(url_for('addEPES.ListPersons'))
    return render_template('persons/person_Add.html', title='Add Person', form=form)


#This function will  show currently added person into DB it can show you grid to edit it.
@bp.route('/addEPES/ListPersons',methods =['GET','POST'])
@login_required
def ListPersons():
    persons = Persons.query.filter_by(u_id=current_user.id).all()
    return render_template('persons/person_addView.html', viewper=persons)


@bp.route('/addEPES/EditPersons',methods=['GET','POST'])
@login_required
def EditPersonsNames():
        personid = request.args.get("person_id")
        person = Persons.query.get_or_404(personid)
        form = PersonEditForm()
        meth = request.method
        if form.validate_on_submit():
            person.per_name = form.Person_Name.data
            person.per_sex = form.Per_Sex.data
            person.per_bdate = form.Per_Bdate.data
            db.session.commit()
            flash('Your changes have been saved.')
            return redirect(url_for('addEPES.ListPersons'))
        elif request.method == 'GET':
            form.Person_Name.data =person.per_name
            form.Per_Sex.data =person.per_sex
            form.Per_Bdate.data =person.per_bdate
        return render_template('persons/Person_edit.html', form=form,per=person)




@bp.route('/addEPES/DeletePerson',methods=['GET','POST'])
@login_required
def DeletePersonNames():
    personid = request.args.get("person_id")
    delper=Persons.query.filter_by(id=personid).first()
    try:
        db.session.delete(delper)
        db.session.commit()
        flash("Person Deleted")
        return redirect(url_for('addEPES.ListPersons'))
    except Exception as e:
        flash('There was Exception Person cannot be delete he/she may some records in tables.')
        return redirect(url_for('addEPES.ListPersons'))
