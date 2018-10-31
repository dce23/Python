class Color:
    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B

    def __str__(self):
        return "Color ({}, {}, {})".format(self.R, self.G, self.B)

def r_channels(cL):
    for c in range(0, len(cL)):
        cL[c].R = 0


def blended(c1, c2, w):
    b = Color(0, 0, 0)
    b.R = c1.R*w + c2.R*(1-w)
    b.G = c1.G*w + c2.G*(1-w)
    b.B = c1.B*w + c2.B*(1-w)
    
    return b

def main():
    color1 = Color(0, 0, 0)
    print(color1)
    color2 = [Color(0,0,0), Color(1,1,1), Color(3,3,3)]
    print(color2)
    color3 = blended(Color(39,53,89),Color(58,210,157),0.34)
    print(color3)
main()

    
