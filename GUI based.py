
## This program will show the athletes first name in the first scrollbox and when users click on the name the results will be display in the list2 box and when user search by sports, it will show the athletes name in the search result box and when the sports are not in the list it will show that no results found
## Input: The list of athletes is from Athletes-1.txt, Output: a- Display the athletes’ first names into a list, Once the user clicks any athlete from that list, all the athlete’s details must appear into theentry items, Show the first names of the athletes resulted from the search of the following sports(Tabletennis, Volleyball, Cycling, Gymnastics) in the second list, Show the search result of a sport that doesn’t exist in the list.

from tkinter import *

athletesList = [['Bart', 'Walsh', 'Male', 23, 75, 178, 'Blue', 'Tennis', 'B'],
                    ['Beth', 'Wolf', 'Female', 25, 55, 162, 'Black', 'Tabletennis', 'A'],
                    ['Blaine', 'Mann', 'Male', 18, 70, 172, 'Gray', 'Volleyball', 'A'],
                    ['Chris', 'House', 'Female', 17, 60, 170, 'Brown', 'Netball', 'C'],
                    ['Dawn', 'Holt', 'Female', 26, 62, 177, 'Green', 'Volleyball', 'B'],
                    ['Earle', 'Hobbs', 'Male', 27, 80, 185, 'Blue', 'Basketball', 'B'],
                    ['Fay', 'Nash', 'Female', 19, 56, 158, 'Amber', 'Cycling', 'A'],
                    ['Gayle', 'Pierce', 'Female', 19, 57, 159, 'Hazel', 'Gymnastics', 'A'],
                    ['Glenn', 'Green', 'Male', 21, 71, 166, 'Amber', 'Tabletennis', 'C'],
                    ['Jacques', 'Pace', 'Male', 26, 65, 163, 'Gray', 'Swimming', 'A'],
                    ['Jeanne', 'Riggs', 'Female', 18, 62, 172, 'Blue', 'Netball', 'B'],
                    ['Jim', 'Leach', 'Male', 16, 72, 164, 'Brown', 'Cycling', 'C'],
                    ['Joan', 'Hill', 'Female', 16, 53, 164, 'Black', 'Netball', 'C'],
                    ['Jon', 'Webb', 'Male', 30, 63, 175, 'Green', 'Gymnastics', 'A'],
                    ['Leigh', 'Graves', 'Female', 31, 70, 180, 'Black', 'Volleyball', 'A'],
                    ['Marc', 'Klein', 'Male', 32, 79, 188, 'Blue', 'Volleyball', 'C'],
                    ['Merle', 'Joyce', 'Male', 24, 74, 183, 'Green', 'Basketball', 'B'],
                    ['Pearl', 'Roach', 'Female', 23, 63, 182, 'Gray', 'Tennis', 'C'],
                    ['Reid', 'Short', 'Male', 20, 66, 168, 'Hazel', 'Swimming', 'A'],
                    ['Shawn', 'Kane', 'Female', 20, 61, 174, 'Brown', 'Tabletennis', 'A']]


##this function will show the athletes details on the right labels
def displayAthletesDetails(selected_athlete):
    txtFirstName.set(selected_athlete[0])
    txtLastName.set(selected_athlete[1])
    txtAge.set(selected_athlete[2])
    txtGender.set(selected_athlete[3])
    txtWeight.set(selected_athlete[4])
    txtHeight.set(selected_athlete[5])
    txtEyeColor.set(selected_athlete[6])
    txtSport.set(selected_athlete[7])
    txtClass.set(selected_athlete[8])


##this function will display the search results
def displaySearchResults(sport_name):
    lstMembers1.delete(0, END)
    matching_athletes = [athlete for athlete in athletesList if athlete[7] == sport_name]
    if matching_athletes:
        for item in matching_athletes:
            lstMembers1.insert(END, item[0])
    else:
        lstMembers1.insert(END, "No\n", "results\n", "found\n")


##this function will take the input search from the users
def getSportsName():
    sport_name = entry.get()
    displaySearchResults(sport_name)


##this function will display the first name
def displayFirstNames():
    lstMembers.delete(0, END)
    for item in athletesList:
        lstMembers.insert(END, item[0])

# Create the main window of GUI
window = Tk()
window.title("Athletes App")

# Buttons
textForButton = "Search"
btnDisplay = Button(window, text=textForButton, command=getSportsName)
btnDisplay.grid(row=5, column=5, columnspan=3, pady=5)

# Scrollbars
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=1, column=1, rowspan=20, pady=(0, 5), sticky=NS)

yscroll1 = Scrollbar(window, orient=VERTICAL)
yscroll1.grid(row=2, column=0, rowspan=20, pady=(0, 5), sticky=NS)

entry = Entry(window, width=20)
entry.grid(row=4, column=5, padx=10, pady=5)

# List1
lstAthletesTxt = StringVar()
lstMembers = Listbox(window, width=20, height=10, listvariable=lstAthletesTxt, yscrollcommand=yscroll.set)
lstMembers.grid(row=1, column=0, padx=(5, 0), pady=(0, 5), rowspan=20)

lstSearchResult1Txt = StringVar()
lstMembers1 = Listbox(window, width=20, height=10, listvariable=lstSearchResult1Txt, yscrollcommand=yscroll1.set)
lstMembers1.grid(row=30, column=0, padx=(5, 0), pady=(0, 5), rowspan=20)

# Scrollbox
yscroll["command"] = lstMembers.yview
yscroll1["command"] = lstMembers1.yview

# Labels
Label(window, text="Welcome to the Athletes App, stage (2) !", font=("Arial", 16), bg="brown").grid(row=0, column=5, columnspan=3)
Label(window, text="Athletes List").grid(row=0, column=0)
Label(window, text="Search results List").grid(row=29, column=0)
Label(window, text="First Name ").grid(row=1, column=2, padx=10, pady=5)
Label(window, text="Last Name ").grid(row=1, column=3, padx=10, pady=5)
Label(window, text="Gender ").grid(row=1, column=4, padx=10, pady=5)
Label(window, text="Age ").grid(row=1, column=5, padx=10, pady=5)
Label(window, text="Weight ").grid(row=1, column=6, padx=10, pady=5)
Label(window, text="Height ").grid(row=1, column=7, padx=10, pady=5)
Label(window, text="Eye color ").grid(row=1, column=8, padx=10, pady=5)
Label(window, text="Sport ").grid(row=1, column=9, padx=10, pady=5)
Label(window, text="Class ").grid(row=1, column=10, padx=10, pady=5)
Label(window, text="Enter a sport to search ").grid(row=4, column=4, padx=10, pady=5)

#list2
txtFirstName = StringVar()
entFirstName = Entry(window, width=20, state="readonly", textvariable=txtFirstName)
entFirstName.grid(row=2, column=2)

txtLastName = StringVar()
entLastName = Entry(window, width=20, state="readonly", textvariable=txtLastName)
entLastName.grid(row=2, column=3)

txtGender = StringVar()
entGender = Entry(window, width=20, state="readonly", textvariable=txtGender)
entGender.grid(row=2, column=5)

txtAge = StringVar()
entAge = Entry(window, width=20, state="readonly", textvariable=txtAge)
entAge.grid(row=2, column=4)

txtWeight = StringVar()
entWeight = Entry(window, width=20, state="readonly", textvariable=txtWeight)
entWeight.grid(row=2, column=6)

txtHeight = StringVar()
entHeight = Entry(window, width=20, state="readonly", textvariable=txtHeight)
entHeight.grid(row=2, column=7)

txtEyeColor = StringVar()
entEyeColor = Entry(window, width=20, state="readonly", textvariable=txtEyeColor)
entEyeColor.grid(row=2, column=8)

txtSport = StringVar()
entSport = Entry(window, width=20, state="readonly", textvariable=txtSport)
entSport.grid(row=2, column=9)

txtClass = StringVar()
entClass = Entry(window, width=20, state="readonly", textvariable=txtClass)
entClass.grid(row=2, column=10)

# Populate the first listbox
displayFirstNames()

# Bind data to listbox selection
lstMembers.bind("<<ListboxSelect>>", lambda event: displayAthletesDetails(athletesList[lstMembers.curselection()[0]]))
lstMembers1.bind("<<ListboxSelect>>", lambda event: displayAthletesDetails(athletesList[lstMembers1.curselection()[0]]))

# Run the main event loop
window.mainloop()

