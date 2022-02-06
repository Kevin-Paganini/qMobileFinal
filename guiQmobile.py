from qMobile import qMobile
from tkinter import ttk
from tkinter import *

import threading
import selenium
from tkinter import messagebox


textFieldListGUI = []
textFieldInputs = []
redYellowBlueList = []
global t2




class guiQmobile:
    
    
    def __init__(self):
        
        tkWindow = Tk()
        tkWindow.geometry('300x400')
        tkWindow.title('QMobile Enhancer')
    
        def quitButton():
            tkWindow.destroy()
            repopulate(redYellowBlueList)

            
        
        def runBot():
            

            try:
                #running bot
                global bot
                bot = qMobile(textFieldInputs)
                bot.customerSearch()
                redYellowBlueList = bot.listToFile()

                #clerical work to load to original state
                repopulate(redYellowBlueList)  
                textFieldInputs.clear()
            
                #In case Idiot decides to put in wrong username or password
            except selenium.common.exceptions.NoSuchElementException:
                print('youre an idiot')
                messagebox.showerror("error", "Wrong username or password")
            
        
        def hideFields():
            #Basically hides login fields and pulls up loadingbar and quit button
            endingLabel.grid_forget()
            usernameLabel.grid_forget()
            usernameEntry.grid_forget()
            passwordLabel.grid_forget()
            passwordEntry.grid_forget()
            zipCodeLabel.grid_forget()
            zipCodeEntry.grid_forget()
            fileNameLabel.grid_forget()
            fileNameEntry.grid_forget()
            buildingStartLabel.grid_forget()
            buildingStartEntry.grid_forget()
            buildingEndLabel.grid_forget()
            buildingEndEntry.grid_forget()
            loginButton.grid_forget()

            quitButton.grid(row=9, column=0, padx= 10, pady=10)

            loadingBar.grid(row=10,column=0, padx = 5, pady= 10)
            
            tkWindow.update()

        
        
        def repopulate(redYellowBlueList):
            #repopulates login page
            #Forgets loading screen
            loadingBar.grid_forget()
            quitButton.grid_forget()

            #Repopulates login screen and deletes old inputs
            usernameLabel.grid(row=0, column=0, padx=10, pady=10, sticky=E)
            usernameEntry.grid(row=0, column=1, padx=10, pady=10) 
            passwordLabel.grid(row=1, column=0, padx=10, pady=10, sticky=E)
            passwordEntry.grid(row=1, column=1, padx=10, pady=10) 
            zipCodeLabel.grid(row=2, column=0, padx=10, pady=10, sticky=E)
            zipCodeEntry.grid(row=2, column=1, padx=10, pady=10)  
            zipCodeEntry.delete(0, END)
            fileNameLabel.grid(row=3, column=0, padx=10, pady=10, sticky=E)
            fileNameEntry.grid(row=3, column=1, padx=10, pady=10)  
            fileNameEntry.delete(0, END)
            buildingStartLabel.grid(row=4, column=0, padx=10, pady=10, sticky=E)
            buildingStartEntry.grid(row=4, column=1, padx=10, pady=10) 
            buildingStartEntry.delete(0, END)
            buildingEndLabel.grid(row=5, column=0, padx=10, pady=10, sticky=E)
            buildingEndEntry.grid(row=5, column=1, padx=10, pady=10)
            buildingEndEntry.delete(0, END)
            loginButton.grid(row=6, column=0, padx= 10, pady=10) 

            #Shows ending label at end of search with red, yellow and blue accounts
            endingLabel.config(text= 'Finished Search: \n' + 'Red: ' +str(redYellowBlueList[0]) + '\nYellow: ' + str(redYellowBlueList[1]) + '\nBlue: ' + str(redYellowBlueList[2])) 
            endingLabel.grid(row=8, column=0, pady=10, padx= 10)
            
            #To get string names from each field
            username = StringVar()
            textFieldInputs.append(username)
            password = StringVar()
            textFieldInputs.append(password)
            zipCode = StringVar()
            textFieldInputs.append(zipCode)
            fileName = StringVar()
            textFieldInputs.append(fileName)
            buildingStart = StringVar()
            textFieldInputs.append(buildingStart)
            buildingEnd = StringVar()
            textFieldInputs.append(buildingEnd)
            



        def getFields():
            #Gets text fields and starts another thread to run the bot
            #getting text fields
            for textField in textFieldListGUI:
                textFieldInputs.append(textField.get())
            #starts loading screen
            hideFields()
            loadingBar.start()
            #new thread to not make program freeze
            global t2
            t2 = threading.Thread(target = runBot)
            t2.daemon = True
            t2.start()
            
       
        #blablabla making labels and buttons and stuff
        usernameLabel = ttk.Label(tkWindow, text="User Name:")
        usernameLabel.grid(row=0, column=0, padx=10, pady=10, sticky=E)
        username = StringVar()
        textFieldListGUI.append(username)
        usernameEntry = ttk.Entry(tkWindow, textvariable=username)
        usernameEntry.grid(row=0, column=1, padx=10, pady=10)  

        passwordLabel = ttk.Label(tkWindow,text="Password:")
        passwordLabel.grid(row=1, column=0, padx=10, pady=10, sticky=E)  
        password = StringVar()
        textFieldListGUI.append(password)
        passwordEntry = ttk.Entry(tkWindow, textvariable=password, show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=10)  

        zipCodeLabel = ttk.Label(tkWindow, text="Zip Code:")
        zipCodeLabel.grid(row=2, column=0, padx=10, pady=10, sticky=E)
        zipCode = StringVar()
        textFieldListGUI.append(zipCode)
        zipCodeEntry = ttk.Entry(tkWindow, textvariable=zipCode)
        zipCodeEntry.grid(row=2, column=1, padx=10, pady=10)  

        fileNameLabel = ttk.Label(tkWindow, text="File Name:")
        fileNameLabel.grid(row=3, column=0, padx=10, pady=10, sticky=E)
        fileName = StringVar()
        textFieldListGUI.append(fileName)
        fileNameEntry = ttk.Entry(tkWindow, textvariable=fileName)
        fileNameEntry.grid(row=3, column=1, padx=10, pady=10)  

        buildingStartLabel = ttk.Label(tkWindow, text="Building Start Number:")
        buildingStartLabel.grid(row=4, column=0, padx=10, pady=10, sticky=E)
        buildingStart = StringVar()
        textFieldListGUI.append(buildingStart)
        buildingStartEntry = ttk.Entry(tkWindow, textvariable=buildingStart)
        buildingStartEntry.grid(row=4, column=1, padx=10, pady=10)  

        buildingEndLabel = ttk.Label(tkWindow, text="Building End Number:")
        buildingEndLabel.grid(row=5, column=0, padx=10, pady=10, sticky=E)
        buildingEnd = StringVar()
        textFieldListGUI.append(buildingEnd)
        buildingEndEntry = ttk.Entry(tkWindow, textvariable=buildingEnd)
        buildingEndEntry.grid(row=5, column=1, padx=10, pady=10)
        endingLabel = ttk.Label(tkWindow, text= 'Search takes about 5 seconds for 10 searches.') 
        
       
        
        loadingBar = ttk.Progressbar(tkWindow, orient= HORIZONTAL, length= 290, mode= 'indeterminate')
        loginButton = ttk.Button(tkWindow, text="Start Bot", command=getFields, cursor='target')
        loginButton.grid(row=6, column=0, padx= 10, pady=10)  
        quitButton = ttk.Button(tkWindow, text="Quit", command=quitButton, cursor='target')
        

        tkWindow.mainloop()





    def getAllAttributes(self):
        return textFieldInputs
