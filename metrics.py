import matplotlib.pyplot as plt
import numpy as np

filename = 'horse_batch4.txt'
Gfile = open(filename, 'r')
Epochs = dict()
lossDA = dict()
lossGA = dict()
losscA = dict()
lossiA = dict()
lossDB = dict()
lossGB = dict()
losscB = dict()
lossiB = dict()
for line in Gfile:
    line = line.split()
    #print(line)
    epochs = line[1].split(',')

    if epochs[0] not in Epochs:
        try :
            n = int(epochs[0])
            Epochs[epochs[0]]=1
            lossDA[epochs[0]]=0
            lossGA[epochs[0]]=0
            losscA[epochs[0]]=0
            lossiA[epochs[0]]=0
            lossDB[epochs[0]]=0
            lossGB[epochs[0]]=0
            losscB[epochs[0]]=0
            lossiB[epochs[0]]=0
        except :
            pass
    else:
        Epochs[epochs[0]]+=1
    for i in range(len(line)):
        if line[i] == 'D_A:':
            lossDA[epochs[0]]+=float(line[i+1])
        if line[i] == 'G_A:':
            lossGA[epochs[0]]+=float(line[i+1])
        if line[i] == 'cycle_A:':
            losscA[epochs[0]]+=float(line[i+1])
        if line[i] == 'idt_A:':
            lossiA[epochs[0]]+=float(line[i+1])
        if line[i] == 'D_B:':
            lossDB[epochs[0]]+=float(line[i+1])
        if line[i] == 'G_B:':
            lossGB[epochs[0]]+=float(line[i+1])
        if line[i] == 'cycle_B:':
            losscB[epochs[0]]+=float(line[i+1])
        if line[i] == 'idt_B:':
            lossiB[epochs[0]]+=float(line[i+1])


    #print(line.split())
print(Epochs)
print(lossiA)
for u in lossDA:
    lossDA[u]=lossDA[u]/Epochs[u]

for u in lossGA:
    lossGA[u]=lossGA[u]/Epochs[u]

for u in losscA:
    losscA[u]=losscA[u]/Epochs[u]

for u in lossiA:
    lossiA[u]=lossiA[u]/Epochs[u]

for u in lossDB:
    lossDB[u]=lossDB[u]/Epochs[u]

for u in lossGB:
    lossGB[u]=lossGB[u]/Epochs[u]

for u in losscB:
    losscB[u]=losscB[u]/Epochs[u]

for u in lossiB:
    lossiB[u]=lossiB[u]/Epochs[u]

X = []
Y = []
X2 = []
Y2 = []
X3 = []
Y3 = []
X4 = []
Y4 = []
X_ = []
Y_ = []
X2_ = []
Y2_ = []
X3_ = []
Y3_ = []
X4_ = []
Y4_ = []
for key,value in lossDA.items():
    X.append(key)
    Y.append(value)
for key,value in lossGA.items():
    X2.append(key)
    Y2.append(value)
for key,value in losscA.items():
    X3.append(key)
    Y3.append(value)
for key,value in lossiA.items():
    X4.append(key)
    Y4.append(value)
for key,value in lossDB.items():
    X_.append(key)
    Y_.append(value)
for key,value in lossGB.items():
    X2_.append(key)
    Y2_.append(value)
for key,value in losscB.items():
    X3_.append(key)
    Y3_.append(value)
for key,value in lossiB.items():
    X4_.append(key)
    Y4_.append(value)

n_epochs = len(Epochs)
#ticks = [0,4,9,14,19,24,29,34,39,44,49]
ticks = [0,4,9,14,19]
#ticks = [0, 49, 99, 149 , 199]
fig, axs = plt.subplots(2, 4)

axs[0,0].plot(X,Y)
axs[0,0].set_title("D_A loss on "+str(n_epochs)+" epochs")
axs[0,0].set_xticks(ticks)

axs[0,1].plot(X2,Y2)
axs[0,1].set_title("G_A loss on "+str(n_epochs)+" epochs")
axs[0,1].set_xticks(ticks)

axs[1,0].plot(X3,Y3)
axs[1,0].set_title("cycle_A loss on "+str(n_epochs)+" epochs")
axs[1,0].set_xticks(ticks)

axs[1,1].plot(X4,Y4)
axs[1,1].set_title("idt_A loss on "+str(n_epochs)+" epochs")
axs[1,1].set_xticks(ticks)

axs[0,2].plot(X_,Y_)
axs[0,2].set_title("D_B loss on "+str(n_epochs)+" epochs")
axs[0,2].set_xticks(ticks)

axs[0,3].plot(X2_,Y2_)
axs[0,3].set_title("G_B loss on "+str(n_epochs)+" epochs")
axs[0,3].set_xticks(ticks)

axs[1,2].plot(X3_,Y3_)
axs[1,2].set_title("cycle_B loss on "+str(n_epochs)+" epochs")
axs[1,2].set_xticks(ticks)

axs[1,3].plot(X4_,Y4_)
axs[1,3].set_title("idt_B loss on "+str(n_epochs)+" epochs")
axs[1,3].set_xticks(ticks)
plt.show()
