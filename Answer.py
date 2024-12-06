import turtle
import ball
from run_ball import create_ball
from seven_segments_proc import create_num

call_oop = create_ball()
dt = 0.2 # time step

Tom = turtle.Turtle()
tom_color = (255, 0, 0)
delay_in_seconds = 0.2
used_class = create_num(Tom, tom_color)
used_class.run(delay_in_seconds)

create_num().run()

while (True):
    turtle.clear()
    call_oop.draw_border()
    call_oop.generate()
    for i in range(call_oop.num_balls):
        ball.draw_ball(call_oop.ball_color[i], call_oop.ball_radius, call_oop.xpos[i], call_oop.ypos[i])
        ball.move_ball(i, call_oop.xpos, call_oop.ypos, call_oop.vx, call_oop.vy, dt)
        ball.update_ball_velocity(i, call_oop.xpos, call_oop.ypos, call_oop.vx, call_oop.vy, call_oop.canvas_width, call_oop.canvas_height, call_oop.ball_radius)
    turtle.update()


turtle.done()