input.onButtonPressed(Button.A, function () {
    if (target.get(LedSpriteProperty.X) == 2) {
        score += 1
        music.playTone(262, music.beat(BeatFraction.Half))
        if (score % 5 == 0) {
            level += 1
            interval += 0 - 50
            targetSpeed += 0 - 50
        }
    } else {
        game.gameOver()
        music.playTone(131, music.beat(BeatFraction.Half))
    }
})
function resetTarget () {
    target = game.createSprite(randint(0, 4), randint(0, 4))
    targetSpeed = 500 - level * 50
    targetBehavior = randint(1, 3)
    pause(5000)
target.set(LedSpriteProperty.X, 2)
}
function updateTarget () {
    switch (targetBehavior) {
        case 1:
            target.move(1)
            break
        case 2:
            target.move(-1)
            break
        case 3:
            target.move(1)
            break
        case 4:
            target.move(-1)
            break
    }
target.ifOnEdgeBounce()
}
let score = 0
let targetBehavior = 0
let targetSpeed = 0
let level = 0
let target: game.LedSprite = null
level = 1
let interval = 500
targetSpeed = 500
targetBehavior = 1
resetTarget()
basic.forever(function () {
    updateTarget()
    if (target.get(LedSpriteProperty.X) != 2) {
        targetSpeed = 500 - level * 50
        targetBehavior = randint(1, 3)
    }
    basic.pause(targetSpeed)
    if (target.get(LedSpriteProperty.X) == 2) {
        resetTarget()
    }
})
