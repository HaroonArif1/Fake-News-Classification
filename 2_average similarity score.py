#Test about similarity : analysis on the Train file
import csv
from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer('stsb-roberta-large')

train=[]
limit=100    # limit number of line we will read in the file
count=0

csvfile=open('../train.csv', newline='',encoding="utf8")
spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
for row in spamreader:
    count+=1
    train.append(row)
    if(count>limit):    # When we reach the limit, we stop to take lines
        break

csvfile.close()   
#print(train)

def simScore(LINE):
  embedding1 = model.encode(LINE[3], convert_to_tensor=True)
  embedding2 = model.encode(LINE[4], convert_to_tensor=True)
  cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)
  return cosine_scores.item()


# then we create 3 lists, and in each of it, we will put the Similarity Score
# of one of the 3 categories (Agreed, Disagreed, Unrelated)
simAgreed=[]
simDisagreed=[]
simUnrelated=[]

for line in train:
    if(len(line)>5):
        if(line[5]=="agreed"):
            simAgreed.append(simScore(line))
        elif(line[5]=="disagreed"):
            simDisagreed.append(simScore(line))
        else:
            simUnrelated.append(simScore(line))

print("Agreed :",sum(simAgreed)/len(simAgreed))
print("Disagreed :",sum(simDisagreed)/len(simDisagreed))
print("UnRelated :",sum(simUnrelated)/len(simUnrelated))