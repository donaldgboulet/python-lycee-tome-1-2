"""
Projet : Convertisseur de notes Fr => De

But : convertir une note française (sur 20) en note allemande (sur 6),
puis afficher la mention correspondante en allemand.

Utilise : fonctions, paramètres, return, conditions (chapitre 4).

"""
def note_fr_vers_de(note_francaise):
    """Convertit une note française (/20) en note allemande (/6)."""
    return 6 - (note_francaise / 20) * 5
    
    
def mention(note_allemande):
    if note_allemande <= 1.5:
        return "Sehr gut"
    elif note_allemande <= 2.5:        
        return "Gut"
    elif note_allemande<= 3.5:       
        return "Befriedigend"
    elif note_allemande <= 4.5:
        return "Ausreichend"
    else:
        return "Ungenügend"
 
def bulletin():                         
    note_francaise = int(input("Note sur 20 : "))
    note_allemande = note_fr_vers_de(note_francaise)     
    men = mention(note_allemande)
    print("Note française :", note_francaise, "/20")
    print("Note allemande :", note_allemande, "/6")
    print("Mention :", men)
bulletin()
        
    