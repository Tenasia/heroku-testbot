


import turtle


def applyRule(lhch):

    rule = ''

    if lhch == 'L':
        rule += '+RF-LFL-FR+'
    elif lhch == 'R':
        rule += '-LF+RFR+FL'
    else:
        rule = rule
    
    return rule

def processString(oldString):
    newStr = ''

    for char in oldString:
        newStr += applyRule(char)

    return newStr

def createLSystem(iterNumber, axiom):
    startString = axiom
    endString = ''

    for _ in range(iterNumber):
        endString = processString(startString)
        startString = endString

    return endString

def draw(t, instructions, angle, distance):

    for step in instructions:
        if step == 'F':
            t.forward(distance)
        elif step == 'L':
            t.left(angle)
        elif step == 'R':
            t.right(angle)
        elif step == '+':
            t.forward(distance)
        elif step == '-':
            t.forward(-distance)
        else:
            pass
    
def main():
    wn = turtle.Screen()
    turtleL = turtle.Turtle()

    turtleL.speed(0)

    instructions = createLSystem(4, 'L')

    draw(turtleL, instructions, 90, 5)
    wn.exitonclick()

if __name__ == '__main__':
    main()