# PE02 - OOP and Comprehensions

# DO NOT CHANGE IMPORTS
#######################
import copy
#######################

class Team:
    """
    Question 1
    - Initialize and complete the Team class.
    """
    def __init__(self, mascot, city, league, seed=0):
        self.mascot = mascot
        self.city = city
        self.league = league
        self.seed = seed

    def __eq__(self, other):
        return (self.mascot == other.mascot) and (self.city == other.city)

    def __lt__(self, other):
        return self.seed > other.seed

    def __str__(self):
        return "GO %s %s!" % (self.city.upper(), self.mascot.upper())

    def __repr__(self):
        return "The %s %s are the %s seed in the %s." % (self.city, self.mascot, self.seed, self.league)

def assign_teams_to_owners(owners_list, team_list):
    return {k.split()[1]: v.city[:3].upper() for k,v in zip(owners_list, team_list)}

def playoff_cutoff(playoff_teams, losing_team):
    return [x for x in playoff_teams if x.city not in losing_team.city]


def move_team(team, new_city):
    new_team = copy.copy(team)
    new_team.city = new_city
    return new_team



################################################################################
if __name__ == "__main__":
    """
    This is the if __name__ == "__main___": code block that you learned in class.
    Remember the pyhton interpreter will only read the code below if the statement
    above evaluates to True. Therefore, the code below will only execute if
    this .py file is run as a script (i.e. running it through the command line
    via python PE02.py). This code will not execute when run via the Gradescope
    autograder because the autograder grades your code by importing your PE
    .py file (i.e. import PE02.py). This implies that you can test your code
    in this code block, and the function calls below will neither execute nor
    error in Gradescope when run via the autograder. Good luck!

    Note: You should be able to trace and understand the code below. If you have
    any questions in regards to this code, please make a public post on the ED
    Discussion Board, so everyone can benefit.
    """

    #q1a
    team = Team("Hornets", "Charlotte", "NBA", 10)
    print('q1a', 'PASSED' if team.mascot == 'Hornets' and team.city == 'Charlotte' and team.league == 'NBA' and team.seed == 10 else False)

    #q1b
    team1 = Team("Hornets", "Charlotte", "NBA", 10)
    team2 = Team("Hornets", "Charlotte", "WNBA", 1)
    print('q1b', 'PASSED' if team1 == team2 else False)

    team1 = Team("Hornets", "Charlotte", "NBA", 10)
    team2 = Team("Hornets", "Charleston", "NBA", 10)
    print('q1b', 'PASSED' if not (team1 == team2) else False)

    #q1c
    dream_team = Team("Dream", "Atlanta", "WNBA", 7)
    lib_team = Team("Liberty", "New York", "WNBA", 1)
    print('q1c', 'PASSED' if dream_team < lib_team else False)

    #q1d
    print('q1d', 'PASSED' if str(Team("Dream", "Atlanta", "WNBA", 7)) == 'GO ATLANTA DREAM!' else False)

    #q1e
    alist = [Team("Jazz", "Utah", "NBA", 1), Team("Hornets", "Charlotte", "NBA", 10)]
    print('q1e', 'PASSED' if [repr(t) for t in alist] == ['The Utah Jazz are the 1 seed in the NBA.', 'The Charlotte Hornets are the 10 seed in the NBA.'] else False)

    #q2
    owners = ["Micky Arison", "Michael Jordan", "Mark Cuban"]
    team_arison = Team("Heat", "Miami", "NBA", 6)
    team_jordan = Team("Hornets", "Charlotte", "NBA", 10)
    team_cuban = Team("Mavericks", "Dallas","NBA", 5)
    teams = [team_arison, team_jordan, team_cuban]
    print('q2', 'PASSED' if assign_teams_to_owners(owners, teams) == {"Arison": "MIA", "Jordan": "CHA", "Cuban": "DAL"} else False)

    #q3
    hawk_team = Team("Hawks", "Atlanta", "NBA", 5)
    horn_team = Team("Hornets", "Charlotte", "NBA", 10)
    nug_team = Team("Nuggets", "Denver", "NBA", 1)
    winning_teams = [hawk_team, horn_team, nug_team]
    print('q3', 'PASSED' if [repr(t) for t in playoff_cutoff(winning_teams, horn_team)]
        == ['The Atlanta Hawks are the 4 seed in the NBA.', 'The Denver Nuggets are the 1 seed in the NBA.'] else False)

    #q4
    old_record = Team("Clippers", "Los Angeles", "NBA", 4)
    new_record = move_team(old_record, "San Diego")
    print('q4', 'PASSED' if repr(old_record) == 'The Los Angeles Clippers are the 4 seed in the NBA.' else False)
    print('q4', 'PASSED' if repr(new_record) == 'The San Diego Clippers are the 4 seed in the NBA.' else False)
    print('q4', 'PASSED' if not(team2 == team1) else False)

