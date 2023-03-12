import webbrowser

WhatToSee =  input("What would you like to see")
WhatToSee =WhatToSee.strip()

WhatToSee=WhatToSee.replace(" ","+")

webbrowser.open(f"https://www.google.com/search?q={WhatToSee}")