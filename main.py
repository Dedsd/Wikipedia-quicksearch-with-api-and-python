import wikipedia

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
print(color.RED + "---------------If you don't know how to use it yet, type 'help' for help with the commands---------------" + color.END)
t = 'y'
while t == 'y':
    q1 = input("What you want to do?: ")
    help = """
    help = Use this command to see all the commands and their functionality
    setlang = Select the language in which you would like to search in wikipedia(ex: 'fr')
    summary = Use this command for a search of something in wikipedia and get a short summary
    quicks = Use this command for a quick wikipedia search and get a sentence from the search result
    kword = Use this command for a one-word search and it will return names that can be related to this
    fullpage = Go to the full wikipedia page and collect titles, images, links etc(depending on the size of the page it may take longer)    
    """
    if q1 == "help":
        print(color.GREEN + help + color.END)
    elif q1 == "summary":
        q2 = input("What you would like to have a summary about?: ")
        q2answer = wikipedia.summary({q2})
        print(color.BOLD + q2answer + color.END)
    elif q1 == "quicks":
        q3 = input("What you would like to have a quick search about?: ")
        q3answer = wikipedia.summary({q3}, sentences=1)
        print(color.BOLD + q3answer + color.END)
    elif q1 == "kword":
        q4 = input("What would you like to search for according to the keyword?: ")
        q4answer = wikipedia.search({q4}, results=4)
        print(f"{color.BOLD}{''.join(q4answer)}{color.END}")
    elif q1 == "setlang":
        q5 = input("Which language would you like to wikipedia: ")
        q5answer = wikipedia.set_lang(f"{q5}")
    elif q1 == "fullpage":
        q6 = input("Which page would you like to access?: ")
        q6answer = wikipedia.page(f"{q6}")
        print(f"{color.BOLD}Title:{color.END} {q6answer.title}")
        print("-------------------------------------------------------------")
        print(f"{color.BOLD}Url:{color.END} {q6answer.url}")
        print("-------------------------------------------------------------")
        print(f"{color.BOLD}Content(summary):{color.END} {q6answer.summary}")
        print("-------------------------------------------------------------")
        print(f"{color.BOLD}Images:{color.END} {q6answer.images[2]}")
        print("-------------------------------------------------------------")
        print(f"{color.BOLD}Categories:{color.END} {q6answer.categories}")
    else:
        print(color.BOLD + "No commands found, try again or type 'help' for help with the commands" + color.END)
    t = input(color.BOLD + "Would you like to search again? (y/n): " + color.END).lower()

    


