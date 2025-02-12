from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddOwnerForm

owners_blueprints = Blueprint("owners",__name__,template_folder="templates/owners")

@owners_blueprints.route('/add',methods=['GET','POST'])
def add_owner():
    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data

        new_owner = Owner(name, pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('puppies.list_pup'))
    return render_template('add_owner.html',form=form)