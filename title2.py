import urllib.request
req=urllib.request

#ù��° ���̺��� å ���� ��������
d1=req.urlopen("https://www.gutenberg.org/cache/epub/8009/pg8009.txt")
en1=d1.read()
en1=en1.decode('utf-8')

#�ι�° ���̺��� å ���� ��������
d2=req.urlopen("https://www.gutenberg.org/cache/epub/8010/pg8010.txt")
en2=d2.read()
en2=en2.decode('utf-8')

#ù��° ���̺��� �繫���� ���̺���� �̸� �󵵼� ������ �׷���
import matplotlib.pyplot as plt
for a,b in zip(re.finditer('Samuel',en1),re.finditer('David',en1)):
    x1=a.start()
    x2=b.start()
    plt.scatter(x1,y=1,c="blue",alpha=0.2)
    plt.scatter(x2,y=1,c="red",alpha=0.2)
plt.show()

#�ι�° ���̺��� �繫���� ���̺���� �̸� �󵵼� ������ �׷���
for a in re.finditer('Samuel',en2):
    x=a.start()
    plt.scatter(x,y=1,c="black")
plt.show()

for a in re.finditer('David',en2):
    x=a.start()
    plt.scatter(x,y=1,c="red")
plt.show()