import tkinter as tk
from tkinter import ttk
from tkinter import *
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

a =0
url =''
try:
    def data():
        print('in')
        url = driver.current_url
        for i in range(1,20):
            time.sleep(3)
            div = driver.find_element_by_xpath('//*[@id="container"]/main/div/section/div/div/div[4]/div[2]/div[1]/div[2]/ul/li['+str(i)+']/a/div').click()
            time.sleep(5)                      
            price = driver.find_element_by_xpath('//*[@id="container"]/main/div/div/div[5]/div[1]/div/section/span[1]')
            print(price.text)
            desc = driver.find_element_by_xpath('//*[@id="container"]/main/div/div/div[4]/section/div/div/div[2]')
            print(desc.text)
            specifictaions = driver.find_element_by_xpath('//*[@id="container"]/main/div/div/div[4]/section/div/div/div[1]')
            print('Specifications:',specifictaions.text)

            # For clicking show number button
            driver.find_element_by_xpath('//*[@id="container"]/main/div/div/div[5]/div[2]/div/div/div[3]/div[2]').click()
            time.sleep(1)
            number = driver.find_element_by_xpath('//*[@id="container"]/main/div/div/div[5]/div[2]/div/div/div[3]/div').text
            print(number)
            driver.get(url)
           
        return
except NoSuchElementException as n:
    print(n.stacktrace())
    pass
def gui():
    global win
    win = Tk()
    win.geometry("530x400+400+100")
    win.title("Menu")
    win.config(bg = "cadet blue")
    win.resizable(0, 0) 
    Emaillabel = Label(win,font = ('arial',15,'bold'), text = "Email",width = 10,relief = GROOVE)
    Emaillabel.grid(column=0,row=0,padx=100,pady=10)

    Emailtxt = Entry(win,width=20,font = ('arial',15,'bold'))
    Emailtxt.place(x=260,y=10)
    Passwordlabel = Label(win,font = ('arial',15,'bold'), text = "Password",width = 10,relief = GROOVE)
    Passwordlabel.grid(column=0,row=1,padx=10,pady=20)
    Passwordtxt = Entry(win,width=20,font = ('arial',15,'bold'))
    Passwordtxt.place(x=260,y=70)

    Catlabel = Label(win,font = ('arial',15,'bold'), text = "Category",width = 10,relief = GROOVE)
    Catlabel.grid(column=0,row=2,padx=10,pady=20)
    global comboExample
    comboExample = ttk.Combobox(win, values=list(cat.keys()),font = ('arial',10,'bold'),width = 29)
    #pprint(dict(comboExample)) 
    
    comboExample.place(x=260,y=140)
    #comboExample.current(a)
    comboExample.bind("<<ComboboxSelected>>",c)
    comboExample.current(a)
    #Cattxt = Entry(win,width=20,font = ('arial',15,'bold'))
    #Cattxt.place(x=260,y=140)

    Citylabel = Label(win,font = ('arial',15,'bold'), text = "Province",width = 10,relief = GROOVE)
    Citylabel.grid(column=0,row=3,padx=10,pady=20)
    global comboExample1
    comboExample1 = ttk.Combobox(win, values=list(c2().keys()),font = ('arial',10,'bold'),width = 29) 
    comboExample1.place(x=260,y=210)
    #comboExample1.current(a)


    b = Button(win,text = "Submit",font = ('arial',15,'bold'),command = scrap,height = 1,width = 8,bd = 4)
    b.place(x=180,y=280)
    b1 = Button(win,text = "Exit",command = exit,font = ('arial',15,'bold'),height = 1,width = 8,bd = 4)
    b1.place(x=300,y=280)

    win.mainloop()
    return
def scrap():
    try: 
        j =  c2().get(comboExample1.get())
        login('pratama.jhontata@gmail.com','bangtata1989')
        k =cat.get(comboExample.get())
        time.sleep(3)
        # Clicking properies' category
        driver.find_element_by_xpath(divs.get(k)).click()
        time.sleep(3)
        comboExample1.current(j)
        driver.find_element_by_xpath('//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[2]').click()
        driver.find_element_by_xpath(citydivs1.get(j)).click()
        time.sleep(3)
        data()
        print('out')
        return
        #driver.find_element_by_xpath('//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[2]/div[3]/ul/li[2]/ul/li[3]/a/span[2]').click()
    except NoSuchElementException as n:
        print(n.stacktrace())
        pass

cat = {"For Sale : Houses & Apartments" : 1,"For Rent : Houses & Apartments" : 2,"Land" : 3,"Homestays" : 4,"For Sale :Commercial Buildings" : 5,"For Rent :Commercial Buildings" : 6}
cities1 = {"West Java":1,"East Java" :2,"Yogyakarta DI":3,"Jakarta Capital City":4, "Banten":5,"Central Java":6,"Lampung":7,"Bali":8,"North Samatra":9,"South Sulawasi":10,"Riau":11,"South Sumatra":12,"East Kalimantan":13,"Riau Islands":14,"South Kalimantan":15,"West Kalimantan":16,"Aceh Di":17,"West Sumatra":18,"North Sulawesi":19,"West Nusa Tengarra":20}
cities2 = {"Jakarta Capital City":1,"East Java" :2,"West Java":3,"Banten":4, "Yogyakarta DI":5,"Central Java":6,"Bali":7,"North Samatra":8,"East Kalimantan":9,"South Sumatra":10,"South Sulawasi":11,"South Kalimantan":12,"Lampung":13,"Riau Islands":14,"Riau":15,"West Sumatra":16,"Aceh Di":17,"North Sulawesi":18,"West Kalimantan":19,"West Nusa Tengarra":20}
cities3 = {"Yogyakarta DI":1,"East Java" :2,"West Java":3,"Central Java":4, "Bali":5,"Banten":6,"Jakarta Capital DKI":7,"Lampung":8,"North Samatra":9,"East Kalimantan":10,"South Sumatra":11,"Riau":12,"South Sulawasi":13,"South Kalimantan":14,"Aceh Di":15,"West Kalimantan":16,"West Nusa Tengarra":17,"North Sulawesi":18,"West Sumatra":19,"Jambi":20}
cities4 = {"Jakarta DKI":1,"East Java" :2,"West Java":3,"Yogyakarta DI":4, "Central Java":5,"Bali":6,"Banten":7,"North Samatra":8,"South Samatra":9,"Lampung":10,"South Kalimantan":11,"South Sulawasi":12,"East Kalimantan":13,"Riau":14,"West Sumatra":15,"Aceh Di":16,"Riau Islands":17,"Jambi":18,"West Nusa Tengarra":19,"West Kalimantan":20}
cities5 = {"East Java":1,"West Java" :2,"Jakarta DKI":3,"Banten":4, "Central Java":5,"Yogyakarta DI":6,"North Samatra":7,"Bali":8,"Lampung":9,"Riau Islands":10,"South Sulawasi":11,"Riau":12,"South Sumatra":13,"East Kalimantan":14,"West Kalimantan":15,"South Kalimantan":16,"North Sulawasi":17,"Aceh Di":18,"West Sumatra":19,"West Nusa Tengarra":20}
cities6 = {"Jakarta DKI":1,"East Java" :2,"West Java":3,"Central Java":4, "Banten":5,"Yogyakarta DI":6,"Bali":7,"North Samatra":8,"East Kalimantan":9,"South Sulawasi":10,"South Sumatra":11,"South Kalimantan":12,"Lampung":13,"Riau Islands":14,"Riau":15,"West Kalimantan":16,"North Sulawasi":17,"Aceh Di":18,"West Sumatra":19,"West Nusa Tengarra":20}



# Below is list of cities , for different categories.
divs = {1 : '//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[2]/div[3]/ul/li[2]/ul/li[1]/a',
    2 : '//*[@id=\"container"]/main/div/section/div/div/div[5]/div[1]/div/div[2]/div[3]/ul/li[2]/ul/li[2]/a',
    3 : '//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[2]/div[3]/ul/li[2]/ul/li[3]/a/span[1]',
    4 : '//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[2]/div[3]/ul/li[2]/ul/li[4]/a',
    5 : '//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[2]/div[3]/ul/li[2]/ul/li[5]/a',
    6 : '//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[2]/div[3]/ul/li[2]/ul/li[6]/a'}

citydivs1 = {1:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/li[1]/a',
    2:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/li[2]/a',
    3:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/li[3]/a',
    4:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/li[4]/a',
    5:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/li[5]/a',
    6:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[1]/li[1]/a',
    7:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[1]/li[2]/a',
    8:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[1]/li[3]/a',
    9:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[1]/li[4]/a',
    10:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[1]/li[5]/a',
    11:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[1]/li[6]/a',
    12:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[1]/li[7]/a',
    13:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[1]/li[8]/a',
    14:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[1]/li[9]/a',
    15:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[1]/li[10]/a',
    16:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[1]/li[11]/a',
    17:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[1]/li[12]/a',
    18:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[1]/li[13]/a',
    19:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[1]/li[14]/a',
    20:'//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[3]/div[3]/ul/li/ul/div[1]/li[15]/a'}



try :
    win=''
    
    comboExample=ttk.Combobox(win, values=list(cat.keys()),font = ('arial',10,'bold'),width = 29)
    
    def c(eventobject):
        global comboExample1
        global a
        if(comboExample.get()=='For Sale : Houses & Apartments'):
            comboExample1 = ttk.Combobox(win, values=list(cities1.keys()),font = ('arial',10,'bold'),width = 29)
            comboExample1.place(x=260,y=210)
            a = 0
          
        elif(comboExample.get()=='For Rent : Houses & Apartments'):
            comboExample1 = ttk.Combobox(win, values=list(cities2.keys()),font = ('arial',10,'bold'),width = 29)
            comboExample1.place(x=260,y=210)
            a =1

        elif(comboExample.get()=='Land'):
            comboExample1 = ttk.Combobox(win, values=list(cities3.keys()),font = ('arial',10,'bold'),width = 29)
            comboExample1.place(x=260,y=210)
            a = 2
           
        elif(comboExample.get()=='Homestays'):
            comboExample1 = ttk.Combobox(win, values=list(cities4.keys()),font = ('arial',10,'bold'),width = 29)
            comboExample1.place(x=260,y=210)
            a = 4
         
        elif(comboExample.get()=='For Sale :Commercial Buildings'):
            comboExample1 = ttk.Combobox(win, values=list(cities5.keys()),font = ('arial',10,'bold'),width = 29)
            comboExample1.place(x=260,y=210)
            a =5
           
        elif(comboExample.get()=='For Rent :Commercial Buildings'):
            comboExample1 = ttk.Combobox(win, values=list(cities6.keys()),font = ('arial',10,'bold'),width = 29)
            comboExample1.place(x=260,y=210)
            a = 6
      
        else:
            print('no category')
    comboExample.bind("<<ComboboxSelected>>",c)
    comboExample.current(a)
    def c2():
        global comboExample1
        if(comboExample.get()=='For Sale : Houses & Apartments'):
            return cities1
        elif(comboExample.get()=='For Rent : Houses & Apartments'):
            return cities2
        elif(comboExample.get()=='Land'):
            return cities3
        elif(comboExample.get()=='Homestays'):
            return cities4
        elif(comboExample.get()=='For Sale :Commercial Buildings'):
            return cities5
        elif(comboExample.get()=='For Rent :Commercial Buildings'):
            return cities6  
        else:
            print('no city')

    comboExample1=ttk.Combobox(win, values=list(c2().keys()),font = ('arial',10,'bold'),width = 29) 
            

    def login(username,passw):
            # For clicking login button.
            driver.find_element_by_xpath('//*[@id="container"]/main/div/section/div/div/div[5]/div[1]/div/div[2]/div[3]/ul/li[2]/ul/li[3]/a/span[2]').click()
            driver.find_element_by_xpath('//*[@id="container"]/header/div/div/div[3]/button[1]').click()
            # For clicking login by email button.
            time.sleep(5)
            element = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/button[2]")
            driver.execute_script("arguments[0].click()", element)
            # For writing username in user textfield
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/div[2]/div/div[1]/div/div/input').send_keys(username)
            # For Clicking Next button.
            time.sleep(2)
            element = driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/button')
            driver.execute_script("arguments[0].click();", element)
            # For writing password in password field
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="password"]').send_keys(passw)
            # For Clicking Submit button.
            time.sleep(2)
            element =driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div/button')   
            driver.execute_script("arguments[0].click();", element)
            return
except NoSuchElementException as n:
    print('login failed')
    print(n.stacktrace)
    pass  
            

    

chrome_path='G:\\Python work\\chromedriver_win32\\chromedriver.exe' 
driver=webdriver.Chrome(chrome_path)
driver.get("https://www.olx.co.id/properti/rumah/")
time.sleep(3)
gui()

    
