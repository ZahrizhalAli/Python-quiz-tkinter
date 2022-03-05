

class Scoreboard():
    def __init__(self):
        self.score = 0
        with open('score.txt', 'r') as f:
            self.high_score = f.read()

    def reset(self):
        pass

    def update_score(self):
        pass
