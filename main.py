def defineCharacters():
    global MainCharacter, EvilSnake
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
    EvilSnake.set_bounce_on_wall(True)
    controller.move_sprite(MainCharacter, 100, 100)
    scene.camera_follow_sprite(MainCharacter)
    tiles.place_on_tile(MainCharacter, tiles.get_tile_location(0, 10))
def RewardSystem():
    if MainCharacter.tile_kind_at(TileDirection.BOTTOM, sprites.castle.tile_path2):
        info.change_score_by(1)
        
        def on_pause_until():
            pass
        pause_until(on_pause_until)
        
def initialiseWorld():
    global MainCharacterStatusBar
    game.splash("Use arrow keys to move")
    tiles.set_current_tilemap(tilemap("""
        level1
        """))
    music.play(music.string_playable("D E F E D E F E ", 188),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    MainCharacterStatusBar = statusbars.create(60, 10, StatusBarKind.health)
    MainCharacterStatusBar.set_color(7, 2, 7)
    MainCharacterStatusBar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
    MainCharacterStatusBar.set_bar_border(1, 15)
    MainCharacterStatusBar.set_offset_padding(-43, 5)
    MainCharacterStatusBar.position_direction(CollisionDirection.BOTTOM)

def on_on_zero(status):
    game.game_over(False)
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def defineInitialVariables():
    global EvilSnakeY, EvilSnakeX
    EvilSnakeY = 0
    EvilSnakeX = 0
def makeEvilSnakeMove():
    global EvilSnakeY, EvilSnakeX
    EvilSnakeY = randint(-30, 30)
    EvilSnakeX = randint(-30, 30)
    EvilSnake.set_velocity(EvilSnakeX, EvilSnakeY)
    pause(randint(100, 5000))

def on_on_overlap(sprite, otherSprite):
    MainCharacterStatusBar.value += -12.5
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

EvilSnakeX = 0
EvilSnakeY = 0
MainCharacterStatusBar: StatusBarSprite = None
EvilSnake: Sprite = None
MainCharacter: Sprite = None
initialiseWorld()
defineInitialVariables()
defineCharacters()

def on_forever():
    makeEvilSnakeMove()
    RewardSystem()
forever(on_forever)
