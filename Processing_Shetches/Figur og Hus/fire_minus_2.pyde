# 4 minus 2 
def setup():
    size(510,510)
    background(0)
    stroke(255)


    background(0)
    for j in range(0,10):
        for i in range(0,10):
            r = int(random(1,7))
            if r == 1:
                line(10+50*i,10+50*j,10+50*i,50+50*j)
                line(10+50*i,50+50*j,50+50*i,50+50*j)
    
            if r == 2:
                #background(0)
                line(10+50*i,10+50*j,50+50*i,10+50*j)
                line(50+50*i,10+50*j,50+50*i,50+50*j)
    
            if r == 3:
                #background(0)
                line(50+50*i,10+50*j,50+50*i,50+50*j)
                line(10+50*i,50+50*j,50+50*i,50+50*j)
        
            if r == 4:
                #background(0)
                line(10+50*i,10+50*j,50+50*i,10+50*j)
                line(10+50*i,10+50*j,10+50*i,50+50*j)
    
            if r == 5:
                #background(0)
                line(10+50*i,10+50*j,50+50*i,10+50*j)
                line(10+50*i,50+50*j,50+50*i,50+50*j)
    
            if r == 6:
                #background(0)
                line(50+50*i,10+50*j,50+50*i,50+50*j)
                line(10+50*i,10+50*j,10+50*i,50+50*j)
        
    
