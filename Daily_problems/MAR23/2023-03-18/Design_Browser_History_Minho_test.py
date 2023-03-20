from Design_Browser_History_Minho import BrowserHistory


def test_browser_history():
    # create a browser history object
    browser = BrowserHistory("https://www.google.com")

    # check if the current step is 0
    assert browser.curr_step == 0

    # visit a URL and check if the current step is 1
    browser.visit("https://en.wikipedia.org")
    assert browser.curr_step == 1

    # visit another URL and check if the current step is 2
    browser.visit("https://github.com")
    assert browser.curr_step == 2

    # go back one step and check if the current step is 1
    assert browser.back(1) == "https://en.wikipedia.org"
    assert browser.curr_step == 1

    # go forward one step and check if the current step is 2
    assert browser.forward(1) == "https://github.com"
    assert browser.curr_step == 2

    # go back two steps and check if the current step is 0
    assert browser.back(2) == "https://www.google.com"
    assert browser.curr_step == 0

    # try to go back one more step and check if the current step is still 0
    assert browser.back(1) == "https://www.google.com"
    assert browser.curr_step == 0
