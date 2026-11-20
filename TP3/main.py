# importer les modules nécessaires
import os
import sys

# récupérer le dossier dans lequel se trouve main.py
absolute_file_path = os.path.abspath(__file__)
absolute_folder_path = os.path.dirname(absolute_file_path)

# ajouter ce dossier aux chemins de recherche de python
sys.path.append(absolute_folder_path)

# importer l'interface
from ui import AnimationInterface


# créer et afficher la fenêtre
window = AnimationInterface()
window.show()