from flask import (
    render_template,redirect,
    url_for,abort,flash,
    Blueprint
)
from flask_login import login_user, login_required, logout_user
from AY import app
from AY.models import *
from AY.forms import * 
from flask.cli import with_appcontext
import click


admin = Blueprint('admin', __name__)

# Admin Site
@admin.route('/admin', methods=['GET','POST'])
def login_admin():
    form = AdminLoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin.check_password(form.password.data):
            login_user(admin)
            return redirect(url_for('admin.index'))
        else:
            return 'Wrong Password'

    return render_template('admin/admin_login.html', form=form)


@admin.route('/logoutadmin')
@login_required
def logout_admin(admi_id):
    logout_user()
    return redirect(url_for('login'))




@admin.route('/')
def index():
    return render_template('admin/index.html')









# Flask Commands--------------------------------------------------------------------
# Creates admin user for test enviroment
@click.command(name='create_admin')
@with_appcontext
def create_admin():
    admin = Admin(
        username= 'admin',
        password = 'admin'
    )
    check = Admin.query.filter_by(username='admin').first()
    if check:
        print('Admin is already created man !\nO yeah')
    else:
        db.session.add(admin)
        db.session.commit()
        print('Admin Created!')


# Deletes or clears all records in the database, whatever
@click.command(name='hard_reset_database')
@with_appcontext
def hard_reset_database():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        db.session.execute(table.delete())

    db.session.commit()
    print('Deleted all records from database')


# Test Flask Commands
@click.command(name='test_command')
@with_appcontext
def test_command():
    print('Working Fine! Relax :)')

app.cli.add_command(create_admin)
app.cli.add_command(hard_reset_database)
app.cli.add_command(test_command)
