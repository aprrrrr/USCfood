# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib




food = []
n = int(raw_input('Enter how many kinds of food you would like to get notified for: '))
for i in range(0, n):
    x = raw_input('Enter the name of the food: ')
    food.append(x)

mailinglist=['aprilc@usc.edu',"konghayo@usc.edu"]
email=raw_input('Enter your email:')
mailinglist.append(email)

#ideally, this is supposed to be an infinite loop so that the program updates everyday and notifies users
run=True
while run:
    # set the url as USC dining menu,
    url = "https://hospitality.usc.edu/residential-dining-menus/"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")

    hasGoodfood=False
    txt="The dining hall has: "
    
    for x in food:
        if str(soup).find(x) != -1:
            print(x)
            hasGoodfood=True
            txt+= x
            txt+=", "

    txt=txt[:-1]
    txt=txt[:-1]
    
    txt+=" today."
    print(txt)


    if not hasGoodfood:
        
        # wait for a day
        # time.sleep(86400)
        break
    else:
        # create an email message with just a subject line,
        msg = txt
        # set the 'from' address,
        fromaddr = 'uscdininghall@gmail.com'
        # set the 'to' addresses,
        toaddrs  = mailinglist
        
        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        #add my account login name and password,
        server.login("uscdininghall@gmail.com", "USCR0cks!")
        
        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)
        
        # send the email
        server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        server.quit()
        run=False
        # wait for a day
        # time.sleep(86400)
        break