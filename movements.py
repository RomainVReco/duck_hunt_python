
def target_movements(dictionnary_of_target, screen, largeur_ecran, FONT_SIZE, hauteur_ecran) -> dict:
    for msg, stats_items in dictionnary_of_target.items():
        screen.blit(msg, stats_items[0])
        rect_temp = stats_items[0]
        speed_temp = stats_items[3]
        rect_temp.x += speed_temp[0]
        rect_temp.y += speed_temp[1]
        if rect_temp.x > largeur_ecran - (FONT_SIZE * 1.5) or rect_temp.x < 0:
            new_speed_x = (speed_temp[0] * -1, speed_temp[1])
            stats_items[3] = new_speed_x
            if stats_items[1] == 0:
                has_bounced_sides = 1
            else:
                has_bounced_sides = 0
            stats_items[1] = has_bounced_sides
            dictionnary_of_target.update({msg: stats_items})
        if rect_temp.y > (hauteur_ecran - (round(hauteur_ecran * 0.15))) or rect_temp.y < 0:
            new_speed_y = (speed_temp[0], speed_temp[1] * -1)
            stats_items[3] = new_speed_y
            if stats_items[2] == 0:
                has_bounced_ceiling = 1
            else:
                has_bounced_ceiling = 0
            stats_items[2] = has_bounced_ceiling
            dictionnary_of_target.update({msg: stats_items})
    return dictionnary_of_target


def decoy_movements(dictionnary_of_decoy, screen, largeur_ecran, FONT_SIZE, hauteur_ecran) -> dict:
    for msg_decoy, stats_items_decoy in dictionnary_of_decoy.items():
        screen.blit(msg_decoy, stats_items_decoy[0])
        rect_temp = stats_items_decoy[0]
        speed_temp = stats_items_decoy[3]
        rect_temp.x += speed_temp[0]
        rect_temp.y += speed_temp[1]
        if rect_temp.x > largeur_ecran - (FONT_SIZE * 1.5) or rect_temp.x < 0:
            new_speed_x = (speed_temp[0] * -1, speed_temp[1])
            stats_items_decoy[3] = new_speed_x
            if stats_items_decoy[1] == 0:
                has_bounced_sides_decoy = 1
            else:
                has_bounced_sides_decoy = 0
            stats_items_decoy[1] = has_bounced_sides_decoy
            dictionnary_of_decoy.update({msg_decoy: stats_items_decoy})
        if rect_temp.y > (hauteur_ecran - (round(hauteur_ecran * 0.15))) or rect_temp.y < 0:
            new_speed_y = (speed_temp[0], speed_temp[1] * -1)
            stats_items_decoy[3] = new_speed_y
            if stats_items_decoy[2] == 0:
                has_bounced_ceiling_decoy = 1
            else:
                has_bounced_ceiling_decoy = 0
            stats_items_decoy[2] = has_bounced_ceiling_decoy
            dictionnary_of_decoy.update({msg_decoy: stats_items_decoy})
    return dictionnary_of_decoy