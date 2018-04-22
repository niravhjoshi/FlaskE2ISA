from app import app,db
from flask import render_template,flash, redirect, url_for, request
from app.earnings.forms import EarningEntryForm
from flask_login import current_user, login_user,logout_user,login_required
from werkzeug.urls import url_parse
from datetime import datetime
from ..models.Person_model import Persons
from ..models.Eartype_model import EarType
from app.earnings import bp





@bp.route('/earnings/add_earn', methods=['GET', 'POST'])
@login_required
def earn_add():
    form = EarningEntryForm()
    form.Ear_per_name.choices = [(row.id,row.per_name) for row in Persons.query.all()]
    form .Ear_type_name.choices = [(row.id,row.EarType_name) for row in EarType.query.all()]
    return render_template('earning/earn_add.html',form=form)