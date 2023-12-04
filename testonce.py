from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''
这段只是我刚开始摸索用的单条测试（可以不用看）
'''

# 创建一个新的 WebDriver 对象
chrome_driver_path = r'D:\py\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# 打开指定的网址
url = "https://auth.riotgames.com/login#_gl=1%2A1a8iog%2A_ga%2AMTMyODU0NDM5My4xNjk3NzczODk5%2A_ga_0X9JWXB87B%2AMTcwMTY1NDU5MC4xMi4xLjE3MDE2NTk5ODMuMC4wLjA.&acr_values=urn%3Ariot%3Agold&client_id=accountodactyl-prod&prompt=signup&redirect_uri=https%3A%2F%2Faccount.riotgames.com%2Foauth2%2Flog-in&response_type=code&scope=openid%20email%20profile%20riot%3A%2F%2Friot.atlas%2Faccounts.edit%20riot%3A%2F%2Friot.atlas%2Faccounts%2Fpassword.edit%20riot%3A%2F%2Friot.atlas%2Faccounts%2Femail.edit%20riot%3A%2F%2Friot.atlas%2Faccounts.auth%20riot%3A%2F%2Fthird_party.revoke%20riot%3A%2F%2Fthird_party.query%20riot%3A%2F%2Fforgetme%2Fnotify.write%20riot%3A%2F%2Friot.authenticator%2Fauth.code%20riot%3A%2F%2Friot.authenticator%2Fauthz.edit%20riot%3A%2F%2Frso%2Fmfa%2Fdevice.write%20riot%3A%2F%2Friot.authenticator%2Fidentity.add&state=02907a95-123b-42ae-b774-56adb7592791&ui_locales=zh-MY"
driver.get(url)

# 等待页面加载完成
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]')))

# 找到页面上第一个电子邮件输入框
email_input = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')

# 输入邮箱地址并按回车
email_input.send_keys("gdsfd@163.com")  # 替换为你想要填写的邮箱
time.sleep(2)
email_input.send_keys(Keys.RETURN)

# 等待日输入框加载完成
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="date_of_birth_day"]')))

# 找到日、月、年的输入框
day_input = driver.find_element(By.CSS_SELECTOR, 'input[name="date_of_birth_day"]')
month_input = driver.find_element(By.CSS_SELECTOR, 'input[name="date_of_birth_month"]')
year_input = driver.find_element(By.CSS_SELECTOR, 'input[name="date_of_birth_year"]')

# 填写日、月、年
day_input.send_keys("12")  # 替换为你想要填写的日
month_input.send_keys("01")  # 替换为你想要填写的月
year_input.send_keys("1959")  # 替换为你想要填写的年
time.sleep(2)
# 按回车
year_input.send_keys(Keys.RETURN)

# 等待用户名输入框加载完成
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]')))

# 找到用户名输入框
username_input = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')

# 输入用户名并按回车
username_input.send_keys("rfdvdfdF")  # 替换为你想要填写的用户名
time.sleep(2)
username_input.send_keys(Keys.RETURN)


# 等待密码输入框加载完成
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))

# 找到密码输入框和确认密码输入框
password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
confirm_password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="confirm_password"]')

# 输入密码和确认密码并按回车
password_input.send_keys("yO643Qx")  # 替换为你想要填写的密码
confirm_password_input.send_keys("yO643Qx")  # 替换为你想要填写的确认密码
time.sleep(2)
# 找到下一步按钮
next_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="btn-signup-submit"]')

# 点击下一步按钮
ActionChains(driver).move_to_element(next_button).click().perform()

# 这一步可能会存在图像验证，一般是获取出现一次的对象，手工？？？


# 等待 Riot ID 输入框加载完成
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="riot-id__riotId"]')))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="riot-id__riotId"]')))


# 找到 Riot ID 输入框
riot_id_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="riot-id__riotId"]')

# 输入姓名
riot_id_input.send_keys("erffst")  # 替换为你想要填写的姓名

# 等待 Riot ID 标语输入框加载完成
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="riot-id__tagline"]')))

# 找到 Riot ID 标语输入框
tagline_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="riot-id__tagline"]')

# 输入标语
tagline_input.send_keys("5753")  # 替换为你想要填写的标语

# 找到保存更改按钮
save_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="riot-id__save-btn"]')

# 点击保存更改按钮
ActionChains(driver).move_to_element(save_button).click().perform()



# 关闭浏览器
driver.quit()
