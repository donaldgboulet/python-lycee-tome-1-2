import random 

# =_=_=_=A_=_=_=
# Étape 1 : Cette fonction s'occupe de la saisie des données.
# Elle génère les nombres, demande la réponse et RENVOIE tout au programme.
def calcul_est_exact():
    a = random.randint(1,9)
    b = random.randint(1,9)
    # On pose une question neutre ou standard ici
    reponse = int(input(f"Calculez {a} x {b} : "))
    
    # On renvoie les 3 informations d'un coup à la fonction qui l'appellera
    return a, b, reponse

# =_=_=_=B_=_=_=
# Étape 2 : Cette fonction s'occupe UNIQUEMENT de la logique de la langue.
def test_multiplication(lang):
    
    # 1. On récupère les résultats générés par le "Jeu 1" (Fonction A)
    a, b, reponse_num = calcul_est_exact()
    
    # 2. On fait la vérification mathématique en arrière-plan
    bonne_reponse = a * b
    est_correct = (reponse_num == bonne_reponse)

    # 3. On gère TOUT l'affichage (la question personnalisée et le verdict) selon la langue
    if lang == "francais":
        print(f"-> Votre question était : Combien font {a} x {b} ?")
        if est_correct:
            print("Bravo ! C'est exact.")
        else:
            print(f"Faux ! La bonne réponse était {bonne_reponse}.")
            
    elif lang == "anglais":
        print(f"-> Your question was: How much is {a} x {b} ?")
        if est_correct:
            print("Well done! That's correct.")
        else:
            print(f"Wrong! The correct answer was {bonne_reponse}.")
            
    elif lang == "Deutsch":
        print(f"-> Deine Frage war: Wie viel ist {a} x {b} ?")
        if est_correct:
            print("Super! Das ist richtig.")
        else:
            print(f"Oh nein! Die richtige Antwort war {bonne_reponse}.")
    else:
        print("Langue non supportée / Language not supported")
        return False
        
    return est_correct

# Exemple de test
test_multiplication("francais")
