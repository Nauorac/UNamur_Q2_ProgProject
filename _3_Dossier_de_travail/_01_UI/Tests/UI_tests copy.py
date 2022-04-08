import blessed
term = blessed.Terminal()

#y_middle = term.height // 2
#print(term.center (term.move_y(y_middle+7) + term.underline_bold_green(("Please press 'y' or 'n' "))))
with term.cbreak():
    print("Select game mode for player 1 => 0 (Local) OR 1 (Remote) : ")
    val = term.underline + term.inkey()+term.normal
    v
print (val)