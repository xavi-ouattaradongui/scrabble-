from random import randint
import random
 
liste_mots_cachee =  ["arbre","maison","chat","soleil","mer","étoile","vent","fleur","rivière","montagne","nuage","livre","musique","chocolat","ruisseau","oiseau","fenêtre","chemin","jardin","danse"]

def coller_elements(liste):
    resultat = ""
    i = 0
    while i < len(liste):
        resultat += liste[i]  
        i += 1  
    return resultat



def choisir_mots(mots):
  if len(mots) < 3:
    return mots
  return random.sample(mots, 3)





def melanger_mot(mot):

    lettres = list(mot)
    random.shuffle(lettres)
    mot_melange = ''.join(lettres)
    return mot_melange

mot = coller_elements(liste_mots_cachee)
mot_melange = melanger_mot(mot)



def supprimer_doublons(mots):

    mot_sans_doublons = ''.join(sorted(set(mots), key=mots.index))
    return mot_sans_doublons


mot_initial = melanger_mot(mot)
mot_melange = melanger_mot(mot_initial)
mot_sans_doublons = supprimer_doublons(mot_melange)



def jeu_manche():
    manche = 0

    while manche < 3:
      print("\ntrouver les mots cachée : ")
      manche_jeu = choisir_mots((liste_mots_cachee))
      mot_melange = melanger_mot(manche_jeu)
      mot_sans_doublons = supprimer_doublons(mot_melange)
      print("\n",mot_sans_doublons)
      print("\n")
      manche = manche + 1
      return


def jeu_final():


      score = 0
      mots_trouves = []
      mots_a_trouver = liste_mots_cachee

      while len(mots_trouves) < 3:

          jeu_manche()
          mot = input(f"Entrez un mot trouvé (ou 'Quit' pour passer) : ")
          if mot.lower() == 'quit':
            break
          if mot in mots_a_trouver and mot not in mots_trouves:
             mots_trouves.append(mot)
             score = score + 1
             print(f"Bravo ! Vous avez trouvé : {mot}")
          else:
             print(f"{mot} n'est pas dans les mots à trouver ou déjà trouvé.")


          print(f"Score : {len(mots_trouves)}")


      print(f"Fin de la manche. Score : {score}")
      return score




def jeu_scrabble():
    jeu = 0
    total_points = 0
    print("\nBienvenue dans le jeu de Scrabble !")
    partie_jeu = input("Voulez-vous jouer une partie ? (Oui/Non) : ")
    if partie_jeu.lower() != "oui":
        print("Au revoir !")
        return

    while jeu < 3:
        points = jeu_final()
        total_points = total_points + points
        jeu = jeu + 1

    print(f"\nFin des parties de Scrabble. Total des points : {total_points}.")

jeu_scrabble()