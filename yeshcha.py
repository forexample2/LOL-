import random
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd


# 读取 Excel 文件
excel_file = r"C:\Users\Benjamin\PycharmProjects\pythonProject1\autoaccount_1205\autoaccount\account.xlsx"  # 替换为你的 Excel 文件路径
df = pd.read_excel(excel_file)
# print(df.columns)


# 遍历每一行
for index, row in df.iterrows():
    start_time = time.time()

    # 每次创建一个新的 WebDriver 对象
    chrome_driver_path = r'C:\Users\Benjamin\PycharmProjects\pythonProject1\autoaccount_1205\autoaccount\chromedriver-win64\chromedriver.exe' # 这里需要填写自己本机的chromedriver路径
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=" + r"C:/Users/Benjamin/AppData/Local/Google/Chrome/User Data")  # 获取本地浏览器的插件等信息，chrome://version/查看个人资料路径，执行前关闭所有浏览器
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    # 打开注册的网址,这个拳头网址第一次要手动去页面拉取下，会过期
    url = "https://auth.riotgames.com/login#_gl=1%2A1r2mlj1%2A_ga%2AMjE5MTc5MDg3LjE3MDE3NTA2Mzg.%2A_ga_0X9JWXB87B%2AMTcwMTc1MDYzNy4xLjEuMTcwMTc1MDcyOC4wLjAuMA..&acr_values=urn%3Ariot%3Agold&client_id=accountodactyl-prod&prompt=signup&redirect_uri=https%3A%2F%2Faccount.riotgames.com%2Foauth2%2Flog-in&response_type=code&scope=openid%20email%20profile%20riot%3A%2F%2Friot.atlas%2Faccounts.edit%20riot%3A%2F%2Friot.atlas%2Faccounts%2Fpassword.edit%20riot%3A%2F%2Friot.atlas%2Faccounts%2Femail.edit%20riot%3A%2F%2Friot.atlas%2Faccounts.auth%20riot%3A%2F%2Fthird_party.revoke%20riot%3A%2F%2Fthird_party.query%20riot%3A%2F%2Fforgetme%2Fnotify.write%20riot%3A%2F%2Friot.authenticator%2Fauth.code%20riot%3A%2F%2Friot.authenticator%2Fauthz.edit%20riot%3A%2F%2Frso%2Fmfa%2Fdevice.write%20riot%3A%2F%2Friot.authenticator%2Fidentity.add&state=b2ebc778-8000-4a61-bcdb-8bea3a88290c&ui_locales=zh-MY"
    driver.get(url)

    email = str(row['Email'])
    day = str(row['Day'])
    month = str(row['Month'])
    year = str(row['Year'])
    username = str(row['Username'])
    password = str(row['Password'])
    riot_id = str(row['RiotID'])
    tagline = str(row['Tagline'])

    # 等待页面加载完成
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]')))

    # 找到页面上第一个电子邮件输入框
    email_input = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
    email_input.clear()
    # 输入邮箱地址并按回车
    email_input.send_keys(email) 
    email_input.send_keys(Keys.RETURN)

    # 等待日输入框加载完成
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="date_of_birth_day"]')))

    # 找到日、月、年的输入框
    day_input = driver.find_element(By.CSS_SELECTOR, 'input[name="date_of_birth_day"]')
    month_input = driver.find_element(By.CSS_SELECTOR, 'input[name="date_of_birth_month"]')
    year_input = driver.find_element(By.CSS_SELECTOR, 'input[name="date_of_birth_year"]')

    # 填写日、月、年
    day_input.clear()
    day_input.send_keys(day)
    month_input.clear()
    month_input.send_keys(month)
    year_input.clear()
    year_input.send_keys(year)
    # time.sleep(2)
    # 按回车
    year_input.send_keys(Keys.RETURN)

    # 等待用户名输入框加载完成
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]')))

    # 找到用户名输入框
    username_input = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')

    # 输入用户名并按回车
    username_input.clear()
    username_input.send_keys(username)
    # time.sleep(2)
    username_input.send_keys(Keys.RETURN)

    # 等待密码输入框加载完成
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))

    # 找到密码输入框和确认密码输入框
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    confirm_password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="confirm_password"]')
    password_input.clear()
    # 输入密码和确认密码并按回车
    password_input.send_keys(password)
    confirm_password_input.clear()
    confirm_password_input.send_keys(password)
    # time.sleep(2)

    # 找到下一步按钮
    next_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="btn-signup-submit"]')

    # 点击下一步按钮
    ActionChains(driver).move_to_element(next_button).click().perform()

    time.sleep(13)

    # 设置超时时间
    timeout = 20
    max_attempts = 10

    # 这一步每次会存在图像验证，这个验证器质量一般，以后找见好的再说
    # 计数器
    attempts = 0

    # Define the target URL
    target_url = "https://account.riotgames.com/"

    # 循环点击下一步按钮
    for attempts in range(max_attempts):
        try:
            # 等待15秒，检查是否跳转到目标URL
            WebDriverWait(driver, timeout).until(
                EC.url_to_be(target_url)
            )
            print("成功跳转到目标URL！")
            break  # 如果成功跳转，跳出循环

        except TimeoutException:
            # 如果在15秒内未跳转到目标URL，继续下一步
            print(f"第 {attempts + 1} 次等待超时，再次点击下一步按钮...")

            # 可能会存在重复用户名的情况，这里后面随便加点后缀就行啦
            try:
                # 查找页面元素，检测是否包含 '用户名必须独一无二'
                page_source = driver.page_source
                if '用户名必须独一无二' in page_source:
                    # 找到用户名输入框
                    username_input = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')

                    # 在用户名末尾添加两位随机数
                    random_number = str(random.randint(10, 99))
                    new_username = random_number

                    # 清空输入框并输入新的用户名
                    username_input.clear()
                    username_input.send_keys(new_username)
                    print(f"新用户名: {new_username}")

                # 再次点击下一步
                next_button.click()

            except StaleElementReferenceException:
                # 如果元素过时，捕获 StaleElementReferenceException 并继续
                print("元素过时，尝试重新查找元素...")
                continue

            # 每隔10秒循环点击一次下一步
            time.sleep(4)
        else:
            print("达到最大尝试次数，未成功跳转到目标URL。")

    # 等待 Riot ID 输入框加载完成
    WebDriverWait(driver, 360).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="riot-id__riotId"]')))

    # 找到 Riot ID 输入框
    riot_id_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="riot-id__riotId"]')
    riot_id_input.clear()
    # 输入姓名
    riot_id_input.send_keys(riot_id)

    # 等待 Riot ID 标语输入框加载完成
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="riot-id__tagline"]')))

    # 找到 Riot ID 标语输入框
    tagline_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="riot-id__tagline"]')
    tagline_input.clear()
    # 输入标语
    tagline_input.send_keys(tagline)

    # 找到保存更改按钮
    save_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="riot-id__save-btn"]')

    # 点击保存更改按钮
    ActionChains(driver).move_to_element(save_button).click().perform()

    # 显式等待页面加载完成，例如等待 Riot ID 输入框可见
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="riot-id__riotId"]')))

    # 获取当前行的数据
    current_row_data = {
        'Email': email,
        'Day': day,
        'Month': month,
        'Year': year,
        'Username': username,
        'Password': password,
        'RiotID': riot_id,
        'Tagline': tagline
    }

    # 查看进度，老年银防痴呆
    print(f"当前循环次数: {index + 1}  ;")
    print(f"保存成功:", current_row_data)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"本次循环实际耗时: {elapsed_time} 秒")

    time.sleep(3)

    print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
    # 关闭浏览器后，开始下一轮循环
    driver.quit()
    
    
