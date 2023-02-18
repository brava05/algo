class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows = len(image)
        colums = len(image[0])
        oldColor = image[sr][sc]
        def floodNeibors(r,c):
            if image[r][c] == oldColor:
                image[r][c]=color
                if r>=1:
                    floodNeibors(r-1, c)
                if r<rows-1:
                    floodNeibors(r+1, c)
                if c>=1:
                    floodNeibors(r, c-1)
                if c<colums-1:
                    floodNeibors(r, c+1)
        floodNeibors(sr, sc)
        return image
        


if __name__ == "__main__":
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    sol = Solution()
    
    s = sol.floodFill(image, sr, sc, color)
    print(s)

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.