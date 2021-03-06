from app import app, db
from flask import render_template, flash, redirect, url_for, request, send_file
from app.expenses.forms import ExpenseEntryForm, ExpenseEditForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from datetime import datetime
from ..models.Expense_model import Expenses
from ..models.Person_model import Persons
from ..models.ExpType_model import ExpType
from app.expenses import bp
from base64 import b64encode
from io import BytesIO


# This deocrator function will ensure that if page is served it must have authenticated users

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.ladate = datetime.utcnow()
        db.session.commit()


@bp.route('/expenses/exp_add', methods=['GET', 'POST'])
@login_required
def exp_add():
    form = ExpenseEntryForm()
    person = Persons.query.filter_by(u_id=current_user.id)
    exptype = ExpType.query.filter_by(u_id=current_user.id)
    exptype_list = [(j.id, j.ExpType_name) for j in exptype]
    person_list = [(i.id, i.per_name) for i in person]
    form.Exp_per_name.choices = person_list
    form.Exp_type_name.choices = exptype_list
    meth = request.method
    if form.validate_on_submit():
        # file_upld = request.files()
        per_id = Persons.query.filter_by(u_id=current_user.id, id=form.Exp_per_name.data).all()
        if form.Exp_img.data is None:

            expenseRow = Expenses(per_id=per_id[0].id, U_id=current_user.id,
                                  Exp_per_name=dict(form.Exp_per_name.choices).get(form.Exp_per_name.data),
                                  Exp_type_name=dict(form.Exp_type_name.choices).get(form.Exp_type_name.data),
                                  Exp_amt=form.Exp_amt.data,
                                  Exp_date=form.Exp_date.data, Exp_comm=form.Exp_comm.data)
        else:

            expenserow = Expenses(per_id=per_id[0].id, U_id=current_user.id,
                                  Exp_per_name=dict(form.Exp_per_name.choices).get(form.Exp_per_name.data),
                                  Exp_type_name=dict(form.Exp_type_name.choices).get(form.Exp_type_name.data),
                                  Exp_amt=form.Exp_amt.data,
                                  Exp_date=form.Exp_date.data, Exp_img=form.Exp_img.data.read(),
                                  Exp_FileName=form.Exp_img.data.filename,
                                  Exp_comm=form.Exp_comm.data)

            db.session.add(expenserow)
            db.session.commit()
            flash("Expense Entry and file has been Saved Fine")
            return redirect(url_for('expenses.list_expenses'))
        return render_template('expense/exp_add.html', title='Add Expense', form=form)

    @bp.route('/expenses/list_exp', methods=['GET', 'POST'])
    @login_required
    def list_expenses():
        page = request.args.get('page', 1, type=int)
        expenses = Expenses.query.filter_by(U_id=current_user.id).order_by(Expenses.Exp_date.desc()).paginate(page,
                                                                                                              app.config[
                                                                                                                  'RECORDS_PER_PAGE'],
                                                                                                              False)
        next_url = url_for('expenses.list_expenses', page=expenses.next_num) if expenses.has_next else None
        prev_url = url_for('expenses.list_expenses', page=expenses.prev_num) if expenses.has_prev else None
        return render_template('expense/exp_List.html', viewexp=expenses.items, next_url=next_url, prev_url=prev_url)

    @bp.route('/expenses/download<int:id>', methods=['GET'])
    @login_required
    def exp_download(id):
        perid = request.args.get("perID")
        # newearn = Earnings.query.get_or_404(perid,id)
        expenses = Expenses.query.filter_by(per_id=perid, U_id=current_user.id, id=id).all()
        filebuff = expenses[0].Exp_img
        filename = expenses[0].Exp_FileName
        return send_file(BytesIO(filebuff), attachment_filename=filename)

    @bp.route('/expenses/edit_exp', methods=['GET', 'POST'])
    @login_required
    def edit_exp():
        expID = request.args.get("exp_id")
        expenses = Expenses.query.filter_by(id=expID, U_id=current_user.id).all()
        form = ExpenseEditForm()
        meth = request.method
        if request.method == 'POST':
            # THis code will load the dropdown box.
            person = Persons.query.filter_by(u_id=current_user.id)
            exptype = ExpType.query.filter_by(u_id=current_user.id)
            exptype_list = [(j.id, j.ExpType_name) for j in exptype]
            person_list = [(i.id, i.per_name) for i in person]
            form.Exp_per_name.choices = person_list
            form.Exp_type_name.choices = exptype_list

            # This code will load form
            expenses[0].Exp_per_name = dict(form.Exp_per_name.choices).get(form.Exp_per_name.data),
            expenses[0].Exp_type_name = dict(form.Exp_type_name.choices).get(form.Exp_type_name.data),
            expenses[0].Exp_amt = form.Exp_amt.data
            expenses[0].Exp_date = form.Exp_date.data

            if form.Exp_img.data is None:
                expenses[0].Exp_FileName = form.Exp_FileName.data
            else:
                expenses[0].Exp_img = form.Exp_img.data.read()
                expenses[0].Exp_FileName = form.Exp_img.data.filename
            expenses[0].Exp_comm = form.Exp_comm.data
            # earnings[0].Ear_FileName = form.Ear_FileName.data
            db.session.commit()
            flash('Your changes have been saved.')
            return redirect(url_for('expenses.list_expenses'))

        elif request.method == 'GET':
            # THis code will load the dropdown box.
            person = Persons.query.filter_by(u_id=current_user.id)
            exptype = ExpType.query.filter_by(u_id=current_user.id)
            exptype_list = [(j.id, j.ExpType_name) for j in exptype]
            person_list = [(i.id, i.per_name) for i in person]
            form.Exp_per_name.choices = person_list
            form.Exp_type_name.choices = exptype_list

            # This where edit form take place.
            Expid = ExpType.query.filter_by(ExpType_name=expenses[0].Exp_type_name).all()
            Perid = Persons.query.filter_by(per_name=expenses[0].Exp_per_name).all()
            form.Exp_type_name.data = int(Expid[0].id)
            form.Exp_per_name.data = int(Perid[0].id)
            form.Exp_amt.data = expenses[0].Exp_amt
            form.Exp_date.data = expenses[0].Exp_date
            form.Exp_FileName.data = expenses[0].Exp_FileName
            form.Exp_comm.data = expenses[0].Exp_comm
        return render_template('expense/exp_edit.html', form=form, exp=expenses)

    @bp.route('/expenses/DeleteExp', methods=['GET', 'POST'])
    @login_required
    def DeleteExp():
        exp_id = request.args.get("Delexp_id")
        delexp = Expenses.query.filter_by(id=exp_id, U_id=current_user.id).first()
        try:
            db.session.delete(delexp)
            db.session.commit()
            flash("Expense Record is Deleted")
            return redirect(url_for('expense.list_expenses'))
        except Exception as e:
            flash('There was Exception Expense cannot be delete he/she may some records in tables.')
            return redirect(url_for('expenses.list_expenses'))
