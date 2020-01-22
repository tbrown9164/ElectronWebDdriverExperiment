
#the below starts atom and smartservice successfully
from selenium import webdriver
#def   start_atom():
options = webdriver.ChromeOptions()
# options commands below as indicated in https://stackoverflow.com/questions/50642308/webdriverexception-unknown-error-devtoolsactiveport-file-doesnt-exist-while-t/50642913#50642913
# as of 1/21/20 this version launches smartservice but then gives an error DevToolsActivePort file doesn't exist and closes
options.addArguments=   "--no-sandbox"    #doesn't seem to make any difference whether here or not
options.addArguments=   "--disable-dev-shm-usage"
options.addArguments=   "--headless"
options.addArguments=   "--electronPort=9515"
#options.binary_location=  "/users/brownt/downloads/smartservice-3.2.1-full/lib/net45/mtssmartserviceqa.exe"
#options.binary_location = "/users/brownt/AppData/Local/SmartService/MTS SmartService.exe"
options.binary_location = "/program files/atom/atom.exe"    #for experimental use only
driver = webdriver.Chrome(options=options)
driver.get("http://www.google.com")
driver.quit()



#from an earlier google search on the subject   https://stackoverflow.com/questions/38811123/is-possible-to-use-selenium-with-python-for-electron-apps
#requires chromedriver to be run from the commandline first and it runs on 9515 but we get a version indication (that this version of chromeddriver only works on version 79 etc
#remote_app = webdriver.remote.webdriver.WebDriver(
#                 command_executor='http://localhost:9515',
#                 desired_capabilities = {'chromeOptions':{ 'binary': '/users/brownt/AppData/Local/SmartService/MTS SmartService.exe'}},
#                 browser_profile=None,
#                 proxy=None,
#                 keep_alive=False)


