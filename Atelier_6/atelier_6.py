import maya.cmds as cmds

for i in range(6):
    cmds.polyCube()
    cmds.move(i * 3, 0, 0)
    cmds.scale(0.2, 2, 0.2)

for i in range(2):
    cmds.polyCube()
    cmds.move(7.5, i, 0)
    cmds.scale(15, 0.1, 0.1)