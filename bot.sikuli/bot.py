click(Region(83,565,121,121)) #focus the window
Settings.MoveMouseDelay = .1
while True:
    #Play cards
    x = 320
    y = 730
    w = 44
    h = 86
    play = Region(485,400,69,103)
    for i in range(0, 10):
        r = Region(x, y, w, h)
        
        dragDrop(r, play)
        x += 60

    click(Region(613,583,49,51))
    
    x = 220
    y = 396
    w = 91
    h = 106
    #attack
    for i in range(0, 10):
        r = Region(x, y, w, h)
        click(r)
        click(Region(457,118,119,125))
        x2 = 220
        y2 = 280
        w2 = 91
        h2 = 106
        try:
            if exists("1411536305986.png"):
                region = find("1411536305986.png")
                if region == None or region.x > 385:
                    for i in range(0, 10):
                        r2 = Region(x2, y2, w2, h2)
                        click(r2)
                        x2 += 60
                else:
                    click(region)
            else:
                for i in range(0, 10):
                    r2 = Region(x2, y2, w2, h2)
                    click(r2)
                    x2 += 60
        except FindFailed:
            print "crap"
        x += 60
    #attack minions if there was a taunt
    
    click(Region(884,365,77,26))
        
    
    try:
        hover(Region(83,591,84,69)) #hover in lower left
        wait("1411531507104.png", 120)
        print("MY TURN!")  
        
    except FindFailed:
        print "uh oh, turn didn't finish in 120 seconds"
    