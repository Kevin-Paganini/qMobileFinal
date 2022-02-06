import datetime
from bs4 import BeautifulSoup


#Keep track of all information about one customer



class Customer:
    business = ''
    businessAddress = ''
    buyerName = ''
    lastOrderDate = ''
    lastOrderStatus = ''
    lastInvoiceDate = ''
    account = ''
    program = ''
    cancelledQuillPlus = ''
    contact = ''
    color = ''
    
    #constructor
    def __init__(self, customerInfo) -> None:
        #['DEBORAH CERBONE(Q) ', '1 SEAVIEW CT #725 ', ' ', 'BAYONNE , 07002', ' Buyer Name: DEBORAH CERBONE ', ' Last Order Date: 03/02/2016 ', ' Last Order Status: ', ' Last Invoice Date: ', 'Account: 8151283\xa0\xa0', 'Program: ', 'Cancelled QuillPLUS: ', 'Contact: 201-9549409', '7/18/2021 12:43 PM', 'blue']
        self.customerINFO = customerInfo
        self.business = customerInfo[0]
        self.businessAddress = customerInfo[1] 
        self.businessTown = customerInfo[3]
        self.buyerName = customerInfo[4].replace('Buyer Name: ', '')
        self.lastOrderDate = customerInfo[5].replace('Last Order Date: ', '')
        self.lastOrderStatus = customerInfo[6].replace('Last Order Status: ', '')
        self.lastInvoiceDate = customerInfo[7].replace('Last Invoice Date: ', '')
        self.account = customerInfo[8].replace('Account: ', '')
        self.program = customerInfo[14]
        self.cancelledQuillPlus = customerInfo[10].replace('Cancelled QuillPLUS: ', '')
        self.contact = customerInfo[11].replace('Contact: ', '')
        self.color = customerInfo[13]
        

    def spacetaker():
        pass
    


    #Getters

    def getBusinessTown(self):
        return self.businessTown

    def getBusiness(self):
        return self.business
    
    def getBusinessAddress(self):
        return self.businessAddress
    
    def getBuyerName(self):
        return self.buyerName
    
    def getLastOrderDate(self):
        return self.lastOrderDate
    
    def getLastOrderStatus(self):
        return self.lastOrderStatus
        
    def getLastInvoiceDate(self):
        return self.lastInvoiceDate
    
    def getAccount(self):
        return self.account
    
    #Kind of a shitty implementation so be careful with this
    def getProgram(self):
        if self.program != '' and self.program != 'Quill Plus Gold' and self.program != 'Quill Plus Blue' and self.program != 'School Preffered':
            res = self.program
            
            if res == 'icons/qpg.png':
                res = 'Quill Plus Gold'
            elif res == 'icons/qpb.png':
                res = 'Quill Plus Blue'
            elif res == 'icons/sp.png':
                res = 'School Preffered'
            else:
                res = 'unknown'
            self.program = res
        else:
            pass
        return self.program
    
    def getCancelledQuillPlus(self):
        return self.cancelledQuillPlus

    def getContact(self):
        return self.contact
    
    def getColor(self):
        return self.color


    #Setters

    def setBusiness(self, business):
        self.business = business
    
    def setBusinessAddress(self, businessAddress):
        self.businessAddress = businessAddress
    
    def setBuyerName(self, buyerName):
        self.buyerName = buyerName
    
    def setLastOrderDate(self, lastOrderDate):
        self.lastOrderDate = lastOrderDate
    
    def setLastOrderStatus(self, lastOrderStatus):
        self.lastOrderStatus = lastOrderStatus
        
    def setLastInvoiceDate(self, lastInvoiceDate):
        self.lastInvoiceDate = lastInvoiceDate
    
    def setAccount(self, account):
        self.account = account
    
    def setProgram(self, program):
        self.program = program
    
    def setCancelledQuillPlus(self, cancelledQuillPlus):
        self.cancelledQuillPlus = cancelledQuillPlus

    def setContact(self, contact):
        self.contact = contact
    
    def setColor(self, color):
        self.color = color

    
    #I dont think this gets used
    def theBigSplitter(self, customerInfo):
        #DEBORAH CERBONE(Q)  1 SEAVIEW CT #725                   BAYONNE          , 07002  Buyer Name: DEBORAH CERBONE   Last Order Date: 03/02/2016   Last Order Status:    Last Invoice Date:   Account: 8151283   Program:  Cancelled QuillPLUS:  Contact: 201-9549409 blue
        #10:11 PM   GEORGE METZLER & COMPANY(Q)  1 NORTH WAY #2                      BAYONNE          , 07002  Buyer Name: GEORGE METZLER   Last Order Date: 04/24/2017   Last Order Status:    Last Invoice Date:   Account: 8394855   Program:  Cancelled QuillPLUS:  Contact: 201-4377634 blue
        self.customerInfo.split("(Q)")
        self.setBusiness(customerInfo[0])
        rest = customerInfo[1]
        rest.split("Buyer Name:")
        self.setBusinessAddress(rest[0])


    #For debugging purposes
    def toText(self):
        s = "Business name: " + self.getBusiness() + '\n' + "Address: " + self.getBusinessAddress() + '\n' + "Buyer name: " + self.getBuyerName() + '\n' + "Last Order Date: " + '\n' + "Last Order Status: " + self.getLastOrderStatus() + "Last Invoice Date: " + self.getLastInvoiceDate() + "\n" + "Account: " + self.getAccount() + "\n" + "Program: " + self.getProgram() + "\n" + 'Cancelled QuillPlus: ' + self.getCancelledQuillPlus() + '\n' + 'Contact: ' + self.getContact() + '\n' + "Color: " + self.getColor()
        return s
        