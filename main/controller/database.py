import json

from tinydb import Query, TinyDB

User = Query()


def create_db_file(name_file):
    db = TinyDB("data/" + name_file + ".json")
    return db


def insert_db_info(dic_obj, db):
    db.truncate()
    # Insert dans la db
    for key in dic_obj.keys():
        entry = {}
        entry[key] = dic_obj[key].__dict__
        db.insert(entry)


def open_db(name_file):
    """Récupère les infos d'un autre fichier JSON,
    pour reprendre un autre tournoi"""

    with open("data/" + name_file) as json_file:
        data = json.load(json_file)
        file = name_file.split(".")[0]
        end = data["_default"]["1"][file]["end"]
        if end is True:
            print("Ce tournoi est terminé")
            return False
        else:
            return data["_default"]["1"]


def open_tournament(name_file):
    with open("data/" + name_file) as json_file:
        data = json.load(json_file)
        file = name_file.split(".")[0]
        print(name_file)
        return data["_default"]["1"][file]["players"]
