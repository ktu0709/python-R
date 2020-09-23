import matplotlib.pyplot as plt
hg=[180,190,170,165,176]
wg=[70,95,88,75,65]

plt.plot(wg,hg, label="line Graph")
plt.bar(wg,hg, label="stack bar graph")
plt.legend()
plt.rc('font',family='Malgun Gothic')
plt.title('체중별 신장')
plt.savefig('helth.jpg')
plt.show()
