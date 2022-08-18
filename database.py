from tinydb import TinyDB, Query
import json


FILE = 'database.json'
# db = TinyDB('database.json')
# User = Query()

b = {'name': 'Lina', 'age': 30}

def serialize(params, name_file):
    for key in params:
        print("KEY AND V before", key, params[key], type(params[key]))

        params[key] = json.dumps(repr(params[key]), indent=4)
        
        print("KEY AND V after", key, params[key], type(params[key]))
    
    print("DICCCC", params)
    dic_dump = json.dumps(params)
    print("DICCCC DUMPPPp", dic_dump)
    f = open(name_file, "a", encoding="utf-8")
    f.write("NOM DU TOURNOI")
    f.write("\n")
    f.write(dic_dump)

    f.write("\n")
    f.write("\n")
    f.close()

def deserialize(name_file):
    f = open(name_file, "r", encoding="utf-8")
    fil = f.read()
    print("FILLL", fil, type(fil))
    params = json.loads(fil)
    print("FFFFFF DIC_RETTTTT", fil, type(fil), params, type(params))
    for key in params:
        print("KEY AND V before deserialize", key, params[key], type(params[key]))
        params[key] = json.loads(params[key])
        print("KEY AND V after deserialize", key, params[key], type(params[key]))
    return params


def insert(dic):
    # Insert dans le bd
    #with open( "datafile.json" , "w" ) as write
    # f = open("demofile2.json", "w", encoding="utf-8")
    # print("DICCCC", dic)
    # print("DICCCC", type(dic))
    serialize(dic, FILE)
    # y = json.dumps(str(dic))
    # print("YYYY", y)
    # print("YYYY", type(y))
    # db.dump(dic)
    # f.write(json.dumps(str(dic), sort_keys = True, indent = 2, ensure_ascii=True))
    # f.close()

    # #open and read the file after the appending:
    # f = open("demofile2.json", "r", encoding="utf-8")
    # fil = f.read()
    # dic_ret = json.loads(fil)
    # print("FFFFFF READDDD", type(f.read()))
    # dic_ret = 
    # print("FFFFFF DIC_RETTTTT", fil, type(fil), dic_ret, type(dic_ret))
    # db.insert(str(dic))
    # print("DBBBBBBBB", db.all())
    return(dic)


def search():
    # Recherche un element dans la db
    result = db.search(User.name == 'John')
    print(result)

def update():
    # Modifie la db grace a un element
    db.update({'age': 68}, User.name == 'John')

def delete():
    # Supprime un element de la db
    db.remove(User.name == 'Lina')

####### efface la db
#db.truncate()
#insert(b)
#search()
#update()
#delete()
#print(db.all())
"""
parsed_json = json.dump(b)
print(parsed_json)
"""