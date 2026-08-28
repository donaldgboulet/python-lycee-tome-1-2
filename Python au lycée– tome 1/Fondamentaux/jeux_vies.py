import random 

# =_=_=_=A_=_=_=
def calcul_est_exact(niveau_difficile):
    if niveau_difficile:
        a = random.randint(10, 20)
        b = random.randint(10, 20)
    else:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        
    reponse = int(input(f"Calculez {a} x {b} : "))
    return a, b, reponse

# =_=_=_=B_=_=_=
def lancer_le_quiz():
    # Étape d'accueil : Choix de la langue au clavier
    print("🌍 Choisissez votre langue / Choose your language / Sprache wählen :")
    print("1. Français\n2. English\n3. Deutsch")
    choix = input("Votre choix (1/2/3) : ")
    
    if choix == "1":
        lang = "francais"
    elif choix == "2":
        lang = "anglais"
    elif choix == "3":
        lang = "Deutsch"
    else:
        print("Choix invalide, langue par défaut : Français.\n")
        lang = "francais"

    # Initialisation des variables du jeu
    score = 0
    vies = 3
    combo = 0  # Compteur pour le bonus de vie
    alerte_affichee = False  # Règle le bug de l'affichage répété
    jeu_en_cours = True
    
    if lang == "francais":
        print("\n🎮 DEBUT DU QUIZ ! Enchaînez 5 bonnes réponses pour gagner une vie ❤️ ! 🎮\n")
    elif lang == "anglais":
        print("\n🎮 QUIZ START! Get 5 correct answers in a row to win a life ❤️! 🎮\n")
    elif lang == "Deutsch":
        print("\n🎮 QUIZ-START! Beantworte 5 Fragen in Folge richtig für ein Leben ❤️! 🎮\n")

    while jeu_en_cours:
        mode_difficile = (score >= 5)
        
        # L'alerte ne s'affiche désormais qu'UNE seule fois grâce à alerte_affichee
        if score >= 5 and not alerte_affichee:
            if lang == "francais":
                print("⚡ ATTENTION ! Mode difficile activé (Tables de 10 à 20) ! ⚡\n")
            elif lang == "anglais":
                print("⚡ WARNING! Hard Mode activated (Tables from 10 to 20)! ⚡\n")
            elif lang == "Deutsch":
                print("⚡ ACHTUNG! Schwerer Modus aktiviert (Einmaleins von 10 bis 20)! ⚡\n")
            alerte_affichee = True

        a, b, reponse_num = calcul_est_exact(mode_difficile)
        bonne_reponse = a * b
        est_correct = (reponse_num == bonne_reponse)

        if lang == "francais":
            if est_correct:
                score += 1
                combo += 1
                print(f"✅ Bravo ! +1 point (Score : {score} | Vies : {'❤️' * vies})")
                
                # Système de bonus : maximum 5 vies stockées pour ne pas tricher
                if combo == 5:
                    if vies < 5:
                        vies += 1
                        print("💖 SUPER COMBO ! Vous gagnez une vie supplémentaire ! 💖")
                    else:
                        print("🔥 SUPER COMBO ! (Vos vies sont déjà au maximum)")
                    combo = 0  # On réinitialise le compteur de combo
                print()
            else:
                vies -= 1
                combo = 0  # Le combo est brisé !
                print(f"❌ Faux ! La bonne réponse était {bonne_reponse}.")
                if vies > 0:
                    print(f"⚠️ Il vous reste {vies} vie(s) : {'❤️' * vies}\n")
                else:
                    print(f"💀 GAME OVER ! Score final : {score} point(s).\n")
                    jeu_en_cours = False
                    
        elif lang == "anglais":
            if est_correct:
                score += 1
                combo += 1
                print(f"✅ Well done! +1 point (Score: {score} | Lives: {'❤️' * vies})")
                if combo == 5:
                    if vies < 5:
                        vies += 1
                        print("💖 SUPER COMBO! You earned an extra life! 💖")
                    combo = 0
                print()
            else:
                vies -= 1
                combo = 0
                print(f"❌ Wrong! The correct answer was {bonne_reponse}.")
                if vies > 0:
                    print(f"⚠️ You have {vies} live(s) left: {'❤️' * vies}\n")
                else:
                    print(f"💀 GAME OVER! Final score: {score} point(s).\n")
                    jeu_en_cours = False
                    
        elif lang == "Deutsch":
            if est_correct:
                score += 1
                combo += 1
                print(f"✅ Super! +1 Punkt (Punktestand: {score} | Leben: {'❤️' * vies})")
                if combo == 5:
                    if vies < 5:
                        vies += 1
                        print("💖 SUPER-COMBO! Du hast un zusätzliches Leben gewonnen! 💖")
                    combo = 0
                print()
            else:
                vies -= 1
                combo = 0
                print(f"❌ Oh nein! Die richtige Antwort war {bonne_reponse}.")
                if vies > 0:
                    print(f"⚠️ Du hast noch {vies} Leben: {'❤️' * vies}\n")
                else:
                    print(f"💀 GAME OVER! Finaler Punktestand: {score} Punkt(e).\n")
                    jeu_en_cours = False

# Lancement immédiat du jeu (plus besoin de passer de texte dans les parenthèses)
lancer_le_quiz()

