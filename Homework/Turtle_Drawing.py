import math
def getNumVertex(polygon_name):
    poly={
        "triangle":3,
        "square":4,
        "pentagon":5,
        "hexagon":6,
        "heptagon":7,
        "octagon":8,
        "nonagon":9,
        "decagon":10
    }
    return poly[polygon_name]

def getPolygonName(num_vertex):
    polyName={
        3:"triangle",
        4:"square",
        5:"pentagon",
        6:"hexagon",
        7:"heptagon",
        8:"octagon",
        9:"nonagon",
        10:"decagon"
    }
    return polyName[num_vertex]

def drawPolygon(t, center_pos,num_vertex, radius, color):
    center=[]
    for i in center_pos:
        center.append(i)
    #cx=center_pos[0],cy=center_pos[1]
    t.up()
    t.goto(center[0],center[1])
    t.dot(10,'blue')
    #ver_num=getNumVertex(num_vertex)
    total_deg=180*(num_vertex-2)
    deg=total_deg/num_vertex
    theta=math.radians(deg/2)
    starting_x=abs(radius*math.cos(theta));starting_y=abs(radius*math.sin(theta))
    t.goto(center[0]-starting_x,center[1]-starting_y)
    line_length=starting_x*2
    t.down()
    t.color(color)
    t.write(t.pos())#starting point

    for i in range(num_vertex):
        t.fd(line_length)
        t.lt(360/num_vertex)
    t.up()
    t.dot(10,color)
    t.goto(center[0]-starting_x,center[1]-starting_y-30)
    t.write(color+' '+str(getPolygonName(num_vertex)))

def drawCircle(t, center_pos, radius, color):#center_pos형식: tuple
    center=[]
    t.width(1)
    for i in center_pos:
        center.append(i)
    center_x,center_y=center[0],center[1]
    t.up()
    t.goto(center_x,center_y-radius)
    t.down()
    t.circle(radius)
    t.width(5)

def drawStar(t, center_pos, radius, color):
    center=[]
    for i in center_pos:
        center.append(i)
    length=radius*math.sin(72)
    #cx=center_pos[0],cy=center_pos[1]
    cx,cy=center[0],center[1]
    sx = cx - length / 2
    theta_rad = math.radians(360 / 5)
    sy = cy + length / (2 * math.tan(theta_rad))
    t.up();t.goto((sx,sy));t.down()
    count=0
    turn_angle=360*2/5
    while count<5:
        t.fd(length)
        t.rt(turn_angle)
        count+=1
    t.up();t.goto(0,0);t.down()