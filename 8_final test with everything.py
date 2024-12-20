#Test finding words 2.0:

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
            if(Train[C][5]=="agreed" and count1<6000):
              L.append(C)
              limit-=1
              count1+=1
            if(Train[C][5]=="disagreed" and count2<6000):
              L.append(C)
              limit-=1
              count2+=1
            if(Train[C][5]=="unrelated" and count3<8000):
              L.append(C)
              limit-=1
              count3+=1
    #print(L)
    #L=[235062, 130975, 141962, 119531, 110506, 155781, 211922, 183365, 49363, 110159, 240514, 102923, 5706, 126066, 94135, 184044, 216792, 186134, 63579, 101287, 248170, 190149, 243306, 37173, 212784, 4032, 144469, 20048, 173985, 170983, 223135, 10069, 162129, 8616, 243463, 118722, 149157, 109768, 36560, 85310, 22349, 156694, 63234, 131827, 189267, 34319, 37647, 87351, 195287, 150774, 245576, 159250, 178007, 200325, 203563, 4452, 127951, 103217, 94012, 8424, 103893, 94136, 219159, 157533, 67833, 114374, 251632, 179088, 226789, 193982, 27646, 191196, 206170, 193382, 209149, 58338, 174595, 67324, 208848, 200308, 6385, 240568, 217211, 139094, 245695, 190284, 110129, 9268, 101002, 128307, 98457, 246014, 191147, 192893, 90728, 138300, 99924, 236328, 225249, 255146]
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
FALSE4=0
for line in train:
    if(len(line)>5):
      count=similarWords(line)
      DISA=testDisagreed(line) # test to find "rumor" or "rumour" in the message
      if (DISA or count>2):
        score=simScore(line)
        if(score>0.4 and DISA):
          if (line[5]=="disagreed"):
            TRUE1+=1
          else :
            FALSE1+=1
        elif(count>3 and score>0.4):
          if (line[5]=="agreed"):
            TRUE2+=1
          else :
            FALSE2+=1
            #print(count," ",score)
        else:
          if (line[5]=="unrelated"):
            TRUE3+=1
          else :
            FALSE3+=1
      else:
        if (line[5]=="unrelated"):
          TRUE3+=1
        else :
          FALSE4+=1
      

print("")
print("True :",TRUE1+TRUE2+TRUE3)
print("")
# there is a better explenation of the True1, False1, True2... in previous codes
print("True1 :",TRUE1)
print("False1 :",FALSE1)
print("True2 :",TRUE2)
print("False2 :",FALSE2)
print("True3 :",TRUE3)
print("False3 :",FALSE3)
print("False4 :",FALSE4)