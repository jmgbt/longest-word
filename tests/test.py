from longest_word.game import Game

game = Game()
print(game.grid) # --> OQUWRBAZE
my_word = "BAROQUE"
print(game.is_valid(my_word)) # --> True
