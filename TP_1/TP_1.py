import sys
import json
import os
from PySide6.QtWidgets import (
    QApplication, QTableWidget, QTableWidgetItem,
    QWidget, QVBoxLayout, QLineEdit
)

# ouvrir le fichier json
def load_data(json_path):
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data

# barre de recherche / outil de recherche
def filtrer_tableau(texte_recherche):
    texte_recherche = texte_recherche.lower()
    for ligne in range(table.rowCount()):
        # par défaut, on cache la ligne
        ligne_visible = False
        for colonne in range(table.columnCount()):
            item = table.item(ligne, colonne)
            if item and texte_recherche in item.text().lower():
                ligne_visible = True
                break  # pas besoin de checker les autres colonnes
        table.setRowHidden(ligne, not ligne_visible)

# Ouvrir application
app = QApplication()

# widget principal + layout (pour contenir la barre de recherche ET le tableau)
fenetre = QWidget()
layout = QVBoxLayout()

# barre de recherche
barre_recherche = QLineEdit()
barre_recherche.setPlaceholderText("Rechercher...")
barre_recherche.textChanged.connect(filtrer_tableau)

# Afficher interface du tableau
table = QTableWidget()

# attribuer a une variable le chemin de fichier du fichier json
chemin_json = "data_small.json"

# charger les données du fichier json
data = load_data(chemin_json)

# recuperer les informations du nom, taille et d'elements du fichier json
nom = os.path.basename(chemin_json)
taille = os.path.getsize(chemin_json)
nombre_elem = len(data)

# Afficher les informations du json dans le terminal
print("Nom :", nom)
print("Taille :", taille, "octets")
print("Nombre d'éléments :", nombre_elem)

# Recuperer les noms des colonnes du fichier json
colonnes = list(data[0].keys())

# faire le nombre de lignes et colonnes equivalents au contenu
table.setRowCount(len(data))
table.setColumnCount(len(colonnes))
table.setHorizontalHeaderLabels(colonnes)

# remplir le tableau
for i, item in enumerate(data):
    for j, cle in enumerate(colonnes):
        valeur = str(item[cle])
        table.setItem(i, j, QTableWidgetItem(valeur))

# classer odre croissant decroissant
table.setSortingEnabled(True)

# ajuster la largeur des colonnes selon le contenu
table.resizeColumnsToContents()

# assembler le layout : barre de recherche en haut, tableau en dessous
layout.addWidget(barre_recherche)
layout.addWidget(table)
fenetre.setLayout(layout)

# montrer la fenêtre (au lieu du tableau seul)
fenetre.show()

# lancer l'application
sys.exit(app.exec())