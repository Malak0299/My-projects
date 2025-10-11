#STACKS AND QUEUES

#STACK (lIFO - LAST IN, FIRST OUT) - STACK BØGER: BRUGES NÅR SIDSTE ELEMENT SKAL FJERNES FØRST.(UNDO KNAP)
stak = []
stak.append(1)
stak.append(2)
stak.pop() #fjerner 2
print(stak)

#QUEUE (FIFO -FIRST IN, FIRST OUT) - KØ BRUGES: NÅR FØRSTE ELEMENT SKAL FJERNES FØRST (PRINTERJOBS, TRAFIKSYS, KUNDEKØER)
ko = []
ko.append(1)
ko.append(2)
ko.pop(0) #fjerner 1
print(ko)

