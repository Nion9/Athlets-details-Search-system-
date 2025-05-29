## Author: (Minhajul Islam Nion & u3266650)
## Date created: 11 Aug 2023
## Date last changed: 11 Aug 2023
## This program will show the athletes
## Input: The list of athletes is from Athletes-1.txt, Output: Display all athletes’ details,Show the search result of the following sports (Tabletennis, Volleyball, Cycling,Gymnastics), Show the search result of a sport that doesn’t exist in the list.

##athletes list is from the Athletes-1.txt
athletesList = [["Bart", "Walsh", "Male", 23, 75, 178, "Blue", "Tennis", "B"],
    ["Beth", "Wolf", "Female", 25, 55, 162, "Black", "Tabletennis", "A"],
    ["Blaine", "Mann", "Male", 18, 70, 172, "Gray", "Volleyball", "A"],
    ["Chris", "House", "Female", 17, 60, 170, "Brown", "Netball", "C"],
    ["Dawn", "Holt", "Female", 26, 62, 177, "Green", "Volleyball", "B"],
    ["Earle", "Hobbs", "Male", 27, 80, 185, "Blue", "Basketball", "B"],
    ["Fay", "Nash", "Female", 19, 56, 158, "Amber", "Cycling", "A"],
    ["Gayle", "Pierce", "Female", 19, 57, 159, "Hazel", "Gymnastics", "A"],
    ["Glenn", "Green", "Male", 21, 71, 166, "Amber", "Tabletennis", "C"],
    ["Jacques", "Pace", "Male", 26, 65, 163, "Gray", "Swimming", "A"],
    ["Jeanne", "Riggs", "Female", 18, 62, 172, "Blue", "Netball", "B"],
    ["Jim", "Leach", "Male", 16, 72, 164, "Brown", "Cycling", "C"],
    ["Joan", "Hill", "Female", 16, 53, 164, "Black", "Netball", "C"],
    ["Jon", "Webb", "Male", 30, 63, 175, "Green", "Gymnastics", "A"],
    ["Leigh", "Graves", "Female", 31, 70, 180, "Black", "Volleyball", "A"],
    ["Marc", "Klein", "Male", 32, 79, 188, "Blue", "Volleyball", "C"],
    ["Merle", "Joyce", "Male", 24, 74, 183, "Green", "Basketball", "B"],
    ["Pearl", "Roach", "Female", 23, 63, 182, "Gray", "Tennis", "C"],
    ["Reid", "Short", "Male", 20, 66, 168, "Hazel", "Swimming", "A"],
    ["Shawn", "Kane", "Female", 20, 61, 174, "Brown", "Tabletennis", "A"]]


##this function will controll all the function of this code
def main():
    while True:
        printMenu()
        lstOption1 = input("Enter a number from the above menu: ")

        if lstOption1 in ["1", "2", "3"]:
            if lstOption1 == "1":
                displayAthletesDetails()
            elif lstOption1 == "2":
                searchAthlete()
            else:
                print("Closing program")
                break
        else:
            print("Invalid Choice")
        ##this is another option
        lstOption2 = input("\nPress 1 to go back to the main menu, or press any key to exit program.\n\nEnter a number: ")

        if lstOption2 != "1":
            print("\nGoodbye, hope to see u next time! ")
            break


##this function will give option to choice for users
def printMenu():
    print("Welcome to the Athletes APP!\n")
    print("1. Athletes Information\n2. Athletes Search\n3. Exit\n")


##this function will diplay the athletes details
def displayAthletesDetails():
    print("{0:<20}{1:<15}{2:<15}{3:<10}{4:<10}{5:<10}{6:<15}{7:<15}{8:<15}{9:<10}".format(
        "Athletes Number", "First Name", "Last Name", "Gender", "Age", "Weight", "Height", "Eye Color", "Sport", "Class"))

    for athlete in athletesList:
        print("{0:<20}{1:<15}{2:<15}{3:<10}{4:<10}{5:<10}{6:<15}{7:<15}{8:<15}{9:<10}".format(
            athletesList.index(athlete) + 1, athlete[0], athlete[1], athlete[2], athlete[3], athlete[4],
            athlete[5], athlete[6], athlete[7], athlete[8]))


##this function will controll searchs and the search results
def searchAthlete():
    name = input("\nEnter a sport you want to search: ")
    sportsFound = False
    serialNumber = 1

    foundAthletes = []

    for athlete in athletesList:
        if name.lower() in athlete[7].lower():
            foundAthletes.append(athlete)
            sportsFound = True

    if sportsFound:
        print("{0:<20}{1:<15}{2:<15}{3:<10}{4:<10}{5:<10}{6:<15}{7:<15}{8:<15}{9:<10}".format(
            "Athletes Number", "First Name", "Last Name", "Gender", "Age", "Weight", "Height", "Eye Color", "Sport",
            "Class"))

        for athlete in foundAthletes:
            print("{0:<20}{1:<15}{2:<15}{3:<10}{4:<10}{5:<10}{6:<15}{7:<15}{8:<15}{9:<10}".format(
                serialNumber, athlete[0], athlete[1], athlete[2], athlete[3], athlete[4],
                athlete[5], athlete[6], athlete[7], athlete[8]))
            serialNumber += 1
    else:
        print("No results found, back to the main menu..")

main()
##Refrence1: some code followed from week 9 tuitorial solution
##Refrence2: W3Schools. (2019). Python Tutorial. W3schools.com. https://www.w3schools.com/python/