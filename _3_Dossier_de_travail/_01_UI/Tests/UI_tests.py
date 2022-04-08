from blessed import Terminal
from math import floor
from socket import timeout
import blessed
term = blessed.Terminal()
import time

"""
test_string = "Hello World!"

print(f"{term.home}{term.clear}")



for i in range(len(test_string)):

   print(""+test_string[i]+""+term.move_x(1))
   time.sleep(0.2)
"""
"""
import sys
blah = "This is written slowly\n"
for l in blah:
   sys.stdout.write(l)
   sys.stdout.flush()
   time.sleep(0.2)

"""

# std imports

# local


def roundxy(x, y):
    return int(floor(x)), int(floor(y))


term = Terminal()

x, y, xs, ys = 2, 2, 0.4, 0.3
with term.cbreak(), term.hidden_cursor():
    # clear the screen
    print(term.home + term.black_on_olivedrab4 + term.clear)

    # loop every 20ms
    while term.inkey(timeout=0.02) != 'q':
        # erase,
        txt_erase = term.move_xy(*roundxy(x, y)) + ' '

        # bounce,
        if x >= (term.width - 1) or x <= 0:
            xs *= -1
        if y >= term.height or y <= 0:
            ys *= -1

        # move,
        x, y = x + xs, y + ys

        # draw !
        txt_ball = term.move_xy(*roundxy(x, y)) + '█'
        print(txt_erase + txt_ball, end='', flush=True)
