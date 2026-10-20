from maya import cmds
import json
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QCheckBox,
)

# Fonction pour lire le fichier JSON.
def load_data(json_path):
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


# Chemin du fichier JSON.
json_path = r"C:\Users\ltinivella\repos\NAND403_A26_Ateliers\TP2\rules.json"

# Charger les informations du JSON.
data = load_data(json_path)


# Fonction pour organiser les objets.
def organiser():

    # Vérifier les cases cochées.
    selection_only = checkbox_selection.isChecked()
    apply_colors = checkbox_colors.isChecked()
    sort_objects = checkbox_sort.isChecked()

    # Récupérer les objets.
    if selection_only:
        objects = cmds.ls(selection=True, type="transform")
    else:
        objects = cmds.ls(dag=True, type="transform")
    cmds.undoInfo(openChunk=True)

    # Appliquer les couleurs.
    if apply_colors:
        for objet in objects:
          for prefix, color in data.items():
            if objet.startswith(prefix):
                cmds.setAttr(objet + ".useOutlinerColor", True)
                cmds.setAttr(
                    objet + ".outlinerColor",
                    color[0],
                    color[1],
                    color[2],
                    type="double3"
                )

        # Trier les objets alphabétiquement.
    if sort_objects:
        objects = sorted(objects, reverse=True)
        for objet in objects:
            cmds.reorder(objet, front=True)

    cmds.undoInfo(closeChunk=True)

# Créer la fenêtre Maya.
window = QWidget()
window.setWindowTitle("Outliner Organizer")

# Créer le layout.
layout = QVBoxLayout()
window.setLayout(layout)

# Ajouter le titre.
label = QLabel("Outliner Organizer")
layout.addWidget(label)

# Case Selection Only.
checkbox_selection = QCheckBox("Selection Only")
layout.addWidget(checkbox_selection)

# Case Apply Colors.
checkbox_colors = QCheckBox("Apply Colors")
layout.addWidget(checkbox_colors)

# Case Sort Alphabetically.
checkbox_sort = QCheckBox("Sort Alphabetically")
layout.addWidget(checkbox_sort)

# Cocher les cases par défaut.
checkbox_colors.setChecked(True)
checkbox_sort.setChecked(True)

# Bouton Organize.
button = QPushButton("Organize")
layout.addWidget(button)

# Connecter le bouton à la fonction.
button.clicked.connect(organiser)

# Afficher la fenêtre.
window.show()