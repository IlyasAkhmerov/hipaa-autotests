 <h1 align="center"><img  src="./readme_assets/logo.png" width="5%"> TruVISIBILITY SecureMail AutoTests</h1>

## Description
TruVisibility SecureMail - this is a secure email service that allows you to exchange secure emails in compliance with regulatory requrements such as HIPAA and CFPB

The email client is available at [Staging ](https://.../) and [Production](https://securemail.truvisibility.com/).

The presented tests allow you to check the basic functionality of the email service with the ability to output test results 
in test runs of the [QASE](https://app.qase.io/) test management system or generate a test report using the [Allure](https://github.com/allure-framework) framework

The tests are written in the [Python](https://www.python.org/) programming language, and [Selenium](https://www.selenium.dev/) Webdriver is used to automate the actions of the web browser

## Python Installation

- [Download](https://www.python.org/downloads) Python 
- Start the installation process
- Activate the **Add Python to PATH** check mark
- Install

## IDE Installation

For convenience in writing code and running tests, it is recommended to [install PyCharm](https://www.jetbrains.com/ru-ru/pycharm/) as an IDE.

## Selenium Webdriver

[Download Selenium Webdriver](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) and unpack it

**Pay attention! The driver version must match the version of your browser!**

## Selenium Installation

Open the terminal and run the command:

```
pip3 install selenium
```

## Installing and configuring the Allure plugin

### 1. Java 8

- Make sure you have Java 8 installed. If not, [Download Java 8](https://java.com/en/download/) and install it
- Go to the environment variables and write the path to the JAVA_HOME user variable:
<p align="center">
<img  src="./readme_assets/java_home variable.png" width="100%">

### 2. [Scoop](https://scoop.sh/#/) Installation
Open [Powershell](https://docs.microsoft.com/en-us/powershell/) and run the commands one by one:

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
```
Invoke-WebRequest get.scoop.sh | Invoke-Expression
```

### 3. Allure Installation

In Powershell, run the command:

```
scoop install allure
```

## Pytest and Allure modules installation
Open the terminal and run the command:
```
pip install pytest
```
```
pip install allure-pytest
```
```
pip install allure-python-commons
```
## Qase TMS Pytest Plugin Installation
In the terminal, run the command:
```
pip install qase-pytest
```

## Test Configuration
The [**configs**](configs) folder contains a configuration file with information about the location path of the Selenium Webdriver and user data required for tests.

***Be sure to create a new configuration file*** and specify your configuration data in it: the path to the Selenium Webdriver located on your computer (driverPath), emails, passwords, etc.

After that, specify the name of this configuration file and the name of the project folder in the [ConfigManager.py](tests/e2e/ConfigManager.py)
<p align="center">
<img  src="./readme_assets/config path.png" width="100%">

## How to run tests

Running tests with Allure report generation only:
```
pytest --alluredir results
```

Output of test results:
```
allure serve results
```
Running tests with output test results in test runs of the QASE TMS and Allure report:
```
pytest --qase --qase-api-token=[QASE-token from your project] --qase-project=[YOUR_PROJECT_CODE] --qase-new-run --alluredir results
```

For more information about command line arguments, see [here](https://github.com/qase-tms/qase-pytest)
