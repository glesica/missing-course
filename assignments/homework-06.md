# Homework 6

We're going to test a web page!

## Installing Selenium

First, you'll need a "driver". Different drivers are used to automate different
web browsers. I suggest ChromeDriver to automate Chrome.

On Ubuntu you should be able to install with the command
`sudo apt install chromium-chromedriver`.

On a Mac, if you have Homebrew installed, you can use the command
`brew install chromedriver`.

Otherwise, take a look at the instructions on this page:
<https://selenium-python.readthedocs.io/installation.html>.

Once you've done this, you can install the `selenium` package using Pip:
`pip3 install --user selenium`. If you are using a virtual environment (you
should), then `pip3 install selenium` will work. Note that we're using `pip3` to
ensure that we install Selenium for Python 3 as opposed to Python 2.

## Project

Choose a web site and then write a Selenium script similar to the one we looked
at in class to "test" three things about your chosen web site. Possibilities
include verifying the title of the page, that certain links exist, that an image
exists, and so on.

Use the `assert` function to create an assertion for each of the characteristics
you test.

Submit your Python script through Moodle.

