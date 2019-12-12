# UCI WebReg Automator

**The out-of-the-box UCI WebReg Bot**

## Introduction
Designed for UC Irvine WebReg, 
WebReg Automator is a bot that helps you enroll in the courses you want.

Unlike other bots that are basically a piece of scripts, it is deeply integrated with WebReg and takes advantage of Selenium technology
which makes it robust, fast, and secure. 

However, using it is as simple as a few clicks. With an intuitive yet powerful GUI (under development), you do not need to 
write a single line of code. It is as easy as placing orders on ebay. 

For developers, WebReg Automator also provides well-designed APIs that allows user to manipulate WebReg via Python easily!

### Highlights
* **Secure.** The top priority is that you'll never get banned because of using bots. 
The bot simulates that a real person and a real browser would do so any kind of behavioral detection will not be able to distinguish you from other people.
* **Robust.** The bot keeps track of the WebReg login status. So it won't crash due to exceptions like maintenance or unopened enrollment window. 
* **Versatile.** The bot helps you not only enroll in classes, but also check study lists, waitlists, and so on.

## Prerequisite

* Chrome browser and Python 3.6+

## Roadmap

* Wrap up class enrollment
* Support Waitlists
* Set time interval
* Web-based GUI
* Course code queue
* Auto schedule management

## Deployment

* Install Selenium

```bash
pip3 install selenium
```

* Download WebDriver and make it executable

<https://sites.google.com/a/chromium.org/chromedriver/downloads>

```bash
chmod +x ./webdriver
```

* Make it yours

```bash
git clone https://github.com/maao666/UCI_WebReg_Automator.git
```

```python
form WebReg import WebReg

wr = WebReg(headless=False)
wr.login('UCInetID', 'Password')

#To be continue
```

## We humbly ask you for a star if this bot does help you.
