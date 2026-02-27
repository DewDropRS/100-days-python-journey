from myturtle import MyTurtle

START_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_STEP = 20
class Snake:

    def __init__(self):
        self.segments = []
        self.build_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def build_snake(self):
        for pos in START_POSITIONS:
            new_segment = MyTurtle(pos)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].setpos(*self.segments[seg_num - 1].pos())
        self.segments[0].forward(MOVE_STEP)

    def grow(self):
        #append a new segment overlapping the tail segment
        new_segment = MyTurtle(self.tail.position())
        self.segments.append(new_segment)

    def move_up(self):
        # counter-clockwise
        # 0 is right, 90 is up, 180 is left, 270 is down
        #snake cannot back into its own body
        # if already headed down, can't go up
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        # if already headed up, can't go down
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        # if already headed right, can't go left
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        # if already headed left, can't go right
        if self.head.heading() != 180:
            self.head.setheading(0)

    def change_color(self, color):
        """Change all segments to the specified color"""
        for segment in self.segments:
            segment.color(color)

    def reset(self):
        for segment in self.segments:
            #move offscreen and hide
            segment.goto(800,800)
            segment.hideturtle()
        self.segments.clear()
        self.build_snake()
        self.head = self.segments[0]