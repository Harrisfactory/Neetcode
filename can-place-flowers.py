class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        #going to use trident method while also checking for edges

        for i in range(len(flowerbed)):
            if n == 0:
                return True
            #our current location is a potential position
            if flowerbed[i] == 0:
                #check left, is it a wall or 0?
                if i - 1 < 0 or flowerbed[i - 1] == 0:
                    #check right, is it a wall, or 0?
                    if i + 1 > len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n-=1
                        if n == 0:
                            return True
        if n == 0:
            return True
        return False
