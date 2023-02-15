class Solution:
    def __init__(self):
        self.image = None
        self.image_copy = None
        self.initial_color = None
        self.color_to_be_changed = None
        self.visited = None

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        self.initial_color = image[sr][sc]
        self.color_to_be_changed = color

        if self.initial_color == color: # --> No change is detected
            return image
        else:
            self.image = image
            self.image_copy = image
            self.image_copy[sr][sc] = color
            self.visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
            self.visited[sr][sc] = True 
            self.DFS(x=sr, y=sc)
            return self.image

    def DFS(self, x, y):
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        for idx in range(len(dx)): # check 4 directional positions
            new_x = x + dx[idx]
            new_y = y + dy[idx]

            if new_x >= 0 and new_x < len(self.image) and new_y >= 0 and new_y < len(self.image[0]): # if the next pixel is within the grid
                if self.visited[new_x][new_y] == False: # only handle non-visited grids
                    if self.image[new_x][new_y] == self.initial_color: # only handle those cells that have same initial_color
                        # if any of the connected cells must have the initial color
                        self.image[new_x][new_y] = self.color_to_be_changed
                        self.DFS(new_x, new_y)                    
                else:
                    continue


image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
color = 0


s = Solution()
print(s.floodFill(image, sr, sc, color))