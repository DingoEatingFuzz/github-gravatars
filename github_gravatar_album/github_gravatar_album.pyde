from random import shuffle
from colorsys import hsv_to_rgb

add_library('P8gGraphicsSVG')

def setup():
    global start_ms
    start_ms = millis()
    
    w = 1200
    h = 900
    
    size(w, h)
    
    seeds = [int(x) for x in open('seeds.txt')]
    
    if len(seeds) != 2**15:
        println('seeds had length of %s; required length is %s' % (len(seeds), 2**15))
        exit()
    
    s = 660
    pw = (w - s) / 2
    ph = (h - s) / 2
    for index, seed in enumerate(seeds[:5]):
        background(255)
        beginRecord(P8gGraphicsSVG.SVG, 'svg_album/%s.svg' % index)
        pushMatrix()
        translate(pw, ph)
        avatar(seed, s)
        popMatrix()
        endRecord()
        save('png_album/%s.png' % index)
        clear()
        println(str(floor(float(index) / float(len(seeds)) * 100)) + '%')
    exit()

def stop():
    global start_ms
    end_ms = millis()
    format_duration(end_ms - start_ms)

def format_duration(dur):
    ms = dur % 1000
    s = floor(dur / 1000 % 60)
    m = floor(dur / (1000 * 60) % 60)
    h = floor(dur / (1000 * 60 * 60))
    println('%sh %sm %ss %s' % (h, m, s, ms))

def avatar(seed, avatarSize = 50):
    paddingSize = floor(avatarSize * 0.05)
    tileSize = ceil(avatarSize * 0.9 / 5)
    
    noStroke()
    fill(245, 245, 245)
    rect(0, 0, avatarSize, avatarSize, paddingSize, paddingSize, paddingSize, paddingSize)
    
    c = hsv_to_rgb(to_float(random(255)), to_float(random(25, 75)), to_float(random(175, 225)))
    fill(to_hex(c[0]), to_hex(c[1]), to_hex(c[2]))
    
    pushMatrix()
    translate(paddingSize, paddingSize)
    for i in range(5):
        for j in range(3):
            if seed & (1 << (i * 3 + j)):
                rect(tileSize * j, tileSize * i, tileSize, tileSize)
                if j != 2:
                    rect(tileSize * (4 - j), tileSize * i, tileSize, tileSize)
    popMatrix()

def to_float(n):
    return map(n, 0, 255, 0, 1)

def to_hex(n):
    return map(n, 0, 1, 0, 255)
