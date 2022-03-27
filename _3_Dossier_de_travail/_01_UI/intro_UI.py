
import blessed
term = blessed.Terminal()

def welcome_screen():
      with term.fullscreen(), term.cbreak():
            y_middle = term.height // 2
            print(term.move_y(y_middle-5) + term.center(" *-* ALPHA & OMEGA *-*").rstrip())
            print(term.move_y(y_middle-3) + term.center("by group 20").rstrip())
            print(term.move_y(y_middle-2) + term.center("--------------------").rstrip())
            print(term.move_y(y_middle+1) + term.center('').rstrip())
            print(term.move_y(y_middle+1) + term.center ('Press any key to start !').rstrip())
            print(term.move_y(y_middle+1) + term.center('').rstrip())
            print(term.move_y(y_middle+10) + term.center("William Auspert - Sébastien Baudoux - Aleksander Besler - Trésor Tientcheu").rstrip())
            term.inkey()



def settings():
    with term.fullscreen(), term.cbreak():
      y_middle = term.height // 2
      print(term.move_y(y_middle-3) + term.center(" * 🎮 * Default game settings * 🎮 *").rstrip())
      print(term.move_y(y_middle-2) + term.center("-------------------------------------").rstrip())
      print(term.move_y(y_middle+1) + term.center("       Player 1       ||          Player 2  ").rstrip())
      print(term.move_y(y_middle+2) + term.center("Local (💻) - Human (👤)   ||  Remote (🖧 ) - A.I. (🤖)").rstrip())
      print(term.move_y(y_middle+4) + term.center("Would you like to change it ?").rstrip())
      print(term.move_y(y_middle+5) + term.center(("Press y(es) or n(o)")).rstrip())
      val = term.inkey()
      while val != "y" or val != "n":
          settings()
      if val == "y":
            print("YES")
            #game_settings(P1_game_mode, P2_game_mode, group_1, group_2, P1_type, P2_type)
      else:
            print("NO")
            #game_loop(game_turn, orders_P1, orders_P2, P1_game_mode, P2_game_mode, P1_type, P2_type)


#welcome_screen()
settings()
