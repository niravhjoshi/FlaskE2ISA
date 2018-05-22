from app import app,db
from flask import render_template,flash, redirect, url_for, request
from flask_login import current_user, login_user,logout_user,login_required
from werkzeug.urls import url_parse
from datetime import datetime
from app.addExpType import bp
from app.models.ExpType_model import ExpType
from flask_login import login_user,logout_user,current_user
from forms import EntryExpTypeForm,EditExpTypeForm


#This deocrator function will ensure that if page is served it must have authenticated users
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.ladate = datetime.utcnow()
        db.session.commit()


#This function will insert Expense Types into DB
@bp.route('/addExpType/addExpType',methods =['GET','POST'])
@login_required
def addExpType():
    form =EntryExpTypeForm()
    if form.validate_on_submit():
        exptype = ExpType(u_id=current_user.id,ExpType_name = form.Exp_Type.data)
        db.session.add(exptype)
        db.session.commit()
        flash("Expense Type is saved")
        return redirect(url_for('addExpType.ListExpTypes'))
    return render_template('addExpense/Exp_typeAdd.html', title='Add Expense Type', form=form)

#This function will list Expense Types in DB
@bp.route('/addExpType/ListExpTypes',methods =['GET','POST'])
@login_required
def ListExpTypes():
    ExpTypes = ExpType.query.filter_by(u_id=current_user.id).all()
    return render_template('addExpense/Exp_typeList.html', vieweartype=ExpTypes)


#This function will Edit Earning types in DB
@bp.route('/addExpType/EditExpType',methods=['GET','POST'])
@login_required
def EditExpTypes():
        expid = request.args.get("exp_id")
        expType = ExpType.query.get_or_404(expid)
        form = EditExpTypeForm()
        meth = request.method
        if form.validate_on_submit():
            expType.ExpType_name = form.Exp_Type.data
            db.session.commit()
            flash('Your changes have been saved.')
            return redirect(url_for('addExpType.ListExpTypes'))
        elif request.method == 'GET':
            form.Exp_Type.data =expType.ExpType_name
        return render_template('addExpense/Exp_edit.html', form=form,Exp=expType)


#This function will /Delete Earning Types in DB.

@bp.route('/addExpType/DeleteExpType',methods=['GET','POST'])
@login_required
def DeleteExpType():
    exptypeid = request.args.get("exp_id")
    delexp = ExpType.query.filter_by(id=exptypeid).first()
    try:
        db.session.delete(delexp)
        db.session.commit()
        flash("Expense Type Deleted")
        return redirect(url_for('addExpType.ListExpTypes'))
    except Exception as e:
        flash('There was Exception Expense Type cannot be delete it may some records in tables.')
        return redirect(url_for('addExpType.ListExpTypes'))
