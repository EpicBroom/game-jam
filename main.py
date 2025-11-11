game.splash("Use arrow keys to move")
tiles.set_current_tilemap(tilemap("""
    level1
    """))
MainCharacter = sprites.create(img("""
        . . . . . . . f f f f f . . . .
        . . . . . . f e e e e e f . . .
        . . . . . f e e e d d d d f . .
        . . . . f f e e d f d d f d c .
        . . . f d d e e d f d d f d c .
        . . . c d b e e d d d d e e d c
        . . . c d b e e d d c d d d d c
        . . . . c f e e e d d c c c c c
        . . . . . f f e e e d d d d f .
        . . . . f e e e e f f f f f . .
        f f . f e e e e e e f f . . . .
        f e . f e e f e e f e e f . . .
        f e . f e e e f e e f e e f . .
        f e f f e f b b f b d f d b f .
        f f f f e b d d f d d f d d f .
        . f f f f f f f f f f f f f . .
        """),
    SpriteKind.player)
EvilSnake = sprites.create(img("""
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
    SpriteKind.enemy)
EvilSnakeY = 0
EvilSnakeX = 0
controller.move_sprite(MainCharacter, 100, 100)
scene.camera_follow_sprite(MainCharacter)
tiles.place_on_tile(MainCharacter, tiles.get_tile_location(0, 10))
info.set_life(3)

def on_forever():
    EvilSnake.set_bounce_on_wall(True)
forever(on_forever)

def on_forever2():
    if MainCharacter.tile_kind_at(TileDirection.BOTTOM, sprites.castle.tile_path2):
        info.change_score_by(1)
forever(on_forever2)

def on_forever3():
    global EvilSnakeY, EvilSnakeX
    EvilSnakeY = randint(-30, 30)
    EvilSnakeX = randint(-30, 30)
    EvilSnake.set_velocity(EvilSnakeX, EvilSnakeY)
    pause(randint(100, 5000))
forever(on_forever3)
