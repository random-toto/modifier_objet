#!/usr/bin/python3
#-*- coding: utf-8 -*-


def modify_object():
    '''
    '''
    obj = input("Nom de l'objet du programme à modifier ? ")
    meslocs = None
    try:
        if obj in locals():
            print("Objet trouvé dans les locales.")
            obj = dict(locals())[obj]
        elif obj in globals():
            print("Objet trouvé dans les globales.")
            obj = dict(globals())[obj]
        else:
            raise ValueError("Objet non trouvé dans locales/globales")
    except Exception as e:
        raise e
    while 1:
        nom_attr = input("Attribut de l'objet à créer/modifier ? ")
        if nom_attr:
            break
    try:
        print("La valeur courante de cet attribut est : ", getattr(obj, nom_attr), sep = '')
    except:
        print("Pas de valeur courante trouvée (ou objet sans attributs, gare !)")
    valeur_attr_str = input("Nouvelle valeur de l'attribut ? ")
    try:
        setattr(obj, nom_attr, valeur_attr_str)
    except Exception as e:
        print("Impossible d'initialiser l'attrbut !")
        raise e
    type_attr_str = input("Quel est le type de cet attribut ? ")
    print("Ayé !")
    print(getattr(obj, nom_attr))


