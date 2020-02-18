import numpy
#fisrt task
size=int(input("Введите максимальное количество чисел\n"))
count=0
for i in range(1,size+1):
    for j in range(i):
        count+=1
        if count>size:
            break
        else:
            print(i, end=' ')
    if count>size:
        break
#second task
listOfInt=[]
inint=0
real=True
print()
while real==True:
    inint=int(input("Введите число, отличное от нуля\nВведите 0 для завершения введения\n"))
    if inint!=0:
        listOfInt.append(inint)
    else:
        break
searchNumber=int(input("Введите число для поиска\n"))
for i in range(len(listOfInt)):
    if listOfInt[i]==searchNumber:
        print(i+1)
        real=False
if real!=False:
    print("Отсутствует")
#third task
counter=0
lineofstr=[]
while True:
    lineofstr.append(input("Введите строку\n"));
    if lineofstr[counter]=="end":
        lineofstr.remove("end")
        break
    counter+=1
max=0;
for i in range(len(lineofstr)):
    now=len(lineofstr[i].split())
    if(now>max):
        max=now
matrix=[0]*len(lineofstr)
for i in range(len(lineofstr)):
    matrix[i]=[0]*max
for i in range(len(lineofstr)):
    now=lineofstr[i].split()
    for j in range(len(now)):
        matrix[i][j]=int(now[j])
copyoflines=[0]*len(lineofstr)
for i in range(len(lineofstr)):
    copyoflines[i]=[0]*max
for i in range(len(matrix)):
    nowline=matrix[i]
    for j in range(len(nowline)):
        copyoflines[i][j]=nowline[j]
for i in range(len(copyoflines)):
    nowline=copyoflines[i]
    for j in range(len(nowline)):
        if i==0 and j==0:
            copyoflines[i][j]=matrix[i+1][j]+matrix[i][j+1]+matrix[len(copyoflines)-1][j]+matrix[i][len(nowline)-1]
        elif i==0 and j==len(nowline)-1:
            copyoflines[i][j]=matrix[i][0]+matrix[len(copyoflines)-1][j]+matrix[i][j-1]+matrix[i+1][j]
        elif i==len(copyoflines)-1 and j==0:
            copyoflines[i][j]=matrix[0][j]+matrix[i-1][j]+matrix[i][len(nowline)-1]+matrix[i][j+1]
        elif i==0:
            copyoflines[i][j]=matrix[len(copyoflines)-1][j]+matrix[i+1][j]+matrix[i][j-1]+matrix[i][j+1]
        elif j==0:
            copyoflines[i][j]=matrix[i][len(nowline)-1]+matrix[i+1][j]+matrix[i][j+1]+matrix[i-1][j]
        elif i==len(copyoflines)-1 and j==len(nowline)-1:
            copyoflines[i][j]=matrix[i-1][j]+matrix[i][j-1]+matrix[i][0]+matrix[0][j]
        elif i==len(copyoflines)-1:
            copyoflines[i][j]=matrix[i-1][j]+matrix[i][j+1]+matrix[i][j-1]+matrix[0][j]
        elif j==len(nowline)-1:
            copyoflines[i][j]=matrix[i+1][j]+matrix[i-1][j]+matrix[i][j-1]+matrix[i][0]
        else:
            copyoflines[i][j]=matrix[i+1][j]+matrix[i-1][j]+matrix[i][j+1]+matrix[i][j-1]
print("Исходная матрица")
for i in range(len(matrix)):
    print(matrix[i])
print("Результат изменений")
for i in range(len(copyoflines)):
    print(copyoflines[i])
#fourth task
sizeint=int(input("Введите размер матрицы\n"))
fmatrix=[0]*sizeint
for i in range(sizeint):
    fmatrix[i]=[0]*sizeint
i=0
k=0
j=0
p=1
while i<sizeint*sizeint:
    k+=1
    for j in range(k-1, sizeint-k+1):
        fmatrix[k-1][j]=p
        p+=1
        i+=1
    for j in range(k, sizeint-k+1):
        fmatrix[j][sizeint-k]=p
        p+=1
        i+=1
    for j in range(sizeint-k-1, k-2, -1):
        fmatrix[sizeint-k][j]=p
        p+=1
        i+=1
    for j in range(sizeint-k-1, k-1, -1):
        fmatrix[j][k-1]=p
        p+=1
        i+=1
for i in range(sizeint):
    for j in range(sizeint):
        print(fmatrix[i][j], end=' ')
    print()