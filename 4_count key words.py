#words calcul
import csv
import numpy as np

train=[]
limit=1000000
count=0

csvfile=open('../train.csv', newline='',encoding="utf8")
spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
for row in spamreader:
    count+=1
    train.append(row)
    if(count>limit):
        break

csvfile.close()   
#print(train)

count1=0
count2=0
count3=0
Disa=[]
Agr=[]
Unr=[]

# this loop is usefull to know the number of lines of each categories in the sample of the test
for line in train:
    if(len(line)>5):
        if(line[5]=="agreed"):
          count1+=1
          Agr.append(line[4])
        elif (line[5]=="disagreed"):
          count2+=1  
          Disa.append(line[4])
        elif(line[5]=="unrelated"):
          count3+=1
          Unr.append(line[4])

print("Agreed :",count1)
print("Disagreed :",count2)
print("Unrelated :",count3)

# we did not count words of the Stops List : words that have no impact in the meaning of the sentence
Stops=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

def nbWords(liste):
  Liste=[]
  for a in liste:                      # each News of the Disagreed Liste
    b=a.split()                     # we separate words of the message
    #print(b)
    for C in b:                         #each words in the message
      e=0
      c=C.lower()  # this line change every letters in lowercase letters (to have "Example"="example")
      if len(c) >2 and c not in Stops:        
        for d in Liste:             #check if the word is already in the list
          if (c in d[1]) or (d[1] in c):    #if yes : implement the word +1
            d[0]+=1
            if(len(c)<len(d[1])):   # this trick allow us to combine same words with different ends ("example"="examples")
              d[1]=c
            e=1
            break
        if e==0:                        #if not add it to the list
          Liste.append([1,c])  
  Liste.sort(reverse=True)  
  return Liste

print("Agreed :",count1)
print("Disagreed :",count2)
print("Unrelated :",count3)

print("Disagreed Words : ",nbWords(Disa))
print("Agreed Words : ",nbWords(Agr))
print("Unrelated Words : ",nbWords(Unr))