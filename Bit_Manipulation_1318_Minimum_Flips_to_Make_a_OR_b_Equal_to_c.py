# Reference: https://www.youtube.com/watch?v=oLZL8dheuzc&ab_channel=Pepcoding


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32):  # Loop through 32 bits for an integer
            ai, bi, ci = False, False, False
            if (a & (1 << i)) > 0:  # Check if ith bit is set in a
                ai = True
            if (b & (1 << i)) > 0:  # Check if ith bit is set in b
                bi = True
            if (c & (1 << i)) > 0:  # Check if ith bit is set in c
                ci = True

            # Logic to determine the number of flips needed
            if ci:
                if not ai and not bi:
                    ans += 1
            else:
                if ai and bi:
                    ans += 2
                elif ai or bi:
                    ans += 1

        return ans

        # return ((a | b) ^ c).bit_count() + (a & b & ((a | b) ^ c)).bit_count()

        # return bin(c & ~a & ~b).count("1") + bin(~c & a).count("1") + bin(~c & b).count("1")
