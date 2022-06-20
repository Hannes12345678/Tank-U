from gametestmenu import Game
#monke

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()