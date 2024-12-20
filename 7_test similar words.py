#finding if there is many similar words in the two message
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

# we create 3 lists, with lines of each categories
for line in train:
    if(len(line)>5):
        if(line[5]=="agreed"):
          count1+=1
          Agr.append([line[3],line[4]])
        elif (line[5]=="disagreed"):
          count2+=1  
          Disa.append([line[3],line[4]])
        elif(line[5]=="unrelated"):
          count3+=1
          Unr.append([line[3],line[4]])

print("Agreed :",count1)
print("Disagreed :",count2)
print("Unrelated :",count3)

Stops=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

def nbWords(liste):
  count1=0
  for a in liste:                      # each News of the Liste of line
    b0=a[0].split()                     # separate words of the message
    b1=a[1].split()
    #print(b)
    count2=0
    for C0 in b0:                         # c0 each words in the news 1
      e=0
      c0=C0.lower()
      if len(c0) >2 and c0 not in Stops:
        for C1 in b1:                     # c1 each words in the news 2
          c1=C1.lower()
          if(c0==c1):                     # if there is a match with c0 and c1
            count2+=1                     
    count1=count2+count1
  return count1/len(liste)              # we return the average for the category  
        
print("Disagreed average similar Words : ",nbWords(Disa))
print("Agreed average similar Words : ",nbWords(Agr))
print("Unrelated average similar Words : ",nbWords(Unr))