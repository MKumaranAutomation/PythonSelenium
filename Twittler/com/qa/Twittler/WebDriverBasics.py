from selenium import webdriver

driver = webdriver.Chrome("/Volumes/D Drive/TopTechGurus/Trainings/PythonSelenium/Twittler/drivers/chromedriver")

driver.get("https://toptechgurus-tweet.vercel.app/")

title = driver.title
print(title)

textboxTitle = driver.find_element_by_xpath("//h2[@class = 'mb-6 text-center text-3xl font-extrabold text-gray-900']").text
print(textboxTitle)
assert "Your Tweet" in textboxTitle

driver.close()