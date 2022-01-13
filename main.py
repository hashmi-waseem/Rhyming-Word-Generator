import json
import requests
def alternate(s):
    baseurl = "https://api.datamuse.com/words"
    d={}
    d['rel_rhy']=s
    d['max']='1'
    k = requests.get(baseurl,params = d)
    m = k.json()
    return m[0]['word']

def convert_string_to_word(n):
    my = n.split()
    rephrased = ''
    for i in my:
        k=alternate(i)
        rephrased+=k
        rephrased += ' '
    return rephrased
b=input('Enter a string to generate a rhyming string:   ')
a = convert_string_to_word(b)
print('Original String:    ',b)
print('Rhyming String:     ',a)