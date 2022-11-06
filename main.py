import openpyxl
from tabulate import tabulate
import random
import time

team_ratings = openpyxl.load_workbook("TeamRatings.xlsx")
sheet = team_ratings['Sheet1']

def start():
    team_id = [
        ["Atlanta Hawks" , 1],
        ["Boston Celtics" , 2],
        ["Brooklyn Nets", 3],
        ["Charlotte Hornets", 4],
        ["Chicago Bulls", 5], 
        ["Cleveland Cavaliers", 6],
        ["Dallas Mavericks", 7], 
        ["Denver Nuggets", 8],
        ["Detroit Pistons", 9],
        ["Golden State Warriors", 10],
        ["Houston Rockets", 11],
        ["Indiana Pacers", 12],
        ["Los Angeles Clippers", 13],
        ["Los Angeles Lakers", 14],
        ["Memphis Grizzlies", 15], 
        ["Miami Heat", 16], 
        ["Milwaukee Bucks", 17],
        ["Minnesota Timberwolves", 18],
        ["New Orleans Pelicans", 19],
        ["New York Knicks", 20],
        ["Oklahoma City Thunder", 21],
        ["Orlando Magic", 22],
        ["Philadelphia 76ers", 23],
        ["Phoenix Suns", 24],
        ["Portland Trail Blazers", 25],
        ["Sacramento Kings", 26],
        ["San Antonio Spurs", 27],
        ["Toronto Raptors", 28],
        ["Utah Jazz", 29],
        ["Washington Wizards", 30]
    ]
    head = ["Team Name", "ID"]


    print("Here is the list of teams and their id's to get you started: ")
    print(tabulate(team_id, headers = head, tablefmt = "simple_grid"))


class Team:
    def __init__(self, id):
        self.id = id
        self.conference = None
        self.rating = None
        self.team_name = None

    def getAttributes(self):
        for i in sheet.iter_rows():
            id = i[0].value
            if id == self.id:
                self.team_name = i[1].value
                self.conference = i[2].value
                self.rating = i[15].value
        print(f"Team Name: {self.team_name}")
        print(f"Team Conference: {self.conference}")
        print(f"Team Rating: {self.rating}")

class Series:
    def __init__(self):
        self.winner = None
        self.games = None

    def play(team1, team2):
        team1_wins = 0
        team2_wins = 0
        team1_low = team1.rating - 5
        team1_high = team1.rating + 5
        team2_low = team2.rating - 5
        team2_high = team2.rating + 5
        game_number = 0
        while team1_wins < 4 or team2_wins < 4:
            team1_score = random.uniform(team1_low, team1_high)
            team2_score = random.uniform(team2_low, team2_high)
            game_number += 1
            if team1_score > team2_score:
                team1_wins += 1
                print(f"Game {game_number} winner: {team1}")
                
            else:
                team2_wins += 1
                print(f"Game {game_number} winner: {team2}")
            time.sleep(1)

        if team1_wins == 4:
            return f"Series winner: {team1}"

        else:
            return f"Series winner: {team2}"

start = start()




