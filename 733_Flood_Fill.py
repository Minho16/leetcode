class Solution:
    def __init__(self):
        self.image = None
        self.initial_color = None
        self.color_to_be_changed = None

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        self.initial_color = image[sr][sc]
        self.color_to_be_changed = color

        if self.initial_color == color: 
            return image
        else:
            self.image = image
            self.image[sr][sc] = color
            self.DFS(x=sr, y=sc)
            return self.image

    def DFS(self, x, y):
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        for idx in range(len(dx)): 
            new_x = x + dx[idx]
            new_y = y + dy[idx]

            if new_x >= 0 and new_x < len(self.image) and new_y >= 0 and new_y < len(self.image[0]): 
                if self.image[new_x][new_y] == self.initial_color: 
                    self.image[new_x][new_y] = self.color_to_be_changed
                    self.DFS(new_x, new_y)                    
                else:
                    continue