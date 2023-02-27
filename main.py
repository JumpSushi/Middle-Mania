def on_button_pressed_a():
    global interval
    if position.get(LedSpriteProperty.X) == 2:
        game.add_score(1)
        interval = max(interval - 50, INTERVAL_MIN)
        music.play_melody("C D E F G A B C5 ", 700)
    else:
        game.game_over()
        music.play_melody("C D E F G A B C5 ", 500)
input.on_button_pressed(Button.A, on_button_pressed_a)

position: game.LedSprite = None
interval = 0
INTERVAL_MIN = 0
# Define constants
INTERVAL_START = 800
INTERVAL_MIN = 400
INTERVAL_MAX = 500
MOVE_SPEED_MIN = -5
MOVE_SPEED_MAX = 5
MOVE_SPEED_DEFAULT = 1
Y_MOVE_MIN = -2
Y_MOVE_MAX = 2
interval = INTERVAL_START
moveSpeed = MOVE_SPEED_DEFAULT
level = 1
depend = randint(1, 3)
game.set_score(0)
basic.show_string(" Press ", 100)
basic.show_string(" A ", 100)
basic.show_string(" when ", 100)
basic.show_string(" in ", 100)
basic.show_string(" the ", 100)
basic.show_string(" middle ", 100)
# Create the initial sprite
position = game.create_sprite(2, 2)
# Move the sprite in the background

def on_in_background():
    while not (game.is_game_over()):
        position.move(randint(MOVE_SPEED_MIN, MOVE_SPEED_MAX))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        position.change(LedSpriteProperty.Y, randint(Y_MOVE_MIN, Y_MOVE_MAX))
        position.if_on_edge_bounce()
        basic.pause(interval)
control.in_background(on_in_background)
