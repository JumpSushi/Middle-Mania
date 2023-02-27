function Main () {
    if (Position.get(LedSpriteProperty.X) == 2) {
        game.addScore(1)
        Intervine = Intervine - 50
    } else {
        game.gameOver()
    }
}
let Intervine = 0
let Position: game.LedSprite = null
let Level = 0
basic.showString("s")
while (true) {
    if (input.buttonIsPressed(Button.A)) {
        Level += 1
        basic.showString("" + (Level))
    } else if (input.buttonIsPressed(Button.B)) {
        Level += -1
        basic.showString("" + (Level))
    } else if (Level <= 0) {
        Level = 1
    } else if (input.buttonIsPressed(Button.AB)) {
        Main()
        break;
    }
}
Position = game.createSprite(2, 2)
Intervine = 600
basic.forever(function () {
    Position.move(1)
    Position.ifOnEdgeBounce()
    basic.pause(Intervine)
})
