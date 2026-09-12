# Chapitre 6 — Chaînes de caractères : analyse d'un texte
# Python au lycée – tome 1

# ----- Activité 1 : Pluriels des mots -----
"""Objectifs : écrire petit à petit un programme qui renvoie le pluriel d’un mot donné."""
#-------- 1 --------
mot0 = "Chat" 
print(mot0 + "s")

#-------- 2 --------
mot1 = "Souris"
print(mot1[5])
for i in range(len(mot0)):
    if len(mot0[i-1]) == "s":
        print(mot0)
    else:
        print(mot0 + "s")
    break


#-------- 3 --------
def pluriel_al(mot3):
    #for i in range(len(mot3)):
    if (mot3[-2:]) == "al":
        return mot3[0:-2]+"aux"
    else:
         if (mot3[-1]) == "s":
             return mot3
         else:
            return mot3 + "s"

mot3 = input("Veuilez entre le mot svp: ") 
pluriel_al(mot3)

#-------- 4 --------
def met_au_pluriel(mot):
    resultat = pluriel_al(mot)
    return resultat
mot = input("Veuilez entre le mot svp: ")
resultat_final = met_au_pluriel(mot)
print(resultat_final)
print(met_au_pluriel("Canal"))
print(met_au_pluriel("Voitures"))
print(met_au_pluriel("Enfant"))


#-------- 5 --------
def affiche_conjuguaison(verbe):
    if verbe[-2:]== "er":
        print("Je "+verbe[0:-2]+ "e")
        print("Tu "+verbe[0:-2]+ "es")
        print("Il/Elle "+verbe[0:-2]+ "e")
        print("Nous "+verbe[0:-2]+ "ons")
        print("Vous "+verbe[0:-2]+ "ez")
        print("Ils/Elles "+verbe[0:-2]+ "ent")
    else:
        print("Ce n'est pas un verbe du premier groupe.")
    
verbe = input("Veuillez entrez un verbe du premier groupe Svp: ")    
affiche_conjuguaison(verbe)   