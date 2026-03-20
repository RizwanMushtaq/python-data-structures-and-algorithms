top_games = ["footbal", "hocky", "vollyball"]
# This is not correct way to copy lists, its just assigning my_games, the reference of the orignal list
my_games = top_games
my_games.append("beach vollyball")
print(f"top games are {top_games} but my games are {my_games}")

# To create a new list, we need to use slice and copy complete list as
top_games = ["footbal", "hocky", "vollyball"]
my_games = top_games[:]
my_games.append("beach vollyball")
print(f"top games are {top_games} but my games are {my_games}")
