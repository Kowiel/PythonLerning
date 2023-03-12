import webTest


userinput = input("What would you like to see? : ")

Links = webTest.scrape_google(userinput)
webTest.LookUpThisSides(Links[:4])