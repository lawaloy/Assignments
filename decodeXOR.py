class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        
        xor_all = 0
        for idx in range(len(encoded)+2):
            xor_all ^= idx
            
        result = []
        adj_xor = 0
        for num in encoded:
            adj_xor ^= num
            xor_all ^= adj_xor
        result.append(xor_all)
        for num in encoded:
            result.append(result[-1]^num)
            
        return result
