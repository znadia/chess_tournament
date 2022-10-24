from tinydb import TinyDB, Query
import json

User = Query()

def create_db_file(name_file):
    db = TinyDB('db_' + name_file + '.json')
    return db


def insert_db_info(dic_obj, db):
        # Insert dans la db 
        for key in dic_obj.keys():
                entry = {}
                entry[key]= dic_obj[key].__dict__
                db.insert(entry)


def insert_db_round(dic_obj, db):
        db.insert(dic_obj)

def add_data(dic_obj, db):
    db.truncate()
    insert_db_info(dic_obj, db)


def display_db(db):
        print(db.all())
