class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Base case
        if n == 1:
            return "1"
        
        # Start with the sequence for n = 1
        current_seq = "1"
        
        # Generate terms from 2 to n
        for _ in range(n - 1):
            next_seq = []
            i = 0
            
            # Perform Run-Length Encoding (RLE)
            while i < len(current_seq):
                count = 1
                # Count consecutive identical characters
                while i + 1 < len(current_seq) and current_seq[i] == current_seq[i + 1]:
                    count += 1
                    i += 1
                
                # Append the count followed by the character
                next_seq.append(str(count) + current_seq[i])
                i += 1
                
            current_seq = "".join(next_seq)
            
        return current_seq
