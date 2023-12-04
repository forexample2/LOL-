from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
'''
感觉一个一个点有点慢，变成两个线程试试

太频繁会进行不下去，等几分钟就好
'''

# 读取 Excel 文件
excel_file = r"C:\Users\fd\PycharmProjects\pythonProject1\autoaccount\account.xlsx"  # 替换为你的 Excel 文件路径
df = pd.read_excel(excel_file)
# print(df.columns)
processed_rows = set()  # 记录已处理的行

# 记录每个线程的窗口位置
window_positions = [(0, 0), (810, 0)]  # 在屏幕上的 x, y 坐标，可以根据需要调整

# 遍历每一行
def process_row(index, row):
    global window_positions

    # 获取当前线程的窗口位置
    window_position = window_positions.pop(0)

    chrome_driver_path = r'D:\py\chromedriver-win64\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    # 设置窗口位置
    driver.set_window_position(*window_position)

    # 设置浏览器大小，实现缩放
    driver.set_window_size(int(driver.get_window_size()['width'] * 0.9), int(driver.get_window_size()['height'] * 0.9))

    start_time = time.time()

    # 打开注册的网址,这个拳头网址第一次要手动去页面拉取下，会过期
    url = "https://auth.riotgames.com/login#_gl=1%2A1a8iog%2A_ga%2AMTMyODU0NDM5My4xNjk3NzczODk5%2A_ga_0X9JWXB87B%2AMTcwMTY1NDU5MC4xMi4xLjE3MDE2NTk5ODMuMC4wLjA.&acr_values=urn%3Ariot%3Agold&client_id=accountodactyl-prod&prompt=signup&redirect_uri=https%3A%2F%2Faccount.riotgames.com%2Foauth2%2Flog-in&response_type=code&scope=openid%20email%20profile%20riot%3A%2F%2Friot.atlas%2Faccounts.edit%20riot%3A%2F%2Friot.atlas%2Faccounts%2Fpassword.edit%20riot%3A%2F%2Friot.atlas%2Faccounts%2Femail.edit%20riot%3A%2F%2Friot.atlas%2Faccounts.auth%20riot%3A%2F%2Fthird_party.revoke%20riot%3A%2F%2Fthird_party.query%20riot%3A%2F%2Fforgetme%2Fnotify.write%20riot%3A%2F%2Friot.authenticator%2Fauth.code%20riot%3A%2F%2Friot.authenticator%2Fauthz.edit%20riot%3A%2F%2Frso%2Fmfa%2Fdevice.write%20riot%3A%2F%2Friot.authenticator%2Fidentity.add&state=02907a95-123b-42ae-b774-56adb7592791&ui_locales=zh-MY"
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
    # time.sleep(2)
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

    # 这一步可能会提示重复用户名，手动随便加个后缀吧，反正验证码都得守着，懒得处理

    # 这一步每次会存在图像验证，一般是获取出现一次的对象，找动物的头，手工？？？ 手点确实比较快

    # 等待 Riot ID 输入框加载完成
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="riot-id__riotId"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="riot-id__riotId"]')))

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

    time.sleep(1)   # 我怕看不清

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
    print("当前行数据: ", index + 2)
    print(f"保存成功:", current_row_data)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"本次循环实际耗时: {elapsed_time} 秒")

    # 将已处理的行加入集合
    processed_rows.add(index)

    # 关闭浏览器后，开始下一轮循环
    driver.quit()
    # 将当前窗口位置添加回列表，以便下次使用
    window_positions.append(window_position)

def run_threads(thread_count):
    # 创建 ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        futures = []

        for index, row in df.iterrows():
            # 如果行已经处理过，则跳过
            if index in processed_rows:
                continue

            # 提交任务给线程池
            future = executor.submit(process_row, index, row)
            futures.append(future)

            # 控制最大执行线程数
            while len(futures) >= thread_count:
                for completed_future in futures:
                    if completed_future.done():
                        futures.remove(completed_future)

                time.sleep(1)

# 启动线程池
run_threads(2)
