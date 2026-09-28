from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextEdit, QPushButton, QMessageBox

class MessageBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message board")
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message board")
        layout.addWidget(label)

        self.boite_texte = QTextEdit()
        layout.addWidget(self.boite_texte)

        self.bouton = QPushButton("Envoyer")
        self.bouton.clicked.connect(self.on_click)
        layout.addWidget(self.bouton)

    def on_click(self):
        print("on click called")
        message = self.boite_texte.toPlainText()
        boite = QMessageBox()
        boite.setWindowTitle("Message")
        boite.setText(message)
        boite.exec()

def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()

main()