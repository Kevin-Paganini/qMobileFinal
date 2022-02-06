from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import csv
from customer import Customer
import re
from webdriver_manager.chrome import ChromeDriverManager

USERNAME_LOGIN = ''
PASSWORD_LOGIN = ''
ZIP_CODE = ''
FILE_NAME = ''
BUILDING_START_NUMBER = -1
BUILDING_END_NUMBER = -1
MASTER_CUSTOMER_LIST = []

class qMobile:
    

    def __init__(self, aList):
        self.aList = aList
        USERNAME_LOGIN = aList[0]
        PASSWORD_LOGIN = aList[1]
        
        
        #In case they want to make the program run windowless
        options = Options()
        #options.add_argument("--headless")
        self.driver = self.driver = webdriver.Chrome(ChromeDriverManager().install())

        #Logging in to Qmobile and getting to search page
        self.driver.get("https://qmobile.quill.com/")

        sleep(5)
        #Click and input username
        username = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/input")
        username.click()
        username.send_keys(USERNAME_LOGIN)
        #click and input password
        password = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/input")
        password.click()
        password.send_keys(PASSWORD_LOGIN)
        sleep(0.1)

        #Clicking login button and navigating to customer search
        loginButton = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/p/a/span").click()
        sleep(1)
        cuztomerSearchButton = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/ul/li[1]/div/div/a/h1").click()
        sleep(1)
   
    def quit(self):
        self.driver.close() 

    def customerSearch(self):
        #Getting info from text input
        BUILDING_END_NUMBER = self.aList[5]
        BUILDING_START_NUMBER = self.aList[4]
        ZIP_CODE = self.aList[2]

        #Figuring out how much to iterate
        total = int(BUILDING_END_NUMBER) - int(BUILDING_START_NUMBER) + 3

        #Iterating through entire building number search range
        for i in range(total):
            count = i + int(BUILDING_START_NUMBER)
            address = (str(count) + ', ' + ZIP_CODE)
            adressInput = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/input")
            adressInput.click()
            print(str(i))
            adressInput.send_keys(address)
            
            searchButton = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/table/tbody/tr/td/a/span").click()

            #Checking is page still loading
            spinner = self.driver.find_element_by_xpath('/html/body/div[14]/span')
            while spinner.is_displayed():
                sleep(0.01)

            clearButton = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/a/span/span[2]").click()
            #Getting the information from the website        
            try:
               
                pageSource = self.driver.page_source
                soup = BeautifulSoup(pageSource, 'html.parser')
                soup.prettify()
                for link in soup.find_all('a'):
                    buyerInfo = []
                    color = link.get('style')
                    if color != None and color != 'text-align: center; vertical-align: middle;':
                            
                        if color == "background-color:#bfdcf3":
                            color = 'blue'
                        elif color == "background-color:#eac4dc":
                            color = 'red'
                        elif color == 'background-color:#ffffe4':
                            color = 'yellow'
                        
                        for attribute in link.find_all("p"):
                            
                            res = re.sub(' +', ' ', attribute.text)
                            buyerInfo.append(res)
                            

                        buyerInfo.append(color)
                        for attribute in link.find_all("img"):
                            attribute.get("src")
                            buyerInfo.append(attribute.get('src')) 
                        buyerInfo.append('') 
                        
                        cust = Customer(buyerInfo)
                        
                        MASTER_CUSTOMER_LIST.append(cust)
 
            except:
                pass

         
        

        self.driver.close()


    def listToFile(self):
        
        NumberOfAccounts = []
        #Keeping track of red, yellow and blue accounts
        BLUE_COUNT = 0
        RED_COUNT = 0
        YELLOW_COUNT = 0
        UNKNOWN_COUNT = 0

        #No copies
        FINAL_LIST = dict()
        for customer in MASTER_CUSTOMER_LIST:
            if customer.getBusiness() not in FINAL_LIST.keys():
                FINAL_LIST[customer.getBusiness()] = customer

        #Counting red, yellow and blue customers
        for customer in FINAL_LIST.values():
            color = customer.getColor()
            if color == 'blue':
                BLUE_COUNT += 1
            elif color == 'red':
                RED_COUNT += 1
            elif color == 'yellow':
                YELLOW_COUNT += 1
            else:
                UNKNOWN_COUNT += 1
    

        #Getting filename
        FILE_NAME = self.aList[3]


        #Writing to file
        with open(FILE_NAME + '.csv', 'w', newline='') as csvfile:
            fieldnames = ["Business name: ", "Address: ","Town: ", "Buyer name: ", "Last Order Date: ", "Last Order Status: ", "Last Invoice Date: ", "Account: ", "Program: ", 'Cancelled QuillPlus: ', 'Contact: ', "Color: "]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for customer in FINAL_LIST.values():
                
                writer.writerow({"Business name: ": customer.getBusiness(), "Address: ": customer.getBusinessAddress(),"Town: ": customer.getBusinessTown(), "Buyer name: ": customer.getBuyerName(), "Last Order Date: ": customer.getLastOrderDate(), "Last Order Status: ": customer.getLastOrderStatus(), "Last Invoice Date: ": customer.getLastInvoiceDate(), "Account: ": customer.getAccount(), "Program: ": customer.getProgram(), 'Cancelled QuillPlus: ': customer.getCancelledQuillPlus(), 'Contact: ': customer.getContact(), "Color: ": customer.getColor()})
            writer.writerow({"Business name: ": ('Red: ' + str(RED_COUNT)), "Address: ": ('Yellow: ' + str(YELLOW_COUNT)), "Town: ": ('Blue: ' + str(BLUE_COUNT)), "Buyer name: ": ('Unknown: ' + str(UNKNOWN_COUNT)), "Last Order Date: ": '', "Last Order Status: ": '', "Last Invoice Date: ": '', "Account: ": '', 'Program: ': '', 'Cancelled QuillPlus: ': '', "Contact: ": '', "Color: ": ''})

        NumberOfAccounts.append(RED_COUNT)
        NumberOfAccounts.append(YELLOW_COUNT)
        NumberOfAccounts.append(BLUE_COUNT)
        MASTER_CUSTOMER_LIST.clear()

        return NumberOfAccounts