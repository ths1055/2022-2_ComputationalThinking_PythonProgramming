import turtle as t
base, height, center_x, center_y=map(int,input('input base, height, center_X, center_y ').split())
t.up()
t.goto(center_x, center_y)
starting_x=center_x-base/2
starting_y=center_y-height/3
point1_x=center_x+base/2
point1_y=center_y-height/3
point2_x=center_x
point2_y=center_y+height*2/3
t.goto(starting_x, starting_y)
t.down()
t.goto(point1_x, point1_y)
t.goto(point2_x, point2_y)
t.goto(starting_x,starting_y)
t.up()
t.goto(center_x, center_y)
input()