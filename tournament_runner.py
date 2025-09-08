class tournament:
#includes info about tournament 
    def __init__(self,name, start, end, location, money):
        self.name = name
        self.start = start
        self.end = end
        self.location = location
        self.money = money
        self.list_of_players = []
        self.list_of_matches = []

    def join_tournament(self, player):#to add new player to the tournament.
        self.list_of_players.append(player)

    def add_match(self, match_obj):#to add a match to the tournament.
        self.list_of_matches.append(match_obj)

    def print_tournament_info(self):#prints all the info regarding the tournament.
        print("Name: ", self.name)
        print("Starts: ", self.start)
        print("Ends: ", self.end)
        print("Location: ", self.location)

        print("players:")
        for player in self.list_of_players:
            player.print_info()
        print("Matches")
        for match in self.list_of_matches:
            match.print_match_info()

class match:
    #includes info about match
    def __init__(self,date, player1, player2):
        self.date = date
        self.player1 = player1
        self.player2 = player2
        self.winner = None
    
    def set_winner(self, winner):
        if winner in [self.player1, self.player2]:
            self.winner = winner
            winner.win += 1
            winner.ranking += 10  # Example: increase ranking by 10 for a win
            print(f"{winner.name} is the winner")
        else:
            print("Invalid winner")
    
    def print_match_info(self):
        print("Date: ", self.date)
        self.player1.print_info()
        self.player2.print_info()
        if self.winner:
            print("Winner: ", self.winner.name)
        else:
            print("No winner yet")

class player:
#includes information of player.
    def __init__(self,name, games, win):
        self.name = name
        self.games = games
        self.win = win
        self.ranking = 1000

    def print_info(self):
        print("Name: ", self.name)
        print("Games: ", self.games)
        print("Win: ", self.win)
        print("Ranking: ", self.ranking, "\n")

Tournament1 = tournament("London_cricket_league", "Dec", "Dec", "London \n", 1000000,)

tp1 = player("astar",35, 20)
tp2 = player("andrew",50, 30)
# tp1.print_info()
# tp2.print_info()
Tournament1.join_tournament(tp1)
Tournament1.join_tournament(tp2)

match1 = match("dec 1", tp1, tp2)
print(match1.date)
print(match1.player1.name)
print(match1.player2.name)

match_obj = match("dec 1", tp1, tp2)
Tournament1.add_match(match_obj)
Tournament1.print_tournament_info()

print(Tournament1.list_of_matches)

# Example: Set winner for the match
match_obj.set_winner(tp1)
Tournament1.print_tournament_info()

        