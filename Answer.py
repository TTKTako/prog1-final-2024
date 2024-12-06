import turtle
import ball
from run_ball import create_ball
from seven_segments_proc import create_num
import time

past_time = time.time()
def which_num(i):
    if time.time() - past_time >= delay_in_seconds:
        i += 1
        if i > 9:
            i = 0
        return i
    return i


call_oop = create_ball()
dt = 0.2 # time step

Tom = turtle.Turtle()

tom_color = (255, 0, 0)
delay_in_seconds = 0.2
used_class = create_num(Tom, tom_color)

num = 0
while (True):
    past_time = time.time()
    turtle.clear()
    call_oop.draw_border()
    call_oop.generate()
    for i in range(call_oop.num_balls):
        ball.draw_ball(call_oop.ball_color[i], call_oop.ball_radius, call_oop.xpos[i], call_oop.ypos[i])
        ball.move_ball(i, call_oop.xpos, call_oop.ypos, call_oop.vx, call_oop.vy, dt)
        ball.update_ball_velocity(i, call_oop.xpos, call_oop.ypos, call_oop.vx, call_oop.vy, call_oop.canvas_width, call_oop.canvas_height, call_oop.ball_radius)

    num = which_num(num)
    used_class.clear(Tom)
    used_class.draw(Tom, num)
    turtle.update()


turtle.done()