from app import app,db
from flask import render_template,flash, redirect, url_for, request
from flask_login import current_user, login_user,logout_user,login_required
from werkzeug.urls import url_parse
from datetime import datetime
from app.addEarnType import bp
from app.models.Eartype_model import EarType
from flask_login import login_user,logout_user,current_user
from forms import EntryEarnTypeForm,EditEarnTypeForm



#This deocrator function will ensure that if page is served it must have authenticated users
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.ladate = datetime.utcnow()
        db.session.commit()

#This function will insert Earning Types into DB
@bp.route('/addEarnType/addEarnType',methods =['GET','POST'])
@login_required
def addEarnType():
    form =EntryEarnTypeForm()
    if form.validate_on_submit():
        eartype = EarType(u_id=current_user.id,EarType_name = form.Earn_Type.data)
        db.session.add(eartype)
        db.session.commit()
        flash("Earning Type is saved")
        return redirect(url_for('addEarnType.ListEarningType'))
    return render_template('addEarn/earn_typeAdd.html', title='Add Earning Type', form=form)


#This function will list Earnings Types in DB
@bp.route('/addEarnType/ListEarnType',methods =['GET','POST'])
@login_required
def ListEarningType():
    EarTypes = EarType.query.filter_by(u_id=current_user.id).all()
    return render_template('addEarn/earn_typeList.html', vieweartype=EarTypes)


#This function will Edit Earning types in DB
@bp.route('/addEarnType/EditEarnType',methods=['GET','POST'])
@login_required
def EditEarningTypes():
        earnid = request.args.get("earn_id")
        EarnType = EarType.query.get_or_404(earnid)
        form = EditEarnTypeForm()
        meth = request.method
        if form.validate_on_submit():
            EarnType.EarType_name = form.Earn_Type.data
            db.session.commit()
            flash('Your changes have been saved.')
            return redirect(url_for('addEarnType.ListEarningType'))
        elif request.method == 'GET':
            form.Earn_Type.data =EarnType.EarType_name
        return render_template('addEarn/earntype_edit.html', form=form,Ear=EarnType)


#This function will /Delete Earning Types in DB.

@bp.route('/addEarnType/DeleteEarnType',methods=['GET','POST'])
@login_required
def DeleteEarnType():
    earntypeoid = request.args.get("earn_id")
    delear = EarType.query.filter_by(id=earntypeoid).first()
    try:
        db.session.delete(delear)
        db.session.commit()
        flash("Earning Type Deleted")
        return redirect(url_for('addEarnType.ListEarningType'))
    except Exception as e:
        flash('There was Exception Earning Type cannot be delete it may some records in tables.')
        return redirect(url_for('addEarnType.ListEarningType'))