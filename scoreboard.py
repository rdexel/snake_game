from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.score = 0
        self.speed('fastest')
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'Score = {self.score} High Score = {self.high_score}', move=False, align='center', font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()

