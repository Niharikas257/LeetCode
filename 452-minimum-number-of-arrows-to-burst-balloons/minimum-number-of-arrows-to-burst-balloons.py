class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # if points is None:
        #     return 0
        points.sort(key = lambda x:x[1]) # sort the array based on the end value, 0 indexed.

        arrow_count = 1 # we always need one arrow unless the points is empty
        arrow_pos = points[0][1] # first arrow at the end of the first balloon

        for new_start, new_end in points:
            if new_start<=arrow_pos and arrow_pos <= new_end:
                continue # Because the balloons overlap so we do not need one more arrow
            else:
                arrow_count += 1
                arrow_pos = new_end
        
        return arrow_count




