import urllib.request
req=urllib.request

#첫번째 바이블의 책 내용 가져오기
d1=req.urlopen("https://www.gutenberg.org/cache/epub/8009/pg8009.txt")
en1=d1.read()
en1=en1.decode('utf-8')

#두번째 바이블의 책 내용 가져오기
d2=req.urlopen("https://www.gutenberg.org/cache/epub/8010/pg8010.txt")
en2=d2.read()
en2=en2.decode('utf-8')

#첫번째 바이블에서 사무엘과 데이비드의 이름 빈도수 산점도 그래프
import matplotlib.pyplot as plt
for a,b in zip(re.finditer('Samuel',en1),re.finditer('David',en1)):
    x1=a.start()
    x2=b.start()
    plt.scatter(x1,y=1,c="blue",alpha=0.2)
    plt.scatter(x2,y=1,c="red",alpha=0.2)
plt.show()

#두번째 바이블에서 사무엘과 데이비드의 이름 빈도수 산점도 그래프
for a in re.finditer('Samuel',en2):
    x=a.start()
    plt.scatter(x,y=1,c="black")
plt.show()

for a in re.finditer('David',en2):
    x=a.start()
    plt.scatter(x,y=1,c="red")
plt.show()