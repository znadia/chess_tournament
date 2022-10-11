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


def insert_db_round(list_match, db):
        db.insert(list_match)

def dic_round_match(dic_filtered, name_round, list_filtered_player):
    dic_filtered[name_round] = list_filtered_player
    return dic_filtered


def display_db(db):
        print(db.all())





def search(db):
    # Recherche un element dans la db
    result = db.search(User.name == 'John')
    print(result)


def update(db):
    # Modifie la db grace a un element
    db.update({'age': 68}, User.name == 'John')


def delete(db):
    # Supprime un element de la db
    db.remove(User.name == 'Lina')

