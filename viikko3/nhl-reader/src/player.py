class Player:
    def __init__(self, name, nationality, assists, goals, team):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists

    def get_nationality(self):
        return self.nationality
    
    def __str__(self):
        return f"{self.name} team {self.team} goals {self.goals} assists { self.assists}"

