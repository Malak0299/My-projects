#tal = [10,20,30]
#print(f'Største tal: {len(tal)}')

scores = [60,50,60,58,54,54,58,50,52,54]

def find_min_score(scores):
    min_score = min(scores)
    print(f'Den mindste score er:  {min_score}')
    
find_min_score(scores)
