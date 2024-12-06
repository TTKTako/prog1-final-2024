import turtle
import ball
import random

class create_ball:
    def __init__(self):
        self.num_balls = 5
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []

    def generate(self):
        # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
        for i in range(self.num_balls):
            self.xpos.append(random.uniform(-1*self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos.append(random.uniform(-1*self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx.append(10*random.uniform(-1.0, 1.0))
            self.vy.append(10*random.uniform(-1.0, 1.0))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)

    def run(self):
        call_oop = create_ball()
        dt = 0.2 # time step
        while (True):
            turtle.clear()
            call_oop.draw_border()
            call_oop.generate()
            for i in range(call_oop.num_balls):
                ball.draw_ball(call_oop.ball_color[i], call_oop.ball_radius, call_oop.xpos[i], call_oop.ypos[i])
                ball.move_ball(i, call_oop.xpos, call_oop.ypos, call_oop.vx, call_oop.vy, dt)
                ball.update_ball_velocity(i, call_oop.xpos, call_oop.ypos, call_oop.vx, call_oop.vy, call_oop.canvas_width, call_oop.canvas_height, call_oop.ball_radius)
            turtle.update()

        # hold the window; close it by clicking the window close 'x' mark
        turtle.done()
