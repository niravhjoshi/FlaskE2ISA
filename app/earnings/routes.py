from app import app,db
from flask import render_template,flash, redirect, url_for, request
from app.earnings.forms import EarningEntryForm
from flask_login import current_user, login_user,logout_user,login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from datetime import datetime
from ..models.Earning_model import Earnings
from ..models.Person_model import Persons
from ..models.Eartype_model import EarType
from app.earnings import bp

#This deocrator function will ensure that if page is served it must have authenticated users
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.ladate = datetime.utcnow()
        db.session.commit()




@bp.route('/earnings/add_earn', methods=['GET', 'POST'])
@login_required
def earn_add():

    form = EarningEntryForm()
    meth = request.method
    if form.validate_on_submit():
        #file_upld = request.files()
        earningRow = Earnings(Per_id=current_user.id,Ear_per_name=str(form.Ear_per_name.data),
                              Ear_type_name=str(form.Ear_type_name.data),Ear_amt=form.Ear_amt.data,
                              Ear_date=form.Ear_date.data,Ear_FileName=form.Ear_img.data.filename,
                              Ear_img=form.Ear_img.data.read(),Ear_comm=form.Ear_comm.data)
        db.session.add(earningRow)
        db.session.commit()
        flash("Earning Entry and file has been Saved Fine")
        return render_template('earning/earn_add.html',form=form)

    return render_template('earning/earn_add.html', title='Add Earning', form=form)