import matplotlib
import matplotlib.pyplot as plt

od = 1
rad = od/2

pcswide=23
xList=[]
yList=[]
rList=[]

for i in range(pcswide):
    xList.append(rad + i*od +1.5)
for i in range(pcswide):
    yList.append(rad+1.5)
for i in range(pcswide):
    rList.append(rad)


fig, ax = plt.subplots()
plt.plot(xList, yList,linestyle='none')
plt.title('W1 galaxy cluster field')
plt.xlabel(r'$\vartheta$ (arcmins)')
plt.ylabel(r'$\vartheta$ (arcmins)')
for i in range(len(xList)):
    circle1 = plt.Circle((xList[i], yList[i]), rList[i],facecolor='none', edgecolor='k')
    ax.add_artist(circle1)

plt.axis("equal")

#plt.savefig("test.svg", format="svg")
plt.show()
