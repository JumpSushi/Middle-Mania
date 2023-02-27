input.onButtonPressed(Button.A, function () {
    if (Position.get(LedSpriteProperty.X) == 2) {
        game.addScore(1)
        Intervine = Intervine - 50
    } else {
        game.gameOver()
    }
})
let Intervine = 0
let Position: game.LedSprite = null
Position = game.createSprite(2, 2)
let Level = 1
Intervine = randint(400, 500)
game.setScore(0)
basic.forever(function () {
    Position.move(1)
    Position.ifOnEdgeBounce()
    basic.pause(Intervine)
})
