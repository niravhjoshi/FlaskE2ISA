from app import app, db
from flask import render_template, flash, redirect, url_for, request, send_file
from app.investments.forms import InvestEntryForm, InvestEditForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from datetime import datetime
from ..models.Investment_model import Investments
from ..models.Person_model import Persons
from ..models.Investtype_model import InvType
from app.investments import bp
from base64 import b64encode
from io import BytesIO


# This deocrator function will ensure that if page is served it must have authenticated users

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.ladate = datetime.utcnow()
        db.session.commit()


@bp.route('/investments/inv_add', methods=['GET', 'POST'])
@login_required
def invest_add():
    form = InvestEntryForm()
    person = Persons.query.filter_by(u_id=current_user.id)
    invtype = InvType.query.filter_by(u_id=current_user.id)
    invtype_list = [(j.id, j.InvType_name) for j in invtype]
    person_list = [(i.id, i.per_name) for i in person]
    form.Inv_per_name.choices = person_list
    form.Inv_type_name.choices = invtype_list
    meth = request.method
    if form.validate_on_submit():
        # file_upld = request.files()
        per_id = Persons.query.filter_by(u_id=current_user.id, id=form.Inv_per_name.data).all()
        InvestRow = Investments(per_id=per_id[0].id, U_id=current_user.id,
                                Inv_per_name=dict(form.Inv_per_name.choices).get(form.Inv_per_name.data),
                                Inv_type_name=dict(form.Inv_type_name.choices).get(form.Inv_type_name.data),
                                Inv_init_amt=form.Inv_init_amt.data, Inv_mat_amt=form.Inv_mat_amt.data,
                                Inv_ROI_PerYear=form.Inv_roiper_amt.data,
                                Inv_date=form.Inv_date.data, Inv_mat_date=form.Inv_Mat_date.data,
                                Inv_due_date=form.Inv_due_date.data,
                                Inv_Filename=form.Inv_img.data.filename,
                                Inv_img=form.Inv_img.data.read(), Inv_comm=form.Inv_comm.data)

        db.session.add(InvestRow)
        db.session.commit()
        flash("Invest Entry and file has been Saved Fine")
        return redirect(url_for('investments.invest_list'))
    return render_template('investment/inv_add.html', title='Add Expense', form=form)


@bp.route('/investments/inv_list', methods=['GET','POST'])
@login_required
def invest_list():
    investlist = Investments.query.filter_by(U_id=current_user.id).all()
    return render_template('investment/inv_list.html', viewinv=investlist)


@bp.route('/investments/download<int:id>', methods=['GET'])
@login_required
def inv_download(id):
    perid = request.args.get("perID")
    investment = Investments.query.filter_by(per_id=perid, U_id=current_user.id,id=id).all()
    filebuff = investment[0].Inv_img
    filename = investment[0].Inv_Filename
    return send_file(BytesIO(filebuff), attachment_filename=filename)


@bp.route('/investments/edit_inv', methods=['GET', 'POST'])
@login_required
def edit_inv():
    invID = request.args.get("inv_id")
    investments = Investments.query.filter_by(id=invID, U_id=current_user.id).all()
    form = InvestEditForm()
    meth = request.method
    if request.method == 'POST':
        # THis code will load the dropdown box.
        person = Persons.query.filter_by(u_id=current_user.id)
        invtype = InvType.query.filter_by(u_id=current_user.id)
        invtype_list = [(j.id, j.InvType_name) for j in invtype]
        person_list = [(i.id, i.per_name) for i in person]
        form.Inv_per_name.choices = person_list
        form.Inv_type_name.choices = invtype_list

        # This code will load form
        investments[0].Inv_per_name = dict(form.Inv_per_name.choices).get(form.Inv_per_name.data),
        investments[0].Inv_type_name = dict(form.Inv_type_name.choices).get(form.Inv_type_name.data),
        investments[0].Inv_init_amt = form.Inv_init_amt.data,
        investments[0].Inv_mat_amt = form.Inv_mat_amt.data,
        investments[0].Inv_ROI_PerYear = form.Inv_roiper_amt.data,
        investments[0].Inv_date = form.Inv_date.data,
        investments[0].Inv_mat_date = form.Inv_Mat_date.data,
        investments[0].Inv_due_date = form.Inv_due_date.data,
        investments[0].Inv_comm = form.Inv_comm.data

        if form.Inv_img.data is None:
            investments[0].Inv_Filename = form.Inv_img.data.filename,
        else:
            investments[0].Inv_img = form.Inv_img.data.read()
            investments[0].Inv_Filename = form.Inv_img.data.filename
        investments[0].Inv_comm = form.Inv_comm.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('investments.invest_list'))

    elif request.method == 'GET':
        # THis code will load the dropdown box.
        person = Persons.query.filter_by(u_id=current_user.id)
        invtype = InvType.query.filter_by(u_id=current_user.id)
        invtype_list = [(j.id, j.InvType_name) for j in invtype]
        person_list = [(i.id, i.per_name) for i in person]
        form.Inv_per_name.choices = person_list
        form.Inv_type_name.choices = invtype_list

        # This where edit form take place.
        Invid = InvType.query.filter_by(InvType_name=investments[0].Inv_type_name).all()
        Perid = Persons.query.filter_by(per_name=investments[0].Inv_per_name).all()
        form.Inv_type_name.data = int(Invid[0].id)
        form.Inv_per_name.data = int(Perid[0].id)
        form.Inv_init_amt.data = investments[0].Inv_init_amt,
        form.Inv_mat_amt.data = investments[0].Inv_mat_amt,
        form.Inv_roiper_amt.data = investments[0].Inv_ROI_PerYear,
        form.Inv_date.data = investments[0].Inv_date,
        form.Inv_Mat_date.data = investments[0].Inv_mat_date,
        form.Inv_due_date.data = investments[0].Inv_due_date,
        form.Inv_FileName.data = investments[0].Inv_Filename
        form.Inv_comm.data = investments[0].Inv_comm
    return render_template('investment/inv_edit.html', form=form, inv=investments)


@bp.route('/investments/DeleteInv', methods=['GET', 'POST'])
@login_required
def DeleteInv():
    inv_id = request.args.get("Delinv_id")
    delinv = Investments.query.filter_by(id=inv_id, U_id=current_user.id).first()
    try:
        db.session.delete(delinv)
        db.session.commit()
        flash("Investment Record is Deleted")
        return redirect(url_for('investment.invest_list'))
    except Exception as StandardError:
        flash('There was Exception Investment cannot be delete he/she may some records in tables.')
        return redirect(url_for('investment.invest_list'))
