#Run of the algorithm in test.csv

import csv
from sentence_transformers import SentenceTransformer, util
import numpy as np
from random import randint 

model = SentenceTransformer('stsb-roberta-large')

TEST=[]
#c=0

######################## open of the file #######################################
csvfile=open('../test.csv', newline='',encoding="utf8")
spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
for row in spamreader:
    TEST.append(row)
    #c+=1
    #if(c==10):
    #  break

csvfile.close()   




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
    if (k in texte):
      return True
  return False

####################### function of similar words ############################
Stops=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

def similarWords(line):
  b0=line[3].split()                     # separate words
  b1=line[4].split()
  #print(b)
  count=0
  for C0 in b0:                         #each words in the news
    e=0
    c0=C0.lower()
    if len(c0) >2 and c0 not in Stops:
      for C1 in b1:
        c1=C1.lower()
        if(c0==c1):
          count+=1
  return count



################ run on test.csv ######################

testFile=open('sample.csv', 'w', newline='')
TestFile=csv.writer(testFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

count=-1
countD=0
countA=0
countU=0
for line in TEST:
    count+=1
    if(count%1000==0):
      print(count)
    if(len(line)>3):
      count=similarWords(line)
      DISA=testDisagreed(line) # test to find "rumor" or "rumour" in the message
      if (DISA or count>2):
        score=simScore(line)
        if(score>0.4 and DISA):
          TestFile.writerow([line[0],'disagreed'])
          countD+=1
        elif(count>3 and score>0.4):
          TestFile.writerow([line[0],'agreed'])
          countA+=1
        else:
          TestFile.writerow([line[0],'unrelated'])
          countU+=1
      else:
        TestFile.writerow([line[0],'unrelated'])
        countU+=1
    
    


print("")
print("Disagreed :",countD)
print("Agreed :",countA)
print("Unrelated :",countU)
