# importer random pour générer des valeurs aléatoires
import random

# importer les commandes de maya
from maya import cmds


# fonction pour générer l'animation
def generate_animation(ui):

    # récupérer les objets sélectionnés dans maya
    objects = cmds.ls(selection=True)

    # si aucun objet n'est sélectionné, arrêter la fonction
    if not objects:
        return

    # récupérer la durée et le step depuis l'interface
    duration = ui.duration_nb.value()
    step = ui.step_nb.value()

    # commencer un groupe undo pour pouvoir annuler la génération
    cmds.undoInfo(openChunk=True)

    # parcourir chaque objet sélectionné
    for obj in objects:

        # parcourir les frames selon la durée et le step
        for frame in range(0, duration + 1, step):

            # changer le temps actuel dans maya
            cmds.currentTime(frame)

            # générer des valeurs aléatoires pour la translation
            x = random.uniform(ui.translation_X_min.value(), ui.translation_X_max.value())
            y = random.uniform(ui.translation_Y_min.value(), ui.translation_Y_max.value())
            z = random.uniform(ui.translation_Z_min.value(), ui.translation_Z_max.value())

            # générer des valeurs aléatoires pour la rotation
            rx = random.uniform(ui.rotate_X_min.value(), ui.rotate_X_max.value())
            ry = random.uniform(ui.rotate_Y_min.value(), ui.rotate_Y_max.value())
            rz = random.uniform(ui.rotate_Z_min.value(), ui.rotate_Z_max.value())

            # générer des valeurs aléatoires pour le scale
            sx = random.uniform(ui.scale_X_min.value(), ui.scale_X_max.value())
            sy = random.uniform(ui.scale_Y_min.value(), ui.scale_Y_max.value())
            sz = random.uniform(ui.scale_Z_min.value(), ui.scale_Z_max.value())

            # sauvegarder les premières valeurs de l'animation
            if frame == 0:
                first_x = x
                first_y = y
                first_z = z

                first_rx = rx
                first_ry = ry
                first_rz = rz

                first_sx = sx
                first_sy = sy
                first_sz = sz

            # remettre les premières valeurs à la dernière frame
            if frame == duration:
                x = first_x
                y = first_y
                z = first_z

                rx = first_rx
                ry = first_ry
                rz = first_rz

                sx = first_sx
                sy = first_sy
                sz = first_sz

            # appliquer la translation à l'objet
            cmds.setAttr(obj + ".translateX", x)
            cmds.setAttr(obj + ".translateY", y)
            cmds.setAttr(obj + ".translateZ", z)

            # appliquer la rotation à l'objet
            cmds.setAttr(obj + ".rotateX", rx)
            cmds.setAttr(obj + ".rotateY", ry)
            cmds.setAttr(obj + ".rotateZ", rz)

            # appliquer le scale à l'objet
            cmds.setAttr(obj + ".scaleX", sx)
            cmds.setAttr(obj + ".scaleY", sy)
            cmds.setAttr(obj + ".scaleZ", sz)

            # créer les keyframes pour la translation
            cmds.setKeyframe(obj, attribute="translateX")
            cmds.setKeyframe(obj, attribute="translateY")
            cmds.setKeyframe(obj, attribute="translateZ")

            # créer les keyframes pour la rotation
            cmds.setKeyframe(obj, attribute="rotateX")
            cmds.setKeyframe(obj, attribute="rotateY")
            cmds.setKeyframe(obj, attribute="rotateZ")

            # créer les keyframes pour le scale
            cmds.setKeyframe(obj, attribute="scaleX")
            cmds.setKeyframe(obj, attribute="scaleY")
            cmds.setKeyframe(obj, attribute="scaleZ")

    # terminer le groupe undo
    cmds.undoInfo(closeChunk=True)