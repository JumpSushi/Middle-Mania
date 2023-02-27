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
let Depend = randint(1, 0)
game.setScore(0)
basic.forever(function () {
    if (Depend == 1) {
        Position.move(randint(-2, 2))
        music.playTone(262, music.beat(BeatFraction.Whole))
        Position.change(LedSpriteProperty.Y, randint(-2, 2))
        music.playTone(262, music.beat(BeatFraction.Whole))
        Position.ifOnEdgeBounce()
        basic.pause(Intervine)
    } else {
        Position.move(1)
        music.playTone(262, music.beat(BeatFraction.Whole))
        Position.change(LedSpriteProperty.Y, randint(-1, 1))
        music.playTone(262, music.beat(BeatFraction.Whole))
        Position.ifOnEdgeBounce()
        basic.pause(Intervine)
    }
})
