def setup():
    size(500,500)
    background(0)
    
def draw():    
    background(0)
    
    if mouseY <= 250:
        fill(100,200,0)
        circle(mouseX,mouseY,40)
    elif mouseY <= 400:
        fill(0,100,255)
        circle(mouseX,mouseY,40)
    else:
        fill(200,100,10)
        circle(mouseX,mouseY,40)
