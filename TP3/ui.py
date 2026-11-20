# importer les éléments nécessaires pour créer l'interface
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QSpinBox,
    QDoubleSpinBox,
    QGroupBox,
    QGridLayout,
    QVBoxLayout
)

# importer la fonction qui va générer l'animation
from animator import generate_animation


class AnimationInterface(QWidget):

    def __init__(self):
        super().__init__()

        # nom de la fenêtre
        self.setWindowTitle("Random Animation Generator")

        # créer le layout principal qui place les éléments verticalement
        self.interface = QVBoxLayout()

        # créer les différentes sections de l'interface
        self.create_timing()
        self.create_translation()
        self.create_rotation()
        self.create_scale()

        # créer le bouton generate
        self.generate_button = QPushButton("Generate")

        # connecter le bouton à la fonction de génération d'animation
        self.generate_button.clicked.connect(
            lambda: generate_animation(self)
        )

        # ajouter le bouton à l'interface
        self.interface.addWidget(self.generate_button)

        # ajouter un espace sous le bouton
        self.interface.addStretch()

        # appliquer le layout principal à la fenêtre
        self.setLayout(self.interface)

    # section pour régler la durée et le step de l'animation
    def create_timing(self):

        # créer le groupe et son layout
        self.timing_group = QGroupBox("Animation Timing")
        self.timing_layout = QGridLayout()

        # créer le champ pour la durée
        self.duration_text = QLabel("Duration")
        self.duration_nb = QSpinBox()
        self.duration_nb.setRange(1, 10000)
        self.duration_nb.setValue(100)

        # créer le champ pour le step
        self.step_text = QLabel("Step")
        self.step_nb = QSpinBox()
        self.step_nb.setRange(1, 1000)
        self.step_nb.setValue(1)

        # placer les éléments dans le layout
        self.timing_layout.addWidget(self.duration_text, 0, 0)
        self.timing_layout.addWidget(self.duration_nb, 0, 1)
        self.timing_layout.addWidget(self.step_text, 1, 0)
        self.timing_layout.addWidget(self.step_nb, 1, 1)

        # ajouter le layout au groupe
        self.timing_group.setLayout(self.timing_layout)

        # ajouter le groupe à l'interface principale
        self.interface.addWidget(self.timing_group)

    # section pour régler la translation
    def create_translation(self):

        # créer le groupe et son layout
        self.translation_group = QGroupBox("Translation")
        self.translation_layout = QGridLayout()

        # créer les champs min et max pour chaque axe
        self.translation_X_min = QDoubleSpinBox()
        self.translation_X_max = QDoubleSpinBox()
        self.translation_Y_min = QDoubleSpinBox()
        self.translation_Y_max = QDoubleSpinBox()
        self.translation_Z_min = QDoubleSpinBox()
        self.translation_Z_max = QDoubleSpinBox()

        # permettre des valeurs positives et négatives
        self.translation_X_min.setRange(-1000, 1000)
        self.translation_X_max.setRange(-1000, 1000)
        self.translation_Y_min.setRange(-1000, 1000)
        self.translation_Y_max.setRange(-1000, 1000)
        self.translation_Z_min.setRange(-1000, 1000)
        self.translation_Z_max.setRange(-1000, 1000)

        # ajouter les titres des colonnes
        self.translation_layout.addWidget(QLabel("Axis"), 0, 0)
        self.translation_layout.addWidget(QLabel("Min"), 0, 1)
        self.translation_layout.addWidget(QLabel("Max"), 0, 2)

        # ajouter les champs de l'axe x
        self.translation_layout.addWidget(QLabel("X"), 1, 0)
        self.translation_layout.addWidget(self.translation_X_min, 1, 1)
        self.translation_layout.addWidget(self.translation_X_max, 1, 2)

        # ajouter les champs de l'axe y
        self.translation_layout.addWidget(QLabel("Y"), 2, 0)
        self.translation_layout.addWidget(self.translation_Y_min, 2, 1)
        self.translation_layout.addWidget(self.translation_Y_max, 2, 2)

        # ajouter les champs de l'axe z
        self.translation_layout.addWidget(QLabel("Z"), 3, 0)
        self.translation_layout.addWidget(self.translation_Z_min, 3, 1)
        self.translation_layout.addWidget(self.translation_Z_max, 3, 2)

        # ajouter le layout au groupe
        self.translation_group.setLayout(self.translation_layout)

        # ajouter le groupe à l'interface principale
        self.interface.addWidget(self.translation_group)

    # section pour régler la rotation
    def create_rotation(self):

        # créer le groupe et son layout
        self.rotate_group = QGroupBox("Rotation")
        self.rotate_layout = QGridLayout()

        # créer les champs min et max pour chaque axe
        self.rotate_X_min = QDoubleSpinBox()
        self.rotate_X_max = QDoubleSpinBox()
        self.rotate_Y_min = QDoubleSpinBox()
        self.rotate_Y_max = QDoubleSpinBox()
        self.rotate_Z_min = QDoubleSpinBox()
        self.rotate_Z_max = QDoubleSpinBox()

        # définir les limites de rotation en degrés
        self.rotate_X_min.setRange(-360, 360)
        self.rotate_X_max.setRange(-360, 360)
        self.rotate_Y_min.setRange(-360, 360)
        self.rotate_Y_max.setRange(-360, 360)
        self.rotate_Z_min.setRange(-360, 360)
        self.rotate_Z_max.setRange(-360, 360)

        # ajouter les titres des colonnes
        self.rotate_layout.addWidget(QLabel("Axis"), 0, 0)
        self.rotate_layout.addWidget(QLabel("Min"), 0, 1)
        self.rotate_layout.addWidget(QLabel("Max"), 0, 2)

        # ajouter les champs de l'axe x
        self.rotate_layout.addWidget(QLabel("X"), 1, 0)
        self.rotate_layout.addWidget(self.rotate_X_min, 1, 1)
        self.rotate_layout.addWidget(self.rotate_X_max, 1, 2)

        # ajouter les champs de l'axe y
        self.rotate_layout.addWidget(QLabel("Y"), 2, 0)
        self.rotate_layout.addWidget(self.rotate_Y_min, 2, 1)
        self.rotate_layout.addWidget(self.rotate_Y_max, 2, 2)

        # ajouter les champs de l'axe z
        self.rotate_layout.addWidget(QLabel("Z"), 3, 0)
        self.rotate_layout.addWidget(self.rotate_Z_min, 3, 1)
        self.rotate_layout.addWidget(self.rotate_Z_max, 3, 2)

        # ajouter le layout au groupe
        self.rotate_group.setLayout(self.rotate_layout)

        # ajouter le groupe à l'interface principale
        self.interface.addWidget(self.rotate_group)

    # section pour régler le scale
    def create_scale(self):

        # créer le groupe et son layout
        self.scale_group = QGroupBox("Scale")
        self.scale_layout = QGridLayout()

        # créer les champs min et max pour chaque axe
        self.scale_X_min = QDoubleSpinBox()
        self.scale_X_max = QDoubleSpinBox()
        self.scale_Y_min = QDoubleSpinBox()
        self.scale_Y_max = QDoubleSpinBox()
        self.scale_Z_min = QDoubleSpinBox()
        self.scale_Z_max = QDoubleSpinBox()

        # éviter un scale égal à zéro ou négatif
        self.scale_X_min.setRange(0.01, 100)
        self.scale_X_max.setRange(0.01, 100)
        self.scale_Y_min.setRange(0.01, 100)
        self.scale_Y_max.setRange(0.01, 100)
        self.scale_Z_min.setRange(0.01, 100)
        self.scale_Z_max.setRange(0.01, 100)

        # définir les valeurs de départ pour le scale
        self.scale_X_min.setValue(1)
        self.scale_X_max.setValue(1)
        self.scale_Y_min.setValue(1)
        self.scale_Y_max.setValue(1)
        self.scale_Z_min.setValue(1)
        self.scale_Z_max.setValue(1)

        # ajouter les titres des colonnes
        self.scale_layout.addWidget(QLabel("Axis"), 0, 0)
        self.scale_layout.addWidget(QLabel("Min"), 0, 1)
        self.scale_layout.addWidget(QLabel("Max"), 0, 2)

        # ajouter les champs de l'axe x
        self.scale_layout.addWidget(QLabel("X"), 1, 0)
        self.scale_layout.addWidget(self.scale_X_min, 1, 1)
        self.scale_layout.addWidget(self.scale_X_max, 1, 2)

        # ajouter les champs de l'axe y
        self.scale_layout.addWidget(QLabel("Y"), 2, 0)
        self.scale_layout.addWidget(self.scale_Y_min, 2, 1)
        self.scale_layout.addWidget(self.scale_Y_max, 2, 2)

        # ajouter les champs de l'axe z
        self.scale_layout.addWidget(QLabel("Z"), 3, 0)
        self.scale_layout.addWidget(self.scale_Z_min, 3, 1)
        self.scale_layout.addWidget(self.scale_Z_max, 3, 2)

        # ajouter le layout au groupe
        self.scale_group.setLayout(self.scale_layout)

        # ajouter le groupe à l'interface principale
        self.interface.addWidget(self.scale_group)