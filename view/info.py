import re


def check_time_control():
    choice = ["bullet", "blitz", "coup rapide"]
    time_control = input("Un bullet, un blitz ou un coup rapide: ")

    while time_control not in choice:
        time_control = input(
            "Veuillez choisir entre un bullet, un blitz ou un coup rapide: "
        )
    return time_control


def check_nbr_round():
    nbr = input("nombre de round: ")

    if not nbr:
        nbr = 4
        print("Le nombre de round sera de 4 par defaut")
    return nbr

    while not nbr.isnumeric() is True:
        nbr = input("Veuillez le nombre de round: ")
    return nbr


def int_date_birthday():

    regex = re.compile(r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$")
    result = input("Date de naissance (format jj/mm/aaaa): ")

    while not re.findall(regex, result):
        result = input("Veuillez entrer une date de naissance valide: ")

    return result


def check_sex():
    choice = ["Homme", "Femme", "h", "f"]
    check_sex = input("Homme ou Femme: ")

    while check_sex not in choice:
        check_sex = input("Veuillez entrer h nou f: ")
    return check_sex
