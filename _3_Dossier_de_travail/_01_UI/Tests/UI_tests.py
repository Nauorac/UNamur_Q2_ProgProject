import blessed
term = blessed.Terminal()

print(f"{term.home}{term.clear}")

"""print(term.underline_bold_green('They live! In sewers!'))
print(term.home + term.clear, end='')
print(term.move_down(2) + term.move_right(20) + term.bright_red('fire!'), end='')
print(term.move_xy(20, 7) + term.bold('Direct hit!'), end='')
print(term.move_y(term.height - 3), end='')
"""

print("press 'y' or 'n' to quit.")
with term.cbreak():
   y_middle = term.height // 2
   #x_middle = term.width // 2
   val = ''
   blink = 0
   while val.lower() != 'y' or val.lower() != 'n':
      val = term.inkey(timeout=5)
      print(blink)
      while not val:
         val = term.inkey(timeout=0.5)
         if blink ==1:
            print(term.center (term.move_y(y_middle+7) + term.underline_bold_green(("Please press 'y' or 'n' "))))
            blink -= 1
         else:
            print(term.move_y(y_middle+6) + term.clear_eos)
            blink += 1
      if val.lower() == 'y':
         print(f"{term.home}{term.clear}")
         game_settings(P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type)
      elif val.lower() == 'n':
         game_loop(game_turn, orders_P1, orders_P2,
                   P1_game_mode, P2_game_mode, P1_type, P2_type)


"""

print(f"blessed {term.link('https://blessed.readthedocs.org', 'documentation')}")
blessed documentation

   val =""
while val.lower() != 'y' or val.lower() != 'n':
   if not val:
      print("It sure is quiet in here ...")
   elif val.lower() == 'y':
      print(f"{term.home}{term.white_on_black}{term.clear}")
      print(f'YES !{term.normal}')
   elif val.lower() == 'n':
      print(f"{term.home}{term.white_on_black}{term.clear}")
      print(f'NO !{term.normal}')
   else:
      val = term.inkey(timeout=300000)
"""