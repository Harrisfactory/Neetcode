class Solution:
    def trap(self, height: List[int]) -> int:
        
        #its a 1d array so we might want to compute by incrementing/decrementing

        #we want to do a 2 pointer approach to act as our walls, we can loop between the walls and fill the elevation up to the shortest wall

        #close the walls until they intersect and I think we'll have our solution

        l, r = 0, len(height) - 1

        totalTrappedWater = 0

        seenWalls = set()

        while l < r:

            #check if either pointer is a non height wall
            if height[l] == 0:
                l+=1
                continue
            if height[r] == 0:
                r-=1
                continue

            lowestWall = min(height[l], height[r])
            #loop through the walls and fill with rain
            for i in range(l, r):
                #if our current point is lower than our lowest wall, tally and fill it
                if height[i] < lowestWall:
                    #tally
                    totalTrappedWater+=lowestWall-height[i]
                    #fill
                    height[i]=lowestWall
            heightChanged = False
            height_r_prev = height[r]
            height_l_prev = height[l]
            while not heightChanged and l < r:
                if height[l] > height_l_prev or height[r] > height_r_prev:
                    break
                if height[l] < height[r]:
                    height_l_prev = height[l]
                    l+=1
                elif height[l] > height[r]:
                    height_r_prev = height[r]
                    r-=1
                else:
                    height_l_prev = height[l]
                    height_r_prev = height[r]
                    l+=1
                    r-=1
            
        
        
        return totalTrappedWater
