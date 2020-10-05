# put your code here.
def word_count (poem):
#returns a dictionary with each space-separated word. 

    words_dict = {}
    for word in poem.split(' '):
        words_dict[word]= (words_dict.get(word, 0))+1 
    
    for word, count in words_dict.items(): 
        print (f'{word} {count}')
    

def main ():
    
    test_1 = "As I was going to St. Ives I met a man with seven wives Every wife had seven sacks Every sack had seven cats Every cat had seven kits Kits, cats, sacks, wives. How many were going to St. Ives?"
    word_count(test_1)

main ()