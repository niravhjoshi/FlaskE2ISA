from app import app,db
from flask import render_template,flash, redirect, url_for, request
from flask_login import current_user, login_user,logout_user,login_required
from werkzeug.urls import url_parse
from datetime import datetime
from app.addInvType import bp
from app.models.Investtype_model import InvType
from flask_login import login_user,logout_user,current_user
from forms import EntryInvTypeForm,EditInvTypeForm


#This deocrator function will ensure that if page is served it must have authenticated users
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.ladate = datetime.utcnow()
        db.session.commit()


#This function will insert Expense Types into DB
@bp.route('/addInvType/addInvType',methods =['GET','POST'])
@login_required
def addInvType():
    form =EntryInvTypeForm()
    if form.validate_on_submit():
        invType = InvType(u_id=current_user.id,InvType_name = form.Inv_Type.data)
        db.session.add(invType)
        db.session.commit()
        flash("Investment  Type is saved")
        return redirect(url_for('addInvType.ListInvTypes'))
    return render_template('addInvest/Inv_typeAdd.html', title='Add Investment Type', form=form)


#This function will list Expense Types in DB
@bp.route('/addInvType/ListInvTypes',methods =['GET','POST'])
@login_required
def ListInvTypes():
    InvTypes = InvType.query.filter_by(u_id=current_user.id).all()
    return render_template('addInvest/Inv_typeList.html', viewinvtype=InvTypes)


#This function will Edit Earning types in DB
@bp.route('/addInvType/EditInvTypes',methods=['GET','POST'])
@login_required
def EditInvTypes():
        invid = request.args.get("inv_id")
        invType = InvType.query.get_or_404(invid)
        form = EditInvTypeForm()
        meth = request.method
        if form.validate_on_submit():
            invType.InvType_name = form.Inv_Type.data
            db.session.commit()
            flash('Your changes have been saved.')
            return redirect(url_for('addInvType.ListInvTypes'))
        elif request.method == 'GET':
            form.Inv_Type.data =invType.InvType_name
        return render_template('addInvest/Inv_edit.html', form=form,Inv=invType)


#This function will /Delete Earning Types in DB.

@bp.route('/addInvType/DeleteInvType',methods=['GET','POST'])
@login_required
def DeleteInvType():
    invid = request.args.get("inv_id")
    delinv = InvType.query.filter_by(id=invid).first()
    try:
        db.session.delete(delinv)
        db.session.commit()
        flash("Investment Type Deleted")
        return redirect(url_for('addInvType.ListInvTypes'))
    except Exception as e:
        flash('There was Exception Investment Type cannot be delete it may some records in tables.')
        return redirect(url_for('addInvType.ListInvTypes'))
