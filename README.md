# Airobots Demo Project

全端自动化测试框架Airobots的演示项目。

Airobots整合了Airtest、RobotFramework、Selenium、Appium、HTTPRunner、Locust框架的方法，从而实现一套框架，能够进行全端的测试，统一执行入口和报告的输出。

目录结构说明：

    ├─Library                           # 测试相关自定义库
    ├─Resource                          # 测试相关资源文件
    │  ├─TestFiles
    │  └─TestSQL
    ├─Results                           # 测试报告存放目录
    ├─TestCases                          # 测试用例存放目录
    │  ├─APICase                        # API测试用例存放目录
    │  ├─WebCase                        # Web测试用例存放目录
    │  ├─AndroidCase                    # Android测试用例存放目录
    │  ├─IOSCase                        # IOS测试用例存放目录
    │  └─PageObjects                    # POM文件存放目录
    └─WebChrome                         # 浏览器远程客户端相关服务
        ├─SeleniumGrid
        └─WebDriver

使用前请先安装相关依赖包, 执行

```
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
```

运行Web测试，需要安装ChromeDriver，请自行下载安装，或安装node之后执行 `npm install -g chromedriver` 安装


## 执行测试 

Allure 报告
```
airobots -t api ./TestCases/APICase/ --alluredir=Results             # API测试
airobots -t web ./TestCases/WebCase/ --alluredir=Results             # Web测试
airobots -t android ./TestCases/AndroidCase/ --alluredir=Results     # Android测试
airobots -t ios ./TestCases/IOSCase/ --alluredir=Results             # IOS测试
```

HTML 报告
```
airobots -t api ./TestCases/APICase/ --html=Results/report.html          # API测试
airobots -t web ./TestCases/WebCase/ --html=Results/report.html          # Web测试
airobots -t android ./TestCases/AndroidCase/ --html=Results/report.html  # Android测试
airobots -t ios ./TestCases/IOSCase/ --html=Results/report.html          # IOS测试
```

## 查看Allure报告

```
allure serve ./Results
```

## 安装Allure

### Linux
```
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update 
sudo apt-get install allure
```

### Mac OS X

对于Mas OS，可通过[Homebrew](https://brew.sh/)进行自动安装

```
brew install allure
```

### Windows

对于Windows，可从[Scoop](https://scoop.sh/)命令行安装程序获得Allure。

要安装Allure，请下载并安装Scoop，然后在Powershell中执行

```
scoop install allure
```
