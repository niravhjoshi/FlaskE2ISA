from app import app,db
from flask import render_template,flash, redirect, url_for, request,send_file
from app.earnings.forms import EarningEntryForm
from flask_login import current_user, login_user,logout_user,login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from datetime import datetime
from ..models.Earning_model import Earnings
from ..models.Person_model import Persons
from ..models.Eartype_model import EarType
from app.earnings import bp
from base64 import b64encode
from io import BytesIO
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
        per_id = Persons.query.filter_by(u_id=current_user.id , per_name=str(form.Ear_per_name.data)).all()
        earningRow = Earnings(Per_id=per_id[0].id,U_id=current_user.id,Ear_per_name=str(form.Ear_per_name.data),
                              Ear_type_name=str(form.Ear_type_name.data),Ear_amt=form.Ear_amt.data,
                              Ear_date=form.Ear_date.data,Ear_FileName=form.Ear_img.data.filename,
                              Ear_img=form.Ear_img.data.read(),Ear_comm=form.Ear_comm.data)
        db.session.add(earningRow)
        db.session.commit()
        flash("Earning Entry and file has been Saved Fine")
        return redirect(url_for('earnings.list_earning'))
    return render_template('earning/earn_add.html', title='Add Earning', form=form)

@bp.route('/earnings/list_earn',methods=['GET','POST'])
@login_required
def list_earning():
    earnings = Earnings.query.filter_by(U_id=current_user.id).all()
    return render_template('earning/earn_List.html', viewearn=earnings)



@bp.route('/earnings/download<int:id>',methods=['GET'])
@login_required
def earn_download(id):
    perid = request.args.get("perID")

    #newearn = Earnings.query.get_or_404(perid,id)
    earnings = Earnings.query.filter_by(Per_id=perid , U_id=current_user.id).all()
    filebuff = earnings[0].Ear_img
    filename = earnings[0].Ear_FileName
    return send_file(BytesIO(filebuff),attachment_filename=filename)

@bp.route('/earnings/edit_earn',methods=['GET','POST'])
@login_required
def edit_earn():
    pass