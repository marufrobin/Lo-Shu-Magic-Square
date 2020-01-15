
magicnumber = [[2,7,6],
               [9,5,1],
               [4,3,8]]
print('Input Matrix: ')
#printing the matrix input
for row in magicnumber:
    print(row)


#ROW SUM 
rowsum = [0 for x in range(len(magicnumber))]
for rowIndex , row in enumerate(magicnumber):
    for num in row:
        rowsum[rowIndex] += num



#COLUM SUM
columsum = [0 for x in range(len(magicnumber))]
for row in magicnumber:
    for index in range(len(magicnumber)):
        columsum[index] += row[index]



#digonal sum (left to right digonal sum)
digonalsum = 0
for i in range(len(magicnumber)):
    digonalsum += magicnumber[i][i]



#another digonal sum(right to left digonal sum)
for x in range(len(magicnumber)):
    for y in range(len(magicnumber)):
        if x==0 and y==2:
            r1=magicnumber[x][y]
        if x==2 and y==0:
            r2=magicnumber[x][y]
        if x==1 and y==1:
            r=magicnumber[x][y]
anotherdigonalsum = r+r1+r2 #another digonal sum (from right to left)

print(digonalsum)
print(anotherdigonalsum)
#checking that row sum, colum sum, digonal sum, another digonal are same 
if rowsum[0]==columsum[0]==digonalsum==anotherdigonalsum:
    print("This is a Lo Shu Magic Square.")
    n=len(magicnumber)
    print("And, The magic number is ",n*(n**2+1)/2)