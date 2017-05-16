import matplotlib.pyplot as plt
from records import records
import math

#print recordList
subpops = []
smallfrac = 0.0001 #to avoid logs of 0

for allele in records:
    #atts = allele
    for key, value in allele.iteritems():
        subPopDict = value['pops']
        subpops.append(subPopDict)

bestTest = subpops[2]
keyList = bestTest.keys()
keyList.sort()

print keyList
yAC = []
yAN = []

for k in keyList:
    popTup = bestTest[k]
    print popTup

    for i in popTup[0]:
        #print type(log(i))
        yAC.append(float(i))
    yAN.append(float(popTup[1]))

yFrac = []
for yindex in range(0, 7):
    yFrac.append(yAC[yindex]/yAN[yindex])

print yFrac
# firstrec = records[0]
# for item in firstrec:
#     print item.values()

xAC = [0, 1, 2, 3, 4, 5, 6]
#y = [6, 7, 8, 9, 4, 9]

#xAN = [0, 1, 2, 3, 4, 5, 6]
#y2 = [1, 3, 4, 2, 1, 4]


fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
ax1.bar(xAC, yFrac, label= 'Bars1', color='salmon')
keyList.append('aaa')
keyList.sort()
ax1.set_xticklabels(keyList)
#plt.bar(xAN, yAN, label='Bars2', color='c')

rects = ax1.patches
labels = []

for it in yAN:
    labels.append(str(it))

for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom')

plt.xlabel('subpopulations')
plt.ylabel('ExAC Allele Frequency (Caclulated)')

plt.show()