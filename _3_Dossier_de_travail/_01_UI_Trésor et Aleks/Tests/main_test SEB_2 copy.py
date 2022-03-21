import blessed
term = blessed.Terminal()

with term.fullscreen(), term.cbreak():
    print(term.move_y(term.height // 2) +
          term.center('press any key').rstrip())
    term.inkey()
