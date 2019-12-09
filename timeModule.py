import time
def calcProd():
    product = 0
    for i in range(1, 100000):
        product = product + i
    return product


startTime = time.time()
prod = calcProd
endTime = time.time()
print('The Result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))
