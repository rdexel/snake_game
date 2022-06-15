from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed('fastest')
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):

        self.write(arg=f'Score = {self.score}', move=False, align='center', font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.write(arg=f'Game Over! Your score was {self.score}', move=False,align='center', font=('Arial', 20, 'normal'))

