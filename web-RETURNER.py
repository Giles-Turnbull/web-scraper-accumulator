import requests
import random

count, found, comp, websites, ex, js, jscode, functions = -1, False, "", [], False, [], [], []
r = requests.get(input("what website would you like to enumerate: "), cookies={ 'sessionid': '123..'})
ret = str(r.content)
print("this may take a second or two depending on the size of the websites source")
#=========================================================================================================================================================================
for letter in ret:
    count += 1
    if letter == "h" and found == False:
        if ret[count + 1] == "t" and ret[count + 2] == "t" and ret[count + 3] == "p": found = True
    if found == True:
        if letter == '"' or letter == " ":                                                                    #linked websites
            websites.append(comp)
            found, comp = False, ""
        else: comp = comp + letter
for site in websites:
    if ".js" in site: js.append(site)
#=========================================================================================================================================================================
#=========================================================================================================================================================================
for site in js:
    try:
        key = ""
        for i in range(15): key = key + chr(random.randint(97, 122))
        jscode.append(key)
        rTwo = requests.get(site, cookies={ 'sessionid': 'abc...'})
        globals()[key] = str(rTwo.content)
        for func in jscode:                                                                                   #js functions
            jscount, jsfound, jscomp = -1, False, ""
            for code in eval(func):
                jscount += 1
                if code == "f" and eval(func)[jscount + 1] == "u" and eval(func)[jscount + 2] == "n" and eval(func)[jscount + 3] == "c" and eval(func)[jscount + 4] == "t" and eval(func)[jscount + 5] == "i" and eval(func)[jscount + 6] == "o" and eval(func)[jscount + 7] == "n":
                    jsfound = True
                if jsfound == True:
                    if code == ")":
                        jsfound, jscomp = False, (jscomp + ")")
                        functions.append(jscomp)
                        jscomp = ""
                    else: jscomp = jscomp + str(code)
    except: print("something went wrong with the js lookup")
#=========================================================================================================================================================================
        # make function to find other jpg and png files
        # then make another to do the same with js files
#=========================================================================================================================================================================

while ex == False:
    option = input("=======================\n1. connected websites\n2. js functions\n3. picture links\n4. classes\n5. view source code\n6. exit\n=======================\n: ")
#----------------------------------------------------------------
    if option == "1":
        for i in websites: print(i, "\n===============================================================================================================")
#----------------------------------------------------------------
    if option == "2":
        for i in js: print(i, "\n===============================================================================================================")
        for i in functions: print(i)
#----------------------------------------------------------------
    if option == "3":
        for i in websites:
            if "jpg" in i: print(i, "\n-----------------------------------------------------------------------------------------------------------------")
            elif "png" in i: print(i, "\n-----------------------------------------------------------------------------------------------------------------")
#----------------------------------------------------------------
    if option == "4": print("coming soon")
    if option == "5": print(ret)
    if option == "6": ex = True
    if option == "clear": print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

