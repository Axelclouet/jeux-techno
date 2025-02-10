@namespace
class SpriteKind:
    Zombie_1 = SpriteKind.create()
    Zombie_2 = SpriteKind.create()

def on_countdown_end():
    effects.clouds.start_screen_effect()
    game.set_game_over_message(False, "MORT")
    effects.clouds.end_screen_effect()
info.on_countdown_end(on_countdown_end)

def on_on_overlap(sprite, otherSprite):
    Healthbarsurvivor.value += -10
    pause(500)
sprites.on_overlap(SpriteKind.Zombie_2, SpriteKind.player, on_on_overlap)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . 2 2 2 2 . . .
                    . . . . . . . 2 2 1 1 1 1 2 . .
                    . . . . 2 2 3 3 1 1 1 1 1 1 . .
                    . . 3 3 3 3 1 1 1 1 1 1 1 1 . .
                    . . 1 1 1 1 1 1 1 1 1 1 1 1 . .
                    . . 3 3 2 2 3 1 1 1 1 1 1 1 . .
                    . . . . . . 2 2 3 1 1 1 1 2 . .
                    . . . . . . . . . 2 2 2 2 . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
        """),
        Survivant,
        50,
        50)
    music.play(music.create_sound_effect(WaveShape.SQUARE,
            1600,
            1,
            255,
            0,
            300,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        music.PlaybackMode.IN_BACKGROUND)
    pause(1000)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    global Restart_monstre
    sprites.destroy(projectile)
    Healthbarzombie.value += -10
    Restart_monstre = 0
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Zombie_1, on_on_overlap2)

def on_on_overlap3(sprite22, otherSprite22):
    global restart_zombi_2
    sprites.destroy(zombie1)
    sprites.destroy(projectile)
    restart_zombi_2 = 1
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Zombie_2, on_on_overlap3)

def on_on_score():
    effects.confetti.start_screen_effect()
    effects.confetti.end_screen_effect()
    game.set_game_over_message(True, "ZOMBIE ÉRADIQUÉ")
    game.game_over(True)
info.on_score(50, on_on_score)

def on_on_overlap4(sprite3, otherSprite3):
    Healthbarsurvivor.value += -10
    pause(500)
sprites.on_overlap(SpriteKind.Zombie_1, SpriteKind.player, on_on_overlap4)

restart_zombi_2 = 0
zombie1: Sprite = None
Restart_monstre = 0
projectile: Sprite = None
Healthbarzombie: StatusBarSprite = None
Healthbarsurvivor: StatusBarSprite = None
Survivant: Sprite = None
info.set_score(0)
tiles.set_current_tilemap(tilemap("""
    niveau10
"""))
Survivant = sprites.create(img("""
        ....ffff.................
            ..ffffffff...............
            .ffffffcfff..............
            ffffffccfffc.............
            fffcfffffffc.............
            cccfffeeffcc.............
            fffffeeffccf.............
            fffbfeefbfff5............
            .f41f44f14f55............
            .fe444444ef55............
            .fffeeeefff55............
            fefb7777bfef5............
            e4f777777f4e.............
            eef666666feef............
            ...ffffff..ff............
            ...ff..ff...f............
            ............f............
            .........................
            .........................
            .........................
            .........................
            .........................
            .........................
            .........................
            .........................
    """),
    SpriteKind.player)
controller.move_sprite(Survivant)
Healthbarsurvivor = statusbars.create(20, 4, StatusBarKind.health)
Healthbarsurvivor.value = 100
Healthbarsurvivor.attach_to_sprite(Survivant)
Healthbarsurvivor.set_color(7, 2)
Healthbarsurvivor.set_label("HP")
scene.camera_follow_sprite(Survivant)
game.show_long_text("VAGUE 1", DialogLayout.FULL)
pause(5000)
Zombie = sprites.create(img("""
        . . . . c c c c c c . . . . . .
            . . . c 6 7 7 7 7 6 c . . . . .
            . . c 7 7 7 7 7 7 7 7 c . . . .
            . c 6 7 7 7 7 7 7 7 7 6 c . . .
            . c 7 c 6 6 6 6 c 7 7 7 c . . .
            . f 7 6 f 6 6 f 6 7 7 7 f . . .
            . f 7 7 7 7 7 7 7 7 7 7 f . . .
            . . f 7 7 7 7 6 c 7 7 6 f c . .
            . . . f c c c c 7 7 6 f 7 7 c .
            . . c 7 2 7 7 7 6 c f 7 7 7 7 c
            . c 7 7 2 7 7 c f c 6 7 7 6 c c
            c 1 1 1 1 7 6 f c c 6 6 6 c . .
            f 1 1 1 1 1 6 6 c 6 6 6 6 f . .
            f 6 1 1 1 1 1 6 6 6 6 6 c f . .
            . f 6 1 1 1 1 1 1 6 6 6 f . . .
            . . c c c c c c c c c f . . . .
    """),
    SpriteKind.Zombie_1)
Zombie.follow(Survivant, 35)
info.start_countdown(180)
Healthbarzombie = statusbars.create(20, 4, StatusBarKind.health)
Healthbarzombie.attach_to_sprite(Zombie)
Healthbarzombie.max = 20
Healthbarzombie.value = 20
Healthbarzombie.set_color(2, 7)
Healthbarzombie.set_label("INFECTION", 2)

def on_forever():
    global Restart_monstre, Zombie, zombie1, restart_zombi_2
    if info.score() == 10:
        if Restart_monstre == 1:
            game.show_long_text("VAGUE 2", DialogLayout.BOTTOM)
            Restart_monstre = 0
            Zombie = sprites.create(img("""
                    . . . . c c c c c c . . . . . .
                                    . . . c 6 7 7 7 7 6 c . . . . .
                                    . . c 7 7 7 7 7 7 7 7 c . . . .
                                    . c 6 7 7 7 7 7 7 7 7 6 c . . .
                                    . c 7 c 6 6 6 6 c 7 7 7 c . . .
                                    . f 7 6 f 6 6 f 6 7 7 7 f . . .
                                    . f 7 7 7 7 7 7 7 7 7 7 f . . .
                                    . . f 7 7 7 7 6 c 7 7 6 f c . .
                                    . . . f c c c c 7 7 6 f 7 7 c .
                                    . . c 7 2 7 7 7 6 c f 7 7 7 7 c
                                    . c 7 7 2 7 7 c f c 6 7 7 6 c c
                                    c 1 1 1 1 7 6 f c c 6 6 6 c . .
                                    f 1 1 1 1 1 6 6 c 6 6 6 6 f . .
                                    f 6 1 1 1 1 1 6 6 6 6 6 c f . .
                                    . f 6 1 1 1 1 1 1 6 6 6 f . . .
                                    . . c c c c c c c c c f . . . .
                """),
                SpriteKind.Zombie_1)
            Zombie.follow(Survivant, 35)
            pause(1000)
            zombie1 = sprites.create(img("""
                    . . . . c c c c c c . . . . . .
                                    . . . c 6 7 7 7 7 6 c . . . . .
                                    . . c 7 7 7 7 7 7 7 7 c . . . .
                                    . c 6 7 7 7 7 7 7 7 7 6 c . . .
                                    . c 7 c 6 6 6 6 c 7 7 7 c . . .
                                    . f 7 6 f 6 6 f 6 7 7 7 f . . .
                                    . f 7 7 7 7 7 7 7 7 7 7 f . . .
                                    . . f 7 7 7 7 6 c 7 7 6 f c . .
                                    . . . f c c c c 7 7 6 f 7 7 c .
                                    . . c 7 2 7 7 7 6 c f 7 7 7 7 c
                                    . c 7 7 2 7 7 c f c 6 7 7 6 c c
                                    c 1 1 1 1 7 6 f c c 6 6 6 c . .
                                    f 1 1 1 1 1 6 6 c 6 6 6 6 f . .
                                    f 6 1 1 1 1 1 6 6 6 6 6 c f . .
                                    . f 6 1 1 1 1 1 1 6 6 6 f . . .
                                    . . c c c c c c c c c f . . . .
                """),
                SpriteKind.Zombie_2)
            zombie1.follow(Survivant, 35)
    elif Restart_monstre == 1:
        Restart_monstre = 0
        Zombie = sprites.create(img("""
                . . . . c c c c c c . . . . . .
                            . . . c 6 7 7 7 7 6 c . . . . .
                            . . c 7 7 7 7 7 7 7 7 c . . . .
                            . c 6 7 7 7 7 7 7 7 7 6 c . . .
                            . c 7 c 6 6 6 6 c 7 7 7 c . . .
                            . f 7 6 f 6 6 f 6 7 7 7 f . . .
                            . f 7 7 7 7 7 7 7 7 7 7 f . . .
                            . . f 7 7 7 7 6 c 7 7 6 f c . .
                            . . . f c c c c 7 7 6 f 7 7 c .
                            . . c 7 2 7 7 7 6 c f 7 7 7 7 c
                            . c 7 7 2 7 7 c f c 6 7 7 6 c c
                            c 1 1 1 1 7 6 f c c 6 6 6 c . .
                            f 1 1 1 1 1 6 6 c 6 6 6 6 f . .
                            f 6 1 1 1 1 1 6 6 6 6 6 c f . .
                            . f 6 1 1 1 1 1 1 6 6 6 f . . .
                            . . c c c c c c c c c f . . . .
            """),
            SpriteKind.Zombie_1)
        Zombie.follow(Survivant, 35)
    elif restart_zombi_2 == 1:
        restart_zombi_2 = 0
        zombie1 = sprites.create(img("""
                . . . . c c c c c c . . . . . .
                            . . . c 6 7 7 7 7 6 c . . . . .
                            . . c 7 7 7 7 7 7 7 7 c . . . .
                            . c 6 7 7 7 7 7 7 7 7 6 c . . .
                            . c 7 c 6 6 6 6 c 7 7 7 c . . .
                            . f 7 6 f 6 6 f 6 7 7 7 f . . .
                            . f 7 7 7 7 7 7 7 7 7 7 f . . .
                            . . f 7 7 7 7 6 c 7 7 6 f c . .
                            . . . f c c c c 7 7 6 f 7 7 c .
                            . . c 7 2 7 7 7 6 c f 7 7 7 7 c
                            . c 7 7 2 7 7 c f c 6 7 7 6 c c
                            c 1 1 1 1 7 6 f c c 6 6 6 c . .
                            f 1 1 1 1 1 6 6 c 6 6 6 6 f . .
                            f 6 1 1 1 1 1 6 6 6 6 6 c f . .
                            . f 6 1 1 1 1 1 1 6 6 6 f . . .
                            . . c c c c c c c c c f . . . .
            """),
            SpriteKind.Zombie_2)
        zombie1.follow(Survivant, 35)
forever(on_forever)

def on_forever2():
    global Restart_monstre
    if Healthbarsurvivor.value == 0:
        game.set_game_over_message(False, "GAME OVER!")
        game.game_over(False)
    if Healthbarzombie.value == 0:
        Restart_monstre = 1
forever(on_forever2)

def on_update_interval():
    pass
game.on_update_interval(500, on_update_interval)

