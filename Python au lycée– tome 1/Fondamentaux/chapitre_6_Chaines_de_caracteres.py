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





# ----- Activité 2 :Jeux de mots --8##---
""" Objectifs : manipuler des mots de façon amusante """

# 1:-) 1. Distance entre deux mots.


def distance_hamming(mot1,mot2):
    compteur = 0
    for i in range(len(mot1)):
            if mot1[i] != mot2[i]:
                compteur +=1
    return compteur   
    
mot1 = input("Veuillez entrez le premier mot que vouz vouliez calculer la distance: ")
mot2 = input("Veuillez entrez le deuxieme mot que vouz vouliez calculer la distance: ")
print(distance_hamming(mot1,mot2))
print(distance_hamming("SAPIN","LAPIN"))
print(distance_hamming("JAPON","SAVON"))
print(distance_hamming("LAPIN","SATIN"))


# 2:-) 2. Le Latin-cochon

def latin_cochon(mot):
    
    if	mot[0] in "aeiuoyEAIUYO":
            print("Votre mot commence par une Voyelle pas besoin alors d'appliquer le latin cochon Merci")
            return mot.upper()
    else:
        mot = mot[0:]
        new_mot = mot[1:] + mot[0].lower() +"um"
        return new_mot.upper()
#mot = input("Veuillez entrez votre mot: ")   
print(latin_cochon("Bonjour"))
print(latin_cochon("VITRE"))
print(latin_cochon("Orange"))


# 3:-) 3. Le Verlan

def verlan(mot):
    mot = mot[::-1]
    return mot.upper()
    
print(verlan("Tocard"))
    

# 4:-) 4. Palindrome

def est_un_palindrome(mot):
    if mot == mot[::-1]:
         return True
        # print("Le mot",mot," est pas  palindrome")
    else:
        return False
        #print("Le mot",mot,"n'est pas palindrome")
        
print(est_un_palindrome("bonjour"))
print(est_un_palindrome("kayak"))


# ----- Activité 3 : Activité 3 (ADN)s ---



""".
Une molécule d’ADN est formée d’environ six milliards de nucléotides. L’ordinateur est donc un
outil indispensable pour l’analyse de l’ADN. Dans un brin d’ADN il y a seulement quatre types de
nucléotides qui sont notés A, C, T ou G. Une séquence d’ADN est donc un long mot de la forme :
TAATTACAGACCTGAA.."""  


# 1:-) 

def presence_de_A(sequence):
    if "A" in sequence:
        return True
    else:
        return False
print(presence_de_A("TAATTACAGACCTGAA"))
print(presence_de_A("ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGG"))
print(presence_de_A("CTTGCT"))


# 2:-)
def position_de_AT(sequence):
    #if sequence in presence_de_A:
    for i in range(len(sequence)-1):
        if sequence[i] == "A":
            if sequence[i+1] == "T":
                return i
    return None 
print(position_de_AT("CTTATGCT"))
print(position_de_AT("GATATAT"))
print(position_de_AT("GACCGTA"))


# 3:-)
def  position(code,sequence):
    for i in range(len(sequence)):
        if sequence[i:i+len(code)]==code:
            return i
    return None

print(position("GG","GACCGTA"))
print(position("GG","CTTATGGCT"))
print(position("CC","CCTTATGCTGGG"))


# 4:-)
def  coupable(code,sequence):
    for i in range(len(sequence)):
        if sequence[i:i+len(code)]==code:
            return i
    return None

print(coupable("CATA","CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC"))
print(coupable("CATA","CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG"))
print(coupable("CATA","AAGCTCGGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCC"))
print(coupable("CATA","CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"))
print("############")

print(coupable("ATGC","CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC"))
print(coupable("ATGC","CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG"))
print(coupable("ATGC","AAGCTCGGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCC"))
print(coupable("ATGC","CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"))

# La coupable est Mlle Rose : elle est la seule (avec le Colonel Moutarde) à avoir les deux codes CATA et ATGC,
# mais chez elle les deux positions sont vraiment éloignées (position 6 et 59, soit 53 d'écart),
# contrairement au Colonel Moutarde où elles sont presque collées (34 et 37, seulement 3 d'écart) probablement une coïncidence.
# Et  Mme Pervenche, M. Leblanc ne sont pas du tout des coupable car le brin "CATA", n'apparait par dans leur ADN du coup la fonction renvoir None pourles deux 
