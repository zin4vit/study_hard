from flask import Flask, redirect, url_for, request
from application.config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.menu import MenuLink
from flask_migrate import Migrate
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


from application.blueprints.auth import auth
from application.blueprints.learning import learning
app.register_blueprint(auth)
app.register_blueprint(learning, url_prefix='/learning')



import application.views
from application.models import *


class HomeAdminView(AdminIndexView):
    def is_accessible(self):        
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next= request.url))
    

admin = Admin(app, 'STUDY_HARD', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(ModelView(Level, db.session))
admin.add_view(ModelView(Theme, db.session))
admin.add_view(ModelView(Quantity, db.session))
admin.add_view(ModelView(Formula, db.session))
admin.add_link(MenuLink(name='Logout', url='/logout'))


