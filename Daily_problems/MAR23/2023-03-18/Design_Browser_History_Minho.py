class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr_step = 0
        self.url_dictionary = {self.curr_step : homepage}
        self.steps_list = [self.curr_step]

    def visit(self, url: str) -> None:
        self.curr_step += 1
        if self.curr_step in self.url_dictionary.keys():
            for num in range(self.curr_step, len(self.steps_list)):
                del self.url_dictionary[num]
            self.steps_list = self.steps_list[:self.curr_step]
        self.url_dictionary[self.curr_step] = url
        self.steps_list.append(self.curr_step)

    def back(self, steps: int) -> str:
        if self.curr_step < steps:
            self.curr_step = 0
        else:
            self.curr_step -= steps
        return self.url_dictionary[self.curr_step]

    def forward(self, steps: int) -> str:
        if steps > len(self.steps_list) - 1 - self.curr_step:
            self.curr_step = len(self.steps_list) - 1
        else:
            self.curr_step += steps
        return self.url_dictionary[self.curr_step]


b = BrowserHistory('leetcode.com')
b.visit('google.com')
b.visit('facebook.com')
b.visit('youtube.com')
print(b.back(1))
print(b.back(1))
print(b.forward(1))
b.visit('linkedin.com')
print(b.forward(2))
print(b.back(2))
print(b.back(7))
