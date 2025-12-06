class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])

        arrow_count = 1
        arrow_pos = points[0][1]

        for new_start, new_end in points[1:]:
            if new_start <= arrow_pos and arrow_pos<= new_end:
                continue
            else:
                arrow_count += 1
                arrow_pos = new_end
            
        return arrow_count
