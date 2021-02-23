from selenium import webdriver

# Navigate to the web site
browser = webdriver.Chrome()
browser.get("https://lesica.com/missing-course/")

# Open the Topics page
topics_link = browser.find_element_by_link_text("topics/")
topics_link.click()

# Verify that the heading is "Topics"
heading = browser.find_element_by_tag_name("h1")
assert heading.text == "Topics"

#browser.quit()

