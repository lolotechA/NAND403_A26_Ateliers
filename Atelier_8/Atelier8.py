import sys
import importlib

from PySide6.QtWidgets import (
    QWidget,
    QTextEdit,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMessageBox
)

sys.path.append(r"C:\Users\ltinivella\repos\NAND403_A26_Ateliers\Cours8")


class RandomAnimationUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Animation Tool Edit")
        self.setMinimumWidth(400)
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)

        title = QLabel("Message Board edit")
        layout.addWidget(title)

        self.text_input = QTextEdit("Enter a message")
        layout.addWidget(self.text_input)

        show_button = QPushButton("show message")
        show_button.clicked.connect(self.show_message)
        layout.addWidget(show_button)

    def show_message(self):
        QMessageBox.information(self, "Message", self.text_input.toPlainText())


def main():
    global tool_window

    try:
        tool_window.close()
    except Exception:
        pass

    tool_window = RandomAnimationUI()
    tool_window.show()


main()