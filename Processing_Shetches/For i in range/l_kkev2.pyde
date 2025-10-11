def setup():
    size(500,500)
    background(20,20,200)
    
    strokeWeight(3)
    for i in range (0,100):
        line(50+30*i,60,random(0,100),200)
        line(50+40*i,60,random(0,100),200)
        line(50+50*i,60,random(0,100),200)
        line(50+60*i,60,random(0,100),200)
        line(50+70*i,60,random(0,100),200)
        line(50+80*i,60,random(0,100),200)
        
