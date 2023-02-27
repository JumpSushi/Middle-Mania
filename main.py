def Main():
    global Intervine
    if Position.get(LedSpriteProperty.X) == 2:
        game.add_score(1)
        Intervine = Intervine - 50
    else:
        game.game_over()
Intervine = 0
Position: game.LedSprite = None
Level = 0
basic.show_string("s")
while True:
    if input.button_is_pressed(Button.A):
        Level += 1
        basic.show_string("" + str((Level)))
    elif input.button_is_pressed(Button.B):
        Level += -1
        basic.show_string("" + str((Level)))
    elif Level <= 0:
        Level = 1
    elif input.button_is_pressed(Button.AB):
        Main()
        break
Position = game.create_sprite(2, 2)
Intervine = 600

def on_forever():
    Position.move(1)
    Position.if_on_edge_bounce()
    basic.pause(Intervine)
basic.forever(on_forever)
