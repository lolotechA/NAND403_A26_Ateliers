
import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QSpinBox,
    QLabel,
    QDoubleSpinBox
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout = QVBoxLayout(self)

        self.x_minimum = QDoubleSpinBox()
        self.x_minimum.setRange(-10000, 10000)
        self.x_minimum.setValue(-10)
        layout.addWidget(QLabel("Position X minimum"))
        layout.addWidget(self.x_minimum)

        self.y_minimum = QDoubleSpinBox()
        self.y_minimum.setRange(-10000, 10000)
        self.y_minimum.setValue(-10)
        layout.addWidget(QLabel("Position Y minimum"))
        layout.addWidget(self.y_minimum)

        self.z_minimum = QDoubleSpinBox()
        self.z_minimum.setRange(-10000, 10000)
        self.z_minimum.setValue(-10)
        layout.addWidget(QLabel("Position Z minimum"))
        layout.addWidget(self.z_minimum)

        self.x_maximum = QDoubleSpinBox()
        self.x_maximum.setRange(-10000, 10000)
        self.x_maximum.setValue(10)
        layout.addWidget(QLabel("Position X maximum"))
        layout.addWidget(self.x_maximum)

        self.y_maximum = QDoubleSpinBox()
        self.y_maximum.setRange(-10000, 10000)
        self.y_maximum.setValue(10)
        layout.addWidget(QLabel("Position Y maximum"))
        layout.addWidget(self.y_maximum)

        self.z_maximum = QDoubleSpinBox()
        self.z_maximum.setRange(-10000, 10000)
        self.z_maximum.setValue(10)
        layout.addWidget(QLabel("Position Z maximum"))
        layout.addWidget(self.z_maximum)

        self.number_label = QLabel("Number of objects")
        layout.addWidget(self.number_label)

        self.number_input = QSpinBox()
        self.number_input.setRange(1, 800)
        self.number_input.setValue(20)
        layout.addWidget(self.number_input)

        self.scale_minimum = QDoubleSpinBox()
        self.scale_minimum.setRange(0.1, 100)
        self.scale_minimum.setValue(0.5)
        layout.addWidget(QLabel("Scale minimum"))
        layout.addWidget(self.scale_minimum)

        self.scale_maximum = QDoubleSpinBox()
        self.scale_maximum.setRange(0.1, 100)
        self.scale_maximum.setValue(2)
        layout.addWidget(QLabel("Scale maximum"))
        layout.addWidget(self.scale_maximum)


        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    def create_object(self):
        number = self.number_input.value()

        for i in range(number):
            forme = random.choice(["cube", "cylindre", "sphere"])
        
            if forme == "cube":
                objet = cmds.polyCube()[0]
            elif forme == "cylindre":
                objet = cmds.polyCylinder()[0]
            else:
                objet = cmds.polySphere()[0]

            x = random.uniform(self.x_minimum.value(), self.x_maximum.value())
            y = random.uniform(self.y_minimum.value(), self.y_maximum.value())
            z = random.uniform(self.z_minimum.value(), self.z_maximum.value())

            cmds.move(x, y, z, objet)
            scale = random.uniform(self.scale_minimum.value(), self.scale_maximum.value())
            cmds.scale(scale, scale, scale, objet)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()
