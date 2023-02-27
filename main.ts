input.onButtonPressed(Button.A, function () {
    if (position.get(LedSpriteProperty.X) == 2) {
        game.addScore(1)
        interval = Math.max(interval - 50, INTERVAL_MIN)
        music.playMelody("C D E F G A B C5 ", 700)
    } else {
        game.gameOver()
        music.playMelody("C D E F G A B C5 ", 500)
    }
})
let position: game.LedSprite = null
let interval = 0
let INTERVAL_MIN = 0
// Define constants
let INTERVAL_START = 800
INTERVAL_MIN = 400
let INTERVAL_MAX = 500
let MOVE_SPEED_MIN = -5
let MOVE_SPEED_MAX = 5
let MOVE_SPEED_DEFAULT = 1
let Y_MOVE_MIN = -2
let Y_MOVE_MAX = 2
interval = INTERVAL_START
let moveSpeed = MOVE_SPEED_DEFAULT
let level = 1
let depend = randint(1, 3)
game.setScore(0)
basic.showString(" Press ", 100)
basic.showString(" A ", 100)
basic.showString(" when ", 100)
basic.showString(" in ", 100)
basic.showString(" the ", 100)
basic.showString(" middle ", 100)
// Create the initial sprite
position = game.createSprite(2, 2)
// Move the sprite in the background
control.inBackground(function () {
    while (!(game.isGameOver())) {
        position.move(randint(MOVE_SPEED_MIN, MOVE_SPEED_MAX))
        music.playTone(262, music.beat(BeatFraction.Whole))
        position.change(LedSpriteProperty.Y, randint(Y_MOVE_MIN, Y_MOVE_MAX))
        position.ifOnEdgeBounce()
        basic.pause(interval)
    }
})
