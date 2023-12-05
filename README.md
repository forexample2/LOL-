# LOL台服拳头直营服账号批量注册

LOL台服拳头直营服账号批量注册
1. 前提需要大量的邮箱，可以某宝买到，或者用注册机自己注册
2. 还需要前置批量生成随机资料到excel，代码见另一个文件
3. 大陆应该需要梯子
4. 算上网页加载实际注册一个大约需要30来秒


使用方法：
1. 注册N多个邮箱（略）
2. 执行prerandom.py生成300个随机资料
3. 将上述生成的generated_data_updated_text_format.xlsx资料填写到account.xlsx对应位置中，包括自己的N多个邮箱
4. 注册https://yescaptcha.com/i/1Trl4h， 跟客服要测试的1500点数， chrome浏览器安装https://chromewebstore.google.com/detail/yescaptcha-%E4%BA%BA%E6%9C%BA%E5%8A%A9%E6%89%8B/jiofmdifioeejeilfkpegipdjiopiekl?hl=zh-CN插件
5. 配置填写你的ClientKey
6. 修改自己的配置，conda环境导入autoaccount_env.yaml，修改其他配置，执行yeshcha.py，（安装缺失的模块，缺失chromedriver，指定自己本机的路径），测试运行

注册完之后就可以刷等级买罐子送皮肤啦


###### 基本都是hcaptcha类型的图片验证码，对于没多少量的小号来说，免费测试的也基本够用啦
