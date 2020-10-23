# Alejandra Castillo 1440370
# Winning team (classes)

# class definition
class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        percent = self.team_wins / (self.team_wins + self.team_losses)
        return percent
