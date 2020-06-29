import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def getLines(nameFile):
    f = open(nameFile,'r',encoding="UTF-8")
    lines = f.read().split('\n')
    f.close()
    return lines[3::]


lines = getLines('Население-по-возрастам.txt')




labels = []
men_means = []
women_means = []
for line in lines:
    labels.append(line.split(";")[0])
    men_means.append(int(line.split(";")[2]))
    women_means.append(int(line.split(";")[3]))



x = np.arange(len(labels)) 
width = 0.4

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Мужчины')
rects2 = ax.bar(x + width/2, women_means, width, label='Женщины')


ax.set_ylabel('Численность')
ax.set_title('Распределение по возрасту и полу')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
fig.set_figwidth(16); fig.set_figheight(8)
plt.show()