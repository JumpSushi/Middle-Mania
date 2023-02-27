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
let Level: string = 1
Intervine = randint(400, 500)
game.setScore(0)
basic.forever(function () {
    if (Level == "") {
        Position.move(randint(-2, 2))
        Position.change(LedSpriteProperty.Y, randint(-2, 2))
        Position.ifOnEdgeBounce()
        basic.pause(Intervine)
    } else {
        Position.move(1)
        Position.change(LedSpriteProperty.Y, 1)
        Position.ifOnEdgeBounce()
        basic.pause(Intervine)
    }
})
