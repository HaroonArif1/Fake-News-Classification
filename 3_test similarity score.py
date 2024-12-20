#Test about similarity : tests on the Train file
import csv
from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer('stsb-roberta-large')

train=[]
limit=100
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

TRUE=0
FALSE=0

def simScore(LINE):
  embedding1 = model.encode(LINE[3], convert_to_tensor=True)
  embedding2 = model.encode(LINE[4], convert_to_tensor=True)
  cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)
  return cosine_scores.item()

for line in train:
    if(len(line)>5):
        score=simScore(line)
        
        # if the score is higher than 0.5 and it is a Agreed or Disagreed 
        # message, the seperation is a success
        if((line[5]=="agreed" or line[5]=="disagreed") and score>0.5):
            TRUE+=1
        
        # if the score is lower than 0.5 and it is a Unrelated 
        # message, the seperation is a success
        elif(line[5]=="unrelated" and score<0.5):
            TRUE+=1
            
        # else the separation did not work for this line
        else:
            FALSE+=1
            #print(line[5],score)

print("True :",TRUE)
print("False :",FALSE)