import colored

nb_rows = 20
nb_cols = 40

to_display = ''
for row_id in range(nb_rows):
    for col_id in range(nb_cols):
            if (row_id + col_id) % 2 == 0:
                to_display += colored.bg('yellow') + colored.fg('red')
            else:
                to_display += colored.bg('green') + colored.fg('blue')
                
            to_display += '◖◗' + colored.attr('reset')
    
    to_display += '\n'
    
print(to_display)
