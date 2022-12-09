import turtle, math

def drawPolygon(t,center_x,center_y,line_length,num_vertices):
    turn_angle_deg = 360/num_vertices
    theta_rad = (math.pi-math.pi*2/num_vertices)/2
    h = math.tan(theta_rad)*line_length/2
    start_x = center_x-line_length/2
    start_y = center_y-h
    t.up(); t.goto(start_x, start_y); t.down()
    t.dot(10, 'red'); t.write(t.pos())
    for i in range(num_vertices):
        t.forward(line_length)
        t.left(turn_angle_deg)
        t.dot(10, 'red'); t.write(t.pos())
    t.up(); t.home(); t.down()

t=turtle.Turtle()
#t.shape('turtle')
center_x,center_y,num_vertices,line_length=map(int,(input('input center_x, center_y, num_vertices, and line_length : ').split(' ')))
center_pos=(center_x,center_y)
line_width=3
t.up();t.goto(center_pos);t.down()
t.dot(10,'red');t.write(center_pos)
t.width(line_width)
t.pencolor('blue')
drawPolygon(t,center_x,center_y,line_length,num_vertices)
input()