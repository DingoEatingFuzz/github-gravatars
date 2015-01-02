def setup():    
    size(128 * 23 + 99, 256 * 23 + 99)
    frameRate(60)
    
    colorMode(HSB)

    background(0, 0, 255)
    global seed
    
    pushMatrix()
    translate(50, 50)
    for x in range(128):
        for y in range(256):
            pushMatrix()
            translate(23 * x, 23 * y)
            avatar(y * 128 + x, 22)
            popMatrix()
    popMatrix()
    save('tiles-full.png')
    exit()

def avatar(seed, avatarSize = 50):
    paddingSize = floor(avatarSize * 0.05)
    tileSize = ceil(avatarSize * 0.9 / 5)
    
    noStroke()
    fill(0, 0, 245)
    rect(0, 0, avatarSize, avatarSize, paddingSize, paddingSize, paddingSize, paddingSize)
    fill(random(255), random(25, 75), random(175, 225))
    
    pushMatrix()
    translate(paddingSize, paddingSize)
    for i in range(5):
        for j in range(3):
            if seed & (1 << (i * 3 + j)):
                rect(tileSize * j, tileSize * i, tileSize, tileSize)
                if j != 2:
                    rect(tileSize * (4 - j), tileSize * i, tileSize, tileSize)
    popMatrix()
