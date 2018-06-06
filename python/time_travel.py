def greeting(y):
    if y < 1900:
        print("You're old!")
    elif y >=1900 and y <=2020:
        print("Howdy!")
    elif y > 2020:
        print("Did Trump fuck up everything?")
year = 1789
greeting(year)

year = 9000
greeting(year)
