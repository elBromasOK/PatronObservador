# import mysql.connector

# ###########################################
# def crearbd():
#     try:
#         mibase = mysql.connector.connect(host="localhost", user="root", passwd="" )
#         micursor = mibase.cursor()
#         micursor.execute("CREATE DATABASE baseprueba3")
#         mibase = mysql.connector.connect(host="localhost", user="root",passwd="",database="baseprueba3")
#         micursor = mibase.cursor()
#         micursor.execute("CREATE TABLE producto( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE utf8_spanish2_ci NOT NULL )")
#         print("Base de datos con tabla creada")
#         showinfo('-', 'Base de datos con tabla creada')
#     except:
#         print("Ya existe la base de datos")
#         showinfo('-', 'Ya existe la base de datos')

# def miconexion():
        
#     mibase = mysql.connector.connect(host="localhost", user="root", passwd="", database="baseprueba3")
#     return mibase

from peewee import *
import datetime

db = SqliteDatabase('baseprueba3.db')

class BaseModel(Model):
    class Meta:
        database = db

class Articulos(BaseModel):
    ID = AutoField(unique = True, primary_key = True)
    titulo = CharField(max_length = 20)
    descripcion = CharField(max_length = 20)

    class Meta:
        table_name = 'tablaarticulos'

class registrosAlta(BaseModel):
    ID = AutoField(unique = True, primary_key = True)
    titulo = CharField(max_length = 20)
    descripcion = CharField(max_length = 20)
    agregado_on = DateTimeField(default=datetime.datetime.now)

    class Meta:
        table_name = 'tablaaltas'

class registrosModif(BaseModel):
    ID_modif = AutoField(unique = True, primary_key = True)
    ID_record = IntegerField(null=False)
    titulo_old = CharField(max_length = 20)
    titulo_new = CharField(max_length = 20)
    descripcion_old = CharField(max_length = 20)
    descripcion_new = CharField(max_length = 20)
    modif_on = DateTimeField(default=datetime.datetime.now)

    class Meta:
        table_name = 'tablamodif'

class registrosElim(BaseModel):
    ID_elim = AutoField(unique = True, primary_key = True)
    ID_record = IntegerField(null=False)
    titulo = CharField(max_length = 20)
    descripcion = CharField(max_length = 20)
    elim_on = DateTimeField(default=datetime.datetime.now)

    class Meta:
        table_name = 'tablaelim'

db.connect()

# Se crea la tabla que se muestra en la app
db.create_tables([Articulos])

# Se crean las tablas de registros que salen de los observadores
db.create_tables([registrosAlta])
db.create_tables([registrosModif])
db.create_tables([registrosElim])