from app import app, db
from flask import render_template, flash, redirect, url_for, request, send_file
from app.shares.forms import SharesEntryForm, SharesEditForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from datetime import datetime
from ..models.Share_model import Shares
from ..models.Person_model import Persons
from app.shares import bp
from base64 import b64encode
from io import BytesIO


# This deocrator function will ensure that if page is served it must have authenticated users

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.ladate = datetime.utcnow()
        db.session.commit()


@bp.route('/shares/share_add', methods=['GET', 'POST'])
@login_required
def share_add():
    form = SharesEntryForm()
    person = Persons.query.filter_by(u_id=current_user.id)
    person_list = [(i.id, i.per_name) for i in person]
    form.Share_per_name.choices = person_list
    meth = request.method
    if form.validate_on_submit():
        # file_upld = request.files()
        per_id = Persons.query.filter_by(u_id=current_user.id, id=form.Share_per_name.data).all()
        if form.Share_img.data is None:
            SharesRow = Shares(per_id=per_id[0].id, U_id=current_user.id,
                               Share_per_name=dict(form.Share_per_name.choices).get(form.Share_per_name.data),
                               Share_tick_name=form.Share_tick_name.data, Share_Count=form.Share_Count.data,
                               Share_tran_type=form.Share_tran_type.data,
                               Share_pershare_amt=form.Share_pershare_amt.data,
                               Share_inv_sell_date=form.Share_SellBuy_date.data, Share_comm=form.Share_comm.data)
        else:
            SharesRow = Shares(per_id=per_id[0].id, U_id=current_user.id,
                               Share_per_name=dict(form.Share_per_name.choices).get(form.Share_per_name.data),
                               Share_tick_name=form.Share_tick_name.data, Share_Count=form.Share_Count.data,
                               Share_tran_type=form.Share_tran_type.data,
                               Share_pershare_amt=form.Share_pershare_amt.data,
                               Share_inv_sell_date=form.Share_SellBuy_date.data, Share_img=form.Share_img.data.read(),
                               Share_FileName=form.Share_img.data.filename, Share_comm=form.Share_comm.data)

        db.session.add(SharesRow)
        db.session.commit()
        flash("Shares Entry and file has been Saved Fine")
        return redirect(url_for('shares.share_list'))
    return render_template('share/share_add.html', title='Add Expense', form=form)


@bp.route('/shares/share_list', methods=['GET', 'POST'])
@login_required
def share_list():
    page = request.args.get('page', 1, type=int)
    shareslist = Shares.query.filter_by(U_id=current_user.id).order_by(Shares.Share_inv_sell_date.desc()).paginate(page,app.config['RECORDS_PER_PAGE'], False)
    next_url = url_for('shares.list_expenses', page=shareslist.next_num) if shareslist.has_next else None
    prev_url = url_for('shares.list_expenses', page=shareslist.prev_num) if shareslist.has_prev else None
    return render_template('share/share_list.html', viewshare=shareslist.items, next_url=next_url, prev_url=prev_url)


@bp.route('/shares/download<int:id>', methods=['GET'])
@login_required
def share_download(id):
    perid = request.args.get("perID")
    share = Shares.query.filter_by(per_id=perid, U_id=current_user.id, id=id).all()
    filebuff = share[0].Share_img
    filename = share[0].Share_FileName
    return send_file(BytesIO(filebuff), attachment_filename=filename)


@bp.route('/shares/edit_share', methods=['GET', 'POST'])
@login_required
def edit_share():
    shareID = request.args.get("share_id")
    shares = Shares.query.filter_by(id=shareID, U_id=current_user.id).all()
    form = SharesEditForm()
    meth = request.method
    if request.method == 'POST':
        # THis code will load the dropdown box.
        person = Persons.query.filter_by(u_id=current_user.id)
        person_list = [(i.id, i.per_name) for i in person]
        form.Share_per_name.choices = person_list
        # This code will load form
        shares[0].Share_per_name = dict(form.Share_per_name.choices).get(form.Share_per_name.data),

        shares[0].Share_tick_name = form.Share_tick_name.data
        shares[0].Share_Count = form.Share_Count.data
        shares[0].Share_tran_type = form.Share_tran_type.data
        shares[0].Share_pershare_amt = form.Share_pershare_amt.data
        shares[0].Share_inv_sell_date = form.Share_SellBuy_date.data
        shares[0].Share_comm = form.Share_comm.data

        if form.Share_img.data is None:
            shares[0].Share_FileName = form.Share_img.data.filename,
        else:
            shares[0].Share_img = form.Share_img.data.read()
            shares[0].Share_FileName = form.Share_img.data.filename
        shares[0].Share_comm = form.Share_comm.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('shares.share_list'))

    elif request.method == 'GET':
        # THis code will load the dropdown box.
        person = Persons.query.filter_by(u_id=current_user.id)
        person_list = [(i.id, i.per_name) for i in person]
        form.Share_per_name.choices = person_list
        # This where edit form take place.
        Perid = Persons.query.filter_by(per_name=shares[0].Share_per_name).all()
        form.Share_per_name.data = int(Perid[0].id)
        form.Share_tick_name.data = shares[0].Share_tick_name
        form.Share_Count.data = shares[0].Share_Count
        form.Share_tran_type.data = shares[0].Share_tran_type
        form.Share_pershare_amt.data = shares[0].Share_pershare_amt
        form.Share_SellBuy_date.data = shares[0].Share_inv_sell_date
        form.Share_FileName.data = shares[0].Share_FileName
        form.Share_comm.data = shares[0].Share_comm
    return render_template('share/share_edit.html', form=form, share=shares)


@bp.route('/shares/DeleteShare', methods=['GET', 'POST'])
@login_required
def DeleteShare():
    share_id = request.args.get("DelShare_id")
    delshare = Shares.query.filter_by(id=share_id, U_id=current_user.id).first()
    try:
        db.session.delete(delshare)
        db.session.commit()
        flash("Share Record is Deleted")
        return redirect(url_for('shares.share_list'))
    except Exception as StandardError:
        flash('There was Exception Shares cannot be delete he/she may some records in tables.')
        return redirect(url_for('shares.share_list'))
