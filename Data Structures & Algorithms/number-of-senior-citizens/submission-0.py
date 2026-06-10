class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            clean = int(detail[11:13])
            if clean > 60:
                count += 1
            
        return count