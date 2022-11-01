from tinydb import TinyDB, Query
import json

User = Query()

def create_db_file(name_file):
    db = TinyDB('db_' + name_file + '.json')
    print("nom du fichier", db)
    return db


def insert_db_info(dic_obj, db):
        # Insert dans la db 
        for key in dic_obj.keys():
                entry = {}
                entry[key]= dic_obj[key].__dict__
                db.insert(entry)


def add_data(dic_obj, db):
    db.truncate()
    insert_db_info(dic_obj, db)


def open_db(name_file):
         with open('db_' + name_file + '.json') as json_file:
                data = json.load(json_file)
                return data['_default']['1']

