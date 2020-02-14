# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Index, Integer, String, Text
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Campagne(db.Model):
    __tablename__ = 'campagne'

    id = db.Column(db.Integer, primary_key=True, unique=True, info='auto increment id')
    titolo_campagna = db.Column(db.String(255), info='campaign title\\n')
    data_inizio_campagna = db.Column(db.Date, info='starting date')
    data_fine_campagna = db.Column(db.Date, info='ending date')
    rel_utente_campagna = db.Column(db.Integer, info='user correlation')
    tipo_campagna = db.Column(db.Integer, info='kind of campaign')
    costo_campagna = db.Column(db.Integer, info='campaign cost')
    status_campagna = db.Column(db.Integer)
    campagin_cover = db.Column(db.String(255))



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



class HotelOld(db.Model):
    __tablename__ = 'hotel_old'

    seq_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(20), index=True)
    order_id = db.Column(db.Integer)
    name = db.Column(db.String(100))
    stars = db.Column(db.String(20))
    address = db.Column(db.String(100))
    zip = db.Column(db.String(10))
    town = db.Column(db.String(50))
    sidecode = db.Column(db.String(11))
    country = db.Column(db.String(50))
    hotel_description = db.Column(db.Text)
    hotel_services = db.Column(db.Text)
    arrival = db.Column(db.String(50))
    departure = db.Column(db.String(50))
    location = db.Column(db.String(50))
    website = db.Column(db.String(500))
    phone = db.Column(db.String(100))
    mails1 = db.Column(db.Text)
    mails2 = db.Column(db.Text)
    mails3 = db.Column(db.Text)
    numero_stelle = db.Column(db.String(50))
    tipologia_struttura = db.Column(db.String(50))
    author = db.Column(db.Integer, nullable=False)
    cover_image = db.Column(db.String(200))
    additional_rules = db.Column(db.Text, nullable=False, info='Additional Rules')
    services = db.Column(db.Text, nullable=False, info='Hotel Services')



class HotelVert(db.Model):
    __tablename__ = 'hotel_vert'

    id = db.Column(db.Integer, primary_key=True)
    rel_hotel = db.Column(db.Integer, nullable=False, index=True)
    rel_sitecode = db.Column(db.String(11), nullable=False, index=True)
    order_id = db.Column(db.Integer)



class HotelsTag(db.Model):
    __tablename__ = 'hotels_tags'

    hotels_tags_id = db.Column(db.Integer, primary_key=True, unique=True)
    hotel_id = db.Column(db.Integer, info='correlazione con gli hotels')
    tag_id = db.Column(db.Integer, info='correlazione con i tags')



class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    hotel_id1 = db.Column(db.String(50), index=True)
    filepath = db.Column(db.String(255), unique=True)
    hotel_id = db.Column(db.Integer, nullable=False)



class ImagesOld(db.Model):
    __tablename__ = 'images_old'
    __table_args__ = (
        db.Index('idx_name', 'id', 'path'),
    )

    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.String(50), index=True)
    path = db.Column(db.String(100), nullable=False, unique=True)



class ImagesVeryold(db.Model):
    __tablename__ = 'images_veryold'
    __table_args__ = (
        db.Index('idx_name', 'id', 'path'),
    )

    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.String(50), index=True)
    path = db.Column(db.String(100))



class OffertaBanner(db.Model):
    __tablename__ = 'offerta_banner'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    titolo_ob = db.Column(db.String(255), nullable=False)
    rel_campagna_ob = db.Column(db.Integer)
    rel_utente_ob = db.Column(db.Integer)
    tipologia_ob = db.Column(db.Integer)
    descrizione_ob = db.Column(db.String)
    servizi_inclusi_ob = db.Column(db.String)
    urlcover_ob = db.Column(db.String(255))
    datainizio_ob = db.Column(db.Date)
    datafine_ob = db.Column(db.Date)
    giorninotti_ob = db.Column(db.Integer)
    numero_gn_ob = db.Column(db.Integer)
    calcolo_costo_ob = db.Column(db.Integer)
    numperscam_ob = db.Column(db.Integer)
    costo_ob = db.Column(db.Integer)
    sconto_perc_ob = db.Column(db.Integer)
    sconto_impo_ob = db.Column(db.Integer)
    risparmio_ob = db.Column(db.Integer)
    cell_contatto = db.Column(db.String(30))
    tipo_trattamento = db.Column(db.String(45))
    url_destinazione = db.Column(db.String(255))
    visibile_su = db.Column(db.Integer)
    pubblicazione_ob = db.Column(db.Integer)
    kw_01_desc = db.Column(db.String(255))
    kw_02_localita = db.Column(db.String(255))
    kw_03_zona = db.Column(db.String(255))
    kw_04_importo = db.Column(db.Integer)
    status_ob = db.Column(db.Integer)



class OfferteTag(db.Model):
    __tablename__ = 'offerte_tags'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    offerta_id = db.Column(db.Integer)
    tagsoff_id = db.Column(db.Integer)



class TagsMain(db.Model):
    __tablename__ = 'tags_main'

    tag_id = db.Column(db.Integer, primary_key=True, unique=True)
    tag_name = db.Column(db.String(64), nullable=False, info='Nome in italiano del tag')
    tag_name_en = db.Column(db.String(64), info='Nome in inglese del tag')
    tag_name_fr = db.Column(db.String(64), info='Nome in francese del tag')
    tag_name_de = db.Column(db.String(64), info='Nome in tedesco del tag')
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())



class Tagsofferte(db.Model):
    __tablename__ = 'tagsofferte'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(45), nullable=False)
    name_en = db.Column(db.String(45))
    name_fr = db.Column(db.String(45))
    name_de = db.Column(db.String(45))
    tagiconurl = db.Column(db.String(255))
    tagbkcolor = db.Column(db.String(45))
    tagfgcolor = db.Column(db.String(45))



class User(db.Model):
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
