class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = bin(n)
        bin_n = bin_n[2:]
        res = ""
        len_bin = len(bin_n)
        for i in range(32):
            if i < len_bin:
                letter = bin_n[len_bin-1-i]
                res += letter
            else:
                res += "0"

        return int(res, 2)

    def reverseBits_leetCode(self, n: int) -> int:
        # Initialize the reversed number to 0
        reversed_num = 0

        # Iterate over all 32 bits of the given number
        for i in range(32):
            # Left shift the reversed number by 1 and add the last bit of the given number to it
            reversed_num = (reversed_num << 1) | (n & 1)
            # To add the last bit of the given number to the reversed number, perform an AND operation with the given number and 1
            n >>= 1

        # Return the reversed number
        return reversed_num

    def reverseBits_leetCode2(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = result << 1
            bit = n % 2
            result = result + bit
            n = n >> 1
        return result

if __name__ == '__main__':
    sol = Solution()
    # print(sol.reverseBits(1000))
    # print(sol.reverseBits("00000010100101000001111010011100"))
    # print(sol.reverseBits_leetCode(1000))
    print(sol.reverseBits_leetCode2(1000))
