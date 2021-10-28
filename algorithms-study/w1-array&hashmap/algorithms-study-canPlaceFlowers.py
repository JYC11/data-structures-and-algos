def canPlaceFlowers(flowerbed,n): #array
    if len(flowerbed) == 1:
        if flowerbed[0] == 0 and n > 0:
            flowerbed[0] = 1
            n -= 1
        return n == 0

    for i in range(len(flowerbed)):
        if n > 0:
            if i == 0:
                if flowerbed[i+1] != 1 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i == len(flowerbed)-1:
                if flowerbed[i-1] != 1 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1 
            elif flowerbed[i-1] != 1 and flowerbed[i+1] != 1 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        else:
            break
    return n == 0

print(canPlaceFlowers([1,0,0,0,1], 1))