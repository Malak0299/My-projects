def setup(): #SETUP
    size(500,500)
    background(255)
    stroke(0)
    
    for i in range(21):#21 FELTER
        line(0+25*i,0,0+25*i,500)#LODRET
        line(0,0+25*i,500,0+25*i)#VANDRET
      
      #DIAGONALE LINJER
    for i in range(20):#LODRET
        for j in range(20):#VANDRET
            line(0+25*i,0+25*j,25+25*i,25+25*j)#LODRET + VANDRET