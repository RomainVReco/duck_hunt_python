# duck_hunt_python

## Règles du jeu

Pyjeu mélange réflexe et réflexion dans un jeu de tir à la souris.​


L'objectif est de tirer sur des cibles mouvantes afin de gagner des points, tout en évitant de toucher les leurres et les obstacles.​

Les leurres enlèvent des points, tandis que les obstacles empêchent le joueur de tirer pendant un certain temps, lui faisant perdre de précieuses secondes.​


La partie se termine lorsque le joueur a éliminé toutes les cibles à l'écran mais n'a pas de limite de temps pour le faire.​
​

Les cibles sont des nombres, dont le nombre et le contenu varie selon le niveau de difficulté :​

Facile : Multiples de 2 - (nombre de cible à définir)​

Intermédiaire : Multiples de 7 - (nombre de cible à définir)​

Difficile : Multiple de 3 en hexadécimale - (nombre de cible à définir)​


Le score est calculé en fonction du nombre de cibles détruites, et du temps écoulé avant destruction de l'ensemble des cibles.

## Ordonnancement des écrans 

Lors du lancement du jeu, un écran avec les options suivantes doit être appel (fichier main.py) :​
--> Play (page_niveau.py) / Option / High scores (présent dans le main.py) / Quit​


Le choix de Play affiche un écran de sélection de la difficulté avec 3 choix (fichier page_niveau.py) :​
--> Facile (page_intermediaire_facile.py) / Medium (page_intermediaire_medium.py) / Difficile  (page_intermediaire_difficile.py)​

​
La sélection de la difficulté lance un écran récapitulant les paramètres de la partie (fichiers  page_intermediaire_facile/medium/difficile.py) 


La partie se lance ensuite selon les paramètres préchargés (fichier number_generator.py)​

​
Une fois la partie terminée (cibles détruites), un écran de fin est proposé (non présent):
