function Set_level () {
    while (true) {
        if (input.buttonIsPressed(Button.A)) {
        	
        } else if (input.buttonIsPressed(Button.B)) {
            Level += 1
            basic.showString("" + Level)
        } else if (Level <= 0) {
            Level = 0
        } else if (input.buttonIsPressed(Button.AB)) {
            Position = game.createSprite(2, 2)
            break;
        }
    }
}
input.onButtonPressed(Button.A, function () {
    if (Position.get(LedSpriteProperty.X) == 2) {
        game.addScore(1)
        Intervine = Intervine - 50
    } else {
        game.gameOver()
    }
})
let Intervine = 0
let Level = 0
let Position: game.LedSprite = null
Position = game.createSprite(2, 2)
Level = 1
Intervine = 500
game.setScore(0)
Position.delete()
Set_level()
basic.forever(function () {
    Position.move(1)
    Position.ifOnEdgeBounce()
    basic.pause(Intervine)
})
