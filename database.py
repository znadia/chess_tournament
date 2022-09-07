from tinydb import TinyDB, Query
import json

User = Query()

def create_db_file(name_file):
    db = TinyDB('db_' + name_file + '.json')

    return db

"""
def insert_db_players(dic_obj, db):
    for k,v in dic_obj.items():
        dic_data  = {}
        dic_data["num_joueur"] = k
        dic_data["name"] = v.name
        dic_data["first_name"] = v.first_name
        dic_data["d_o_b"] = v.d_o_b
        dic_data["sex"] = v.sex
        dic_data["score"] = v.score
        db.insert(dic_data)
"""
def insert_db_players(dic_obj, db):
    for key in dic_obj.keys():
        info = dic_obj[key].__dict__
        db.insert(info)

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

