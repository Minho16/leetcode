class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pointer = 0
        self.size = 1

    def visit(self, url: str) -> None:
        self.history = self.history[:self.pointer+1]
        self.history.append(url)
        self.pointer += 1
        self.size = self.pointer+1

    def back(self, steps: int) -> str:
        self.pointer = max(0, self.pointer-steps)
        return self.history[self.pointer]


    def forward(self, steps: int) -> str:
        self.pointer = min(self.pointer+steps, self.size-1)
        return self.history[self.pointer]
