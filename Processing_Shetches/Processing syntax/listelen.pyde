def setup():
    size(500,500)
    background(0)

    fill(random(100,255),0,random(100,255)) #Vælger en random farve hver gang

    list = [300,200,50,100,200,200,100] #liste med højde af firkanterne
    for i in range(len(list)):#Løkken løber til der ikke er flere elemeter (len tager længen af listen og printer dem).
        rect(50+60*i,400,50,-list[i])#Firkanternes placering og størrelsen
        
        
