namespace SpriteKind {
    export const Zombie_1 = SpriteKind.create()
    export const Zombie_2 = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Zombie_1, SpriteKind.Player, function (sprite3, otherSprite3) {
    sprites.destroy(Zombie)
    sprites.destroy(projectile)
    Restart_monstre = 1
    info.changeScoreBy(1)
})
info.onCountdownEnd(function () {
    effects.clouds.startScreenEffect()
    game.setGameOverMessage(false, "MORT")
    effects.clouds.endScreenEffect()
})
sprites.onOverlap(SpriteKind.Zombie_2, SpriteKind.Player, function (sprite, otherSprite) {
    Healthbarsurvivor.value += -10
    pause(500)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, Survivant, 50, 50)
    music.play(music.createSoundEffect(WaveShape.Square, 1600, 1, 255, 0, 300, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.InBackground)
    pause(1000)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Zombie_1, function (sprite2, otherSprite2) {
    sprites.destroy(projectile)
    Healthbarzombie.value += -10
    Restart_monstre = 0
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Zombie_2, function (sprite22, otherSprite22) {
    sprites.destroy(zombie1)
    sprites.destroy(projectile)
    restart_zombi_2 = 1
    info.changeScoreBy(2)
})
info.onScore(50, function () {
    effects.confetti.startScreenEffect()
    effects.confetti.endScreenEffect()
    game.setGameOverMessage(true, "ZOMBIE ÉRADIQUÉ")
    game.gameOver(true)
})
let restart_zombi_2 = 0
let zombie1: Sprite = null
let Healthbarzombie: StatusBarSprite = null
let Restart_monstre = 0
let projectile: Sprite = null
let Zombie: Sprite = null
let Healthbarsurvivor: StatusBarSprite = null
let Survivant: Sprite = null
info.setScore(0)
tiles.setCurrentTilemap(tilemap`niveau1`)
Survivant = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(Survivant)
scene.cameraFollowSprite(Survivant)
Healthbarsurvivor = statusbars.create(20, 4, StatusBarKind.Health)
Healthbarsurvivor.value = 100
Healthbarsurvivor.attachToSprite(Survivant)
Healthbarsurvivor.setColor(7, 2)
Healthbarsurvivor.setLabel("HP")
game.showLongText("VAGUE 1", DialogLayout.Full)
pause(5000)
Zombie = sprites.create(img`
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
    `, SpriteKind.Zombie_1)
Zombie.follow(Survivant, 40)
info.startCountdown(180)
forever(function () {
    if (info.score() == 10) {
        if (Restart_monstre == 1) {
            game.showLongText("VAGUE 2", DialogLayout.Bottom)
            Restart_monstre = 0
            Zombie = sprites.create(img`
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
                `, SpriteKind.Zombie_1)
            Zombie.follow(Survivant, 35)
            pause(1000)
            zombie1 = sprites.create(img`
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
                `, SpriteKind.Zombie_2)
            zombie1.follow(Survivant, 35)
        }
    } else if (Restart_monstre == 1) {
        Restart_monstre = 0
        Zombie = sprites.create(img`
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
            `, SpriteKind.Zombie_1)
        Zombie.follow(Survivant, 35)
    } else if (restart_zombi_2 == 1) {
        restart_zombi_2 = 0
        zombie1 = sprites.create(img`
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
            `, SpriteKind.Zombie_2)
        zombie1.follow(Survivant, 35)
    }
})
forever(function () {
    if (Healthbarsurvivor.value == 0) {
        game.setGameOverMessage(false, "GAME OVER!")
        game.gameOver(false)
    }
    if (Healthbarzombie.value == 0) {
        Restart_monstre = 1
    }
})
game.onUpdateInterval(500, function () {
	
})
