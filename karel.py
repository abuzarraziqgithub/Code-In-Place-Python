from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    first_row()
    jump()
    first_row()
    jump()
    first_row()
    jump()
    first_row()
    jump()
    first_row()
    put_beeper()
# first row
def first_row():
    while front_is_clear():
        move()
        put_beeper()
    turn_around()
    while front_is_clear():
        move()
# jump to the next row
def jump():
    if front_is_blocked():
        turn_around()
        turn_left()
        put_beeper()
        move()
        turn_around()
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()