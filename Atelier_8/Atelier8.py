import sys
import importlib

sys.path.append(r"C:\Users\ltinivella\repos\NAND403_A26_Ateliers\Cours8")

import ui
importlib.reload(ui)

def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass

    tool_window = ui.RandomAnimationUI()
    tool_window.show()

main()