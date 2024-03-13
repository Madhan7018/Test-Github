from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
import time

@allure.severity(allure.severity_level.NORMAL)
class TestGithub:
    @allure.severity(allure.severity_level.MINOR)
    def testGithub(self):
        print("Automation test Started!!!")
        self.driver = webdriver.Chrome()
        self.driver.get("https://github.com/login")
        username = self.driver.find_element(By.XPATH, '//*[@id="login_field"]')
        password = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        username.send_keys("madhan.a7018@gmail.com")
        password.send_keys("Madhan132003")
        enter = self.driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]')
        enter.send_keys(Keys.RETURN)
        time.sleep(3)

        self.driver.find_element(By.XPATH, '//*[@id="dashboard"]/div/feed-container/div[1]/div/a').click()
        time.sleep(5)

        hme = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[1]/a')
        hme.click()
        time.sleep(2)

        search = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div[1]/qbsearch-input/div[1]/div[1]/div/div/button/div')
        search.click()
        search1 = self.driver.find_element(By.XPATH, '//*[@id="query-builder-test"]')
        search1.send_keys("Login Page")
        search1.send_keys(Keys.RETURN)
        time.sleep(5)

        issue = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div[2]/a[1]')
        issue.click()
        time.sleep(3)

        notification = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/notification-indicator/a')
        notification.click()
        time.sleep(3)

        pull_request = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div[2]/a[2]')
        pull_request.click()
        time.sleep(3)

        hme = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[1]/a')
        hme.click()
        time.sleep(1)
        repo_search = self.driver.find_element(By.XPATH, '//*[@id="dashboard-repos-filter-left"]')
        repo_search.click()
        repo_search.send_keys("Software_Testing")
        time.sleep(3)

        repo = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div/aside/div/div/loading-context/div/div[1]/div/div[1]/a')
        repo.click()
        time.sleep(1)
        repo_name = self.driver.find_element(By.XPATH,'//*[@id=":r3:"]')
        repo_name.send_keys("Demo")
        time.sleep(1)
        repo_button = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/main/react-app/div/form/div[5]/button')
        repo_button.click()
        time.sleep(3)

        self.driver.get("https://github.com/Madhan7018/Demo")
        demo_repo = self.driver.find_element(By.XPATH,'//*[@id="settings-tab"]')
        demo_repo.click()
        time.sleep(1)
        del_repo = self.driver.find_element(By.XPATH,'//*[@id="dialog-show-repo-delete-menu-dialog"]')
        del_repo.click()
        time.sleep(1)
        del_repo1 = self.driver.find_element(By.XPATH,'//*[@id="repo-delete-proceed-button"]')
        del_repo1.click()
        time.sleep(1)
        del_repo2 = self.driver.find_element(By.XPATH,'//*[@id="repo-delete-proceed-button"]')
        del_repo2.click()
        time.sleep(1)
        repo_name = self.driver.find_element(By.XPATH,'//*[@id="verification_field"]')
        repo_name.send_keys("Madhan7018/Demo")
        repo_name.submit()
        time.sleep(1)

        self.driver.close()
        print("Browser Closed")
