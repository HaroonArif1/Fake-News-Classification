#Test finding words:

import csv
from sentence_transformers import SentenceTransformer, util
import numpy as np
from random import randint 

model = SentenceTransformer('stsb-roberta-large')

Train=[]

######################## open of the file #######################################
csvfile=open('../train.csv', newline='',encoding="utf8")
spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
for row in spamreader:
    Train.append(row)

csvfile.close()   

############################ selection of the sample ####################
# this function gives the possibilty to take a random sample of line in the 
# train.csv file to not have only the first line every time.

def RandMail(sample):
    A=len(sample)
    limit=100    #limit of line we take
    L=[]
    count1=0
    count2=0
    count3=0  
    while limit>0:
        C=randint(0,A)
        if C not in L:
            if(Train[C][5]=="agreed" and count1<20): # this gives the possibility to limit the number of Agreed line. 
              L.append(C)                               # if the number is higher than the limit max, it means that there is no restriction.
              limit-=1
              count1+=1
            if(Train[C][5]=="disagreed" and count2<20):
              L.append(C)
              limit-=1
              count2+=1
            if(Train[C][5]=="unrelated" and count3<60):
              L.append(C)
              limit-=1
              count3+=1
    print(L)
    Liste=[]
    for i in L:
        Liste.append(sample[i])
    return Liste

train = RandMail(Train)
#print(train)


####################### function of similarity #################################
def simScore(LINE):
  embedding1 = model.encode(LINE[3], convert_to_tensor=True)
  embedding2 = model.encode(LINE[4], convert_to_tensor=True)
  cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)
  return cosine_scores.item()


########################### function of research of special words ###############
falseList=["rumor","rumour"]
def testDisagreed(Line):
  texte=Line[4].lower()
  for k in falseList:
    if (k in texte): # if there is a word of falseList in the message : we say it is a Disagreed message
      return True
  return False

################### verification repartion of the sample #######################
count1=0
count2=0
count3=0
for line in train:
    if(len(line)>5):
        if(line[5]=="agreed"):
          count1+=1
        elif (line[5]=="disagreed"):
          count2+=1  
        elif(line[5]=="unrelated"):
          count3+=1
print("Disagreed :",count2)
print("Agreed :",count1)
print("Unrelated :",count3)


################ analysis of the sample and count of errors ######################
TRUE1=0 
TRUE2=0
TRUE3=0
FALSE1=0
FALSE2=0
FALSE3=0
for line in train:
    if(len(line)>5):
      score=simScore(line)
      if(score>0.5 and testDisagreed(line)):
        if (line[5]=="disagreed"):
          TRUE1+=1                  # classified as Disagreed and it was a Disagreed
        else :
          FALSE1+=1                 # classified as Disagreed and it was not
      elif(score>0.5):
        if (line[5]=="agreed"):
          TRUE2+=1                  # classified as Agreed and it was a Agreed
        else :
          FALSE2+=1                 # classified as Agreed and it was not
      else:
        if (line[5]=="unrelated"):
          TRUE3+=1                  # classified as Unrelated and it was a Unrelated
        else :
          FALSE3+=1                 # classified as Unrelated and it was not
     

print("")
print("True :",TRUE1+TRUE2+TRUE3)
print("")
print("True1 :",TRUE1)
print("False1 :",FALSE1)
print("True2 :",TRUE2)
print("False2 :",FALSE2)
print("True3 :",TRUE3)
print("False3 :",FALSE3)