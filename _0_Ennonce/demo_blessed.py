import blessed, random, time
term = blessed.Terminal()

# clear screen and hide cursor
print(term.home + term.clear + term.hide_cursor)

# define position of the symbol
row = int(term.height/2)
col = int(term.width/2)

# move cursor + change color of symbol + change color of background + symbol + back to normal
print(term.move_yx(row, col) + term.red + term.on_rosybrown2 + '●' + term.normal, end='', flush=True)

# move symbol forever
while True:
    # wait a fraction of second
    time.sleep(0.5)


    # move cursor + change color of symbol + change color of background + single space + back to normal
    print(term.move_yx(row, col) + term.on_skyblue + ' ' + term.normal, end='', flush=True)

    # update position symbol
    move = random.choice(((-1, 0), (1, 0), (0, -1), (0, 1)))

    row += move[0]
    if row < 0:
        row = 0
    if row >= term.height:
        row = term.height-1

    col += move[1]
    if col < 0:
        col = 0
    if col >= term.width:
        col = term.width-1
    
    # move cursor + change color of symbol + change color of background + symbol + back to normal
    print(term.move_yx(row, col) + term.red + term.on_rosybrown2 + '●' + term.normal, end='',)