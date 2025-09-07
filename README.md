# Tournament_Runner
Tournament_Runner is a Python program that simulates a sports tournament using OOP. It manages tournaments, players, and matches, tracks wins and rankings, and prints detailed results with an easy-to-follow structure.

# tournament_runner  

`tournament_runner` is a Python program that simulates a sports tournament using object-oriented programming (OOP). It allows you to create tournaments, add players, schedule matches, declare winners, and track player rankings dynamically.  

---

## Features  

### 🏆 Tournament Management  
- Store tournament details: name, start & end dates, location, prize money.  
- Maintain a list of players and matches.  
- Print full tournament information anytime.  

### 👤 Player Management  
- Each player has: name, games played, wins, and ranking.  
- Rankings start at `1000` and increase by `+10` per win.  
- Player info can be displayed in a clear format.  

### ⚔️ Match Management  
- Create matches between two players on a specific date.  
- Set the winner to update their stats automatically.  
- Print match details (players, date, winner).  

---

## Example Usage  

```python
# Create a tournament
Tournament1 = tournament("London_cricket_league", "Dec", "Dec", "London", 1000000)

# Add players
tp1 = player("Alok", 35, 20)
tp2 = player("Andrew", 50, 30)
Tournament1.join_tournament(tp1)
Tournament1.join_tournament(tp2)

# Schedule a match
match1 = match("Dec 1", tp1, tp2)
Tournament1.add_match(match1)

# Declare a winner
match1.set_winner(tp1)

# Print tournament details
Tournament1.print_tournament_info()
