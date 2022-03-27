import blessed
term = blessed.Terminal()

print(f"{term.home}{term.black_on_grey}{term.clear}")
print("press 'y' or 'n' to quit.")
with term.cbreak():
    val = ''
    val = term.inkey(timeout=3)
    while val.lower() != 'y' or val.lower() != 'n':
        if val.lower() == 'y':
            print(f"{term.home}{term.white_on_black}{term.clear}")
            print(f'YES !{term.normal}')
        elif val.lower() == 'n':
            print(f"{term.home}{term.white_on_black}{term.clear}")
            print(f'NO !{term.normal}')
        else:
            val = term.inkey(timeout=3)
