from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

un = ""
pw = ""

#Mihraz
reels = "https://www.instagram.com/reel/Cyh3ce2yTTz/?utm_source=ig_web_copy_link"

#Project 1
# reels = "https://www.instagram.com/reel/Cz3tmkIyZd6/?utm_source=ig_web_copy_link"

#Project 2
# reels = "https://www.instagram.com/reel/Cz_Vmv3ymjn/?utm_source=ig_web_copy_link"

urls = ["https://bayitakipci.com/memberlogin",
        "https://takipcigir.com/login",
        "https://fastfollow.in/member",
        "https://www.takipcibase.com/login",
        "https://www.takipciking.com/member",
        "https://takipciking.net/login",
        "https://takipcizen.com/login",
        "https://takipcihilesico.com/login",
        "https://takipcimx.net/login",
        "https://takipcimax.com/login",
        "https://instamoda.org/login",
        "https://takipcitime.com/login",
        "https://takipcikrali.com/login",
        "https://birtakipci.com/member"]

count = 0

while True:
    time.sleep(4000)
    count = count + 1
    print(f"Running cycle: {str(count)}")
    # Loop through each URL
    for url in urls:
        # Step 1: Open Chrome
        driver = webdriver.Chrome()

        # Step 2: Go to the website "www.abcd.com"
        driver.get(url)

        try:
            # Step 4: Click on the username field
            # username_field = driver.find_element(By.NAME, "username")
            username_field = driver.find_element(By.XPATH, "//input[@placeholder='Kullanıcı adı']")
            username_field.click()

            # Step 5: Type username "malu"
            username_field.send_keys(un)

            # Step 6: Click on the password field
            # password_field = driver.find_element(By.NAME, "password")
            password_field = driver.find_element(By.XPATH, "//input[@placeholder='Şifre']")
            password_field.click()

            # Step 7: Type password "malu"
            password_field.send_keys(pw)

            # Step 8: Click on the login button
            login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Giriş yap')]")
            login_button.click()
            time.sleep(8)
            try:
                login_button.click()
            except Exception as e:
                # Handle any other unexpected exception
                print(f"An unexpected error occurred: {str(e)}")


            # Optional: Pause to observe the automation (you can remove this in a production script)
            time.sleep(5)

            # Use ActionChains to move the mouse outside the pop-up and click
            action = ActionChains(driver)
            action.move_by_offset(0, 500).click().perform()

            # Step 9: Click on the element with class "fa fa-eye"
            eye_icon = driver.find_element(By.CSS_SELECTOR, ".fa-eye")
            eye_icon.click()

            # Step 10: Click on the text field with a placeholder matching "https://www.instagram.com"
            instagram_field = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'https://www.instagram.com')]")
            instagram_field.click()

            # Step 11: Type "url" into the text field
            instagram_field.send_keys(reels)

            # Step 12: Submit the form (assuming hitting Enter submits the form)
            instagram_field.send_keys(Keys.RETURN)

            time.sleep(5)

            # Step 13: Click on the text field with a placeholder matching "https://www.instagram.com"
            view_count_field = driver.find_element(By.XPATH, "//input[contains(@placeholder, '10')]")
            view_count_field.click()

            # Step 14: Type "url" into the text field
            view_count_field.clear()
            view_count_field.send_keys('1000')

            # Step 15: Submit the form
            submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Gönderimi Başlat')]")
            submit_button.click()

            time.sleep(10)

            print(f"Completed: {str(url)}")

        except Exception as e:
            # Handle any other unexpected exception
            print(f"An unexpected error occurred: {str(e)}")

        # Step 16: Close the browser
        driver.quit()

    print(f"Completed cycle: {str(count)}")
