import turtle as t

width, length, center_x, center_y=map(int,input('input width, length, center_X, center_y ').split())

t.up()
t.goto((center_x,center_y))
t.lt(90)
t.fd(length/2)
t.rt(90)
t.down()
t.fd(width/2)
t.rt(90)
t.fd(length)
t.rt(90)
t.fd(width)
t.rt(90)
t.fd(length)
t.rt(90)
t.fd(width/2)
t.up()
t.goto(center_x, center_y)
input()