def setup():
    size(500,500)
    background(20,20,250)
    
    #dette er et quad i hjørnet
    fill(200,20,200)
    stroke(255,255,100)
    strokeWeight(5)
    quad(38,31,86,20,69,63,30,76)
    #quad(x1, y1, x2, y2, x3, y3, x4, y4)

    #dette er en linje igennem quad
    strokeWeight(4)
    stroke(20,200,100)
    line(20,20,100,70)
    rect(70,70,200,200)



    
