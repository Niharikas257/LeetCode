class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # hand.sort()
        hand_count = Counter(hand)
        # hand_count.sort()

        for value in sorted(hand_count):
            c = hand_count[value]
            if c > 0:
                for next_value in range(value, value+groupSize):
                    if next_value not in hand_count or hand_count[next_value] < c:
                        return False
                    hand_count[next_value] -= c
        return True





        
        
        