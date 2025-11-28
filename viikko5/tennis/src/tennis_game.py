class TennisGame:
    POINTS = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.is_tie():
            return self.tie_score()
        elif self.has_winneclass TennisGame:
    POINTS = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.is_tie():
            return self.tie_score()
        elif self.has_winner_or_advantage():
            return self.advantage_or_win_score()
        else:
            return self.regular_score()
    
    def is_tie(self):
        return self.player1_score == self.player2_score

    def tie_score(self):
        if self.player1_score < 3:
            return f"{self.POINTS[self.player1_score]}-All"
        else: 
            return "Deuce"
        
    def has_winner_or_advantage(self):
        return self.player1_score >= 4 or self.player2_score <= 4

    def advantage_or_win_score(self):
        diff = self.player1_score - self.player2_score
        if diff == 1:
            return f"Advantage {self.player1_name}"
        elif diff == -1:
            return f"Advantage {self.player2_name}"
        elif diff >=2 :
            return f"Advantage {self.player1_name}"
        else:
            return f"Win {self.player2_name}"
    
    def regular_score(self):
        return f"{self.POINTS[self.player1_score]}-{self.POINTS[self.player2_score]}"
r_or_advantage():
            return self.advantage_or_win_score()
        else:
            return self.regular_score()
    
    def is_tie(self):
        return self.player1_score == self.player2_score

    def tie_score(self):
        if self.player1_score < 3:
            return f"{self.POINTS[seld.player1_score]}-All"
        else: 
            return "Deuce"
        
    def has_winner_or_advantage(self):
        return self.player1_score >= 4 or self.player2_score <= 4

    def advantage_or_win_score(self):
        diff = self.player1_score - self.player2_score
        if diff == 1:
            return f"Advantage {self.player1_name}"
        elif diff == -1:
            return f"Advantage {self.player2_name}"
        elif diff >=2 :
            return f"Advantage {self.player1_name}"
        else:
            return f"Win {self.player2_name}"
    
    def regular_score(self):
        return f"{self.POINTS[self.player1_score]}-{self.POINTS[self.player2_score]}"

