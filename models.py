from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import ModelView
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, current_user

db = SQLAlchemy()

# Define models
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('roles.id'))
)

class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    salt = db.Column(db.String(16), nullable=False, unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    last_ip = db.Column(db.String(45))
    language = db.Column(db.String(20))
    status = db.Column(db.Integer)
    confirmed = db.Column(db.Integer)
    date_created = db.Column(db.DateTime)
    date_updated = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)
    remember_token = db.Column(db.String(255))
    is_admin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='Admin or User?')
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.email

# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

    # can_edit = True
    edit_modal = True
    create_modal = True    
    can_export = True
    can_view_details = True
    details_modal = True

class UserView(MyModelView):
    form_columns = ['id','username','first_name','last_name']
    column_exclude_list = ['language','status','salt','password','remember_token','is_admin']
    column_labels = dict(username='login',confirmed='Enabled',last_ip='IP')

    # valori sotto da rivedere

    # column_editable_list = ['email', 'first_name', 'last_name']
    # column_searchable_list = column_editable_list
    # column_exclude_list = ['password']
    #### form_excluded_columns = column_exclude_list
    # column_details_exclude_list = column_exclude_list
    # column_filters = column_editable_list    


class Hotel(db.Model):
    __tablename__ = 'hotel'

    seq_id = db.Column(db.Integer, primary_key=True, info='id corretto e in uso')
    id = db.Column(db.String(20, 'utf8mb4_unicode_ci'), index=True, info='codice id da booking')
    order_id = db.Column(db.Integer, info='usato per ordine nei portali')
    name = db.Column(db.String(100, 'utf8mb4_unicode_ci'), info='nome della struttura ricettiva')
    rating = db.Column(db.String(20, 'utf8mb4_unicode_ci'), info='rating della struttura')
    address = db.Column(db.String(100, 'utf8mb4_unicode_ci'), info='indirizzo inclusa la città')
    zip = db.Column(db.String(10, 'utf8mb4_unicode_ci'), info='CAP o ZIP code')
    town = db.Column(db.String(50, 'utf8mb4_unicode_ci'), info='città o località')
    sidecode = db.Column(db.String(11, 'utf8mb4_unicode_ci'), info='codice portale geoloc di appartenenza')
    country = db.Column(db.String(50, 'utf8mb4_unicode_ci'), info='nazione')
    hotel_description = db.Column(db.String(collation='utf8mb4_unicode_ci'), info='descrizione completa')
    hotel_smalldesc = db.Column(db.String(255, 'utf8mb4_unicode_ci'), info='descrizione breve per lista')
    hotel_services = db.Column(db.String(collation='utf8mb4_unicode_ci'), info='servizi catturati da booking')
    arrival = db.Column(db.String(50, 'utf8mb4_unicode_ci'), info='orari di arrivo possibili')
    departure = db.Column(db.String(50, 'utf8mb4_unicode_ci'), info='orari di partenza possibili')
    location = db.Column(db.String(50, 'utf8mb4_unicode_ci'), info='duplicato di town')
    website = db.Column(db.String(500, 'utf8mb4_unicode_ci'), info='sito internet della struttura')
    phone = db.Column(db.String(100, 'utf8mb4_unicode_ci'), info='telefono struttura')
    mails1 = db.Column(db.String(collation='utf8mb4_unicode_ci'), info='mail struttura principale')
    mails2 = db.Column(db.String(collation='utf8mb4_unicode_ci'), info='mail secondaria 2')
    mails3 = db.Column(db.String(collation='utf8mb4_unicode_ci'), info='mail secondaria 3')
    numero_stelle = db.Column(db.String(50, 'utf8mb4_unicode_ci'), info='stelle da booking')
    tipologia_struttura = db.Column(db.String(50, 'utf8mb4_unicode_ci'), info='tipo di struttura es hotel camera villa etc')
    author = db.Column(db.Integer, nullable=False, info='relation with users id of the owner')
    cover_image = db.Column(db.String(200, 'utf8mb4_unicode_ci'), info='link to cover image if present')
    additional_rules = db.Column(db.String(collation='utf8mb4_unicode_ci'), nullable=False, info='Additional Rules')
    services = db.Column(db.String(collation='utf8mb4_unicode_ci'), nullable=False, info='Hotel Services in json per la pagina dettaglio')

class HotelView(ModelView):
    column_exclude_list = ['seq_id','id','order_id','mails2','mails1','mails3','rating','zip','sidecode','hotel_description','hotel_smalldesc','hotel_services','arrival','departure','services','additional_rules','cover_image','author','numero_stelle']
    column_labels = dict(town='Località',country='Nazione',location='Zona',tipologia_struttura='Tipologia')