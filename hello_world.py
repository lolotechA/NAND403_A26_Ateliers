import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget

# 1. Create the QApplication instance
app = QApplication(sys.argv)

# 2. Create a basic window (QWidget)
window = QWidget()
window.setWindowTitle("Basic PySide6 Window")
window.resize(400, 300)

# 3. Add an optional label to display text inside the window
label = QLabel("Hello, PySide6!", window)
label.move(150, 130)

# 4. Make the window visible on the screen
window.show()

# 5. Start the Qt event loop
sys.exit(app.exec())