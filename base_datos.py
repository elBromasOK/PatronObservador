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
    hour = DateTimeField()
    titulo = CharField(max_length = 20)
    descripcion = CharField(max_length = 20)

    class Meta:
        table_name = 'tablaaltas'

db.connect()
db.create_tables([Articulos])
db.create_tables([registrosAlta])