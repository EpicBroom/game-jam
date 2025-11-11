function defineCharacters () {
    MainCharacter = sprites.create(img`
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
        `, SpriteKind.Player)
    EvilSnake = sprites.create(img`
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
        `, SpriteKind.Enemy)
    EvilSnake.setBounceOnWall(true)
    controller.moveSprite(MainCharacter, 100, 100)
    scene.cameraFollowSprite(MainCharacter)
    tiles.placeOnTile(MainCharacter, tiles.getTileLocation(0, 10))
}
function RewardSystem () {
    if (MainCharacter.tileKindAt(TileDirection.Bottom, sprites.castle.tilePath2)) {
        info.changeScoreBy(1)
        pauseUntil(() => !(MainCharacter.tileKindAt(TileDirection.Bottom, sprites.castle.tilePath2)))
    }
}
function initialiseWorld () {
    game.splash("Use arrow keys to move")
    tiles.setCurrentTilemap(tilemap`level1`)
    music.play(music.stringPlayable("D E F E D E F E ", 188), music.PlaybackMode.LoopingInBackground)
    MainCharacterStatusBar = statusbars.create(60, 10, StatusBarKind.Health)
    MainCharacterStatusBar.setColor(7, 2, 7)
    MainCharacterStatusBar.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
    MainCharacterStatusBar.setBarBorder(1, 15)
    MainCharacterStatusBar.setOffsetPadding(-43, 5)
    MainCharacterStatusBar.positionDirection(CollisionDirection.Bottom)
}
function defineInitialVariables () {
    EvilSnakeY = 0
    EvilSnakeX = 0
}
function makeEvilSnakeMove () {
    EvilSnakeY = randint(-30, 30)
    EvilSnakeX = randint(-30, 30)
    EvilSnake.setVelocity(EvilSnakeX, EvilSnakeY)
    pause(randint(100, 5000))
}
let EvilSnakeX = 0
let EvilSnakeY = 0
let MainCharacterStatusBar: StatusBarSprite = null
let EvilSnake: Sprite = null
let MainCharacter: Sprite = null
initialiseWorld()
defineInitialVariables()
defineCharacters()
forever(function () {
    makeEvilSnakeMove()
})
forever(function () {
    RewardSystem()
})
