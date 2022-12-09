import turtle
from Turtle_Drawing import *
def fget_drawings(fin):
    L_drawings = []
    texts=fin.readlines()
    for i in range(len(texts)):
        L_drawings.append(list(texts[i].split()))
    fin.close()
    return L_drawings

if __name__ == "__main__":
    turtle.setup(900, 500)
    turtle.title("Drawing polygons with user-defined Turtle_Drawing.py")
    t = turtle.Turtle()
    t.speed(0)
    t.shape("classic")
    fin = open("drawings.txt")
    L_drawings = fget_drawings(fin)
    fin.close()
    for drawing in L_drawings: 
        (color,shape, cx, cy, radius) = drawing
        center_pos = (int(cx), int(cy))
        print("drawing a {} {} of circumscribed circle's radius {} at center_pos({}, {}).".format(color, shape, radius, cx, cy))
        t.up(); t.goto(center_pos); t.down()
        t.dot(10, "red"); t.write(center_pos)
        t.width(5)
        if (shape == "circle"):
            drawCircle(t, center_pos, int(radius), color)
        elif (shape == "star"):
            drawStar(t, center_pos, int(radius), color)
        else:
            num_vert = getNumVertex(shape)
            if num_vert != None:
                drawPolygon(t, center_pos, num_vert, int(radius), color)
                drawCircle(t,center_pos,int(radius),'black')
            else:
                print("Drawing shape {} is not implemented yet !!".format(shape))
    input()