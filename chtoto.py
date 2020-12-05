class character:

    def __init__(self):
        self.x = 200
        self.y = 75
        self.x_size = 20
        self.y_size = 60
        self.orientation = 0 # 1 = right , -1 = left, 0 = forward
        self.vy = 0
        self.vx = 25
        self.hp = 10
        self.color = (255, 255, 255)

    def draw(self):
        global display
        rect(display, self.color,(self.x, self.y, self.x_size, self.y_size))
    

class block():

    def __init__(self, color, hp, breakable, loot):
        self.color = color
        self.hp = hp
        self.breakable = breakable
        self.loot = loot # ochkov
        self.size = 50

    def create(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        global display
        rect(display, self.color, (self.x, self.y, self.size, self.size)))

    def kill(self, blocks):
        blocks.remove(self)
    
    def damage(self):
        if self.breakable == True:
            self.hp -= 1
        


def create_map():
    blocks = []
    for i in range(0, 9):
        for j in range(2, 7):
            block = block(color_green, 10, True, 10)
            block.create(i * block.size, j * block.size)
            blocks.append(block)
    return blocks
