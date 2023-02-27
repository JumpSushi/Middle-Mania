def Set_level():
    global Level, Position
    while True:
        if input.button_is_pressed(Button.A):
            pass
        elif input.button_is_pressed(Button.B):
            Level += 1
            basic.show_string("" + str(Level))
        elif Level <= 0:
            Level = 0
        elif input.button_is_pressed(Button.AB):
            Position = game.create_sprite(2, 2)
            break

def on_button_pressed_a():
    global Intervine
    if Position.get(LedSpriteProperty.X) == 2:
        game.add_score(1)
        Intervine = Intervine - 50
    else:
        game.game_over()
input.on_button_pressed(Button.A, on_button_pressed_a)

Intervine = 0
Level = 0
Position: game.LedSprite = None
Position = game.create_sprite(2, 2)
Level = 1
Intervine = 500
game.set_score(0)
Position.delete()
Set_level()

def on_forever():
    Position.move(1)
    Position.if_on_edge_bounce()
    basic.pause(Intervine)
basic.forever(on_forever)
