# Python Automation
- Automation can be simply defined as the process or procedure that is performed with a base minimum of human assistance.
- In python automation is creating and time saving scripts that we written in python language.


- Install selenium using `pip install selenium --upgrade cryptography` command.
- Install chrome-driver using `sudo apt-get install chromium-chromedriver` command.

### time.sleep(<seconds>) - in selenium
- Time.sleep() suspends the execution of the current thread for the given number of seconds.
  The argument may be a floating point number to indicate more precise sleep time.
- The actual suspension time may be lessthan that requested becouse any cought signal will terminate the sleep() following execution of that signal's catching routine.

### implicitly_wait(<time_to_wait>)
- implicitly_wait() is to specify the amount of time the webdriver instance i.e. the driver should wait when searching for an element if it is not immediatly present in the html dom in terms of seconds  when trying to find an element or elements they are not immediatly available.