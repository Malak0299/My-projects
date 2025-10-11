def setup():
    size(500,500)
    background(0)
    
    fill(255,0,0)
    for m in range(1,6):
        for i in range(1,5):
            rect(50*i+20*i,50*m+20*m,50,50)
    
