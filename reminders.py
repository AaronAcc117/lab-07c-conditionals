
hour = input("Enter the current hour (0-23): ")



    hour = int(hour)
    
    # These are all the  conditions
    if 0 <= hour <= 5:
        reminder = "It's early. You should be sleeping!"
    elif 5 <= hour <= 7:
        reminder = "Wake up, brew that coffee, get that mile run in, and get that breakfast..."
    elif 7 <= hour <= 9:
        reminder = "Time to go to work."
    elif 9 <= hour <= 12:
        reminder = "You should be working!"
    elif 12 <= hour <= 13:
        reminder = "Take your lunch break!"
    elif 13 <= hour <= 17:
        reminder = "Do you feel that afternoon lull?"
    elif 17 <= hour <= 19:
        reminder = "Time to hit the gym..."
    elif 19 <= hour <= 21:
        reminder = "Gotta eat that dinner."
    elif 21 <= hour <= 23:
        reminder = "Get that SLEEP. And rePEAT!"
    else:
        reminder = "You didn't type an acceptable value! (0-23)"

    
    print(reminder)

