import os, random

def addData(bigList):
    """
    This function allows the user to type in 14 elements of an Olympic Athlete and it will add it to the Olympic Cleaned Datset.csv

    Parameters:
    -----------
    bigList: List
        A nested list where it is formatted [[Athlete 1 Data], [Athlete 2 Data], ...]]
    
    Returns:
    --------
    None
        Used to break out of the function due to multiple loops
    """

    os.system("cls")

    with open("Olympic Cleaned Dataset.csv", 'a', encoding = "utf-8") as outFile: #Opens the data to append information
        print("Enter the stats on your athlete:")
        
        names = [] #Will have all names in the Olympic Cleaned Dataset.csv file (a big list)
        done = False #Boolean for if it has already asked the user if they'd like to continue so it doesn't do that forever
        
        while True:
            try:
                if not done:
                    name = input("What is their name? ")
        
                    for i in bigList:
                        names.append(i[0]) #Append all names to the names list
        
                    if name in names and not done:
                        done = True
                        raise FutureWarning
                    
                gender = input("What is their gender? ")
                age = str(int(input("What is their current age? ")))
                height = str(int(input("What is their height in cm: ")))
                weight = str(int(input("What is their weight in kg? ")))
                country = input("What country did they represent? ")
                game = input("Which season did they do the olympics? (Ex: 1992 Summer) ")
                year = str(int(input("What year did they play? ")))
                season = input("What season did they play? ")
                city = input("What city was the olympics in? ")
                sport = input("What sport did they play ")
                event = input("What specific event? ")
                medal = input("Did they win a medal? (No Medal if no medal)")
                edition = input("What edition? (Ex: 1992 Barcelona): ")
                break
            
            except ValueError:
                print("Please enter stats again")

            except FutureWarning:
                print("This athlete already exists in our database. Here are their stats:")
                allAthleteInfo(bigList, name) #Prints all the data given of this athlete
                
                print("\nWould you like to continue adding the data?")
                answer = "x"
                
                while answer not in ['y', 'n']:
                    answer = input("y/n: ")
                
                if answer == 'n':
                    os.system('cls')
                    return #If they don't want to add something that's already there, they escape. Break doesn't work because there is another loop
                
                else:
                    continue #If they do want to continue adding, go back to the top of the loop.

                
        newathleteinfo = [name, gender, age, height, weight, country, game, year, season, city, sport, event, medal, edition] #The list that will get appended
        outFile.write(",".join(newathleteinfo)+"\n") #Join the list into a string seperated it by a comma with no space because that's how it is in the CSV file. Then add a \n
        
        print("Information saved") #Print this so the user knows it got to the stage where it is saved
        print("Information won't be callable till after this program is closed and re opended\n") #We're not going to keep opening the giant Olympic Cleaned Dataset after running this function because that will be way too much memory for the computer


def allAthleteInfo(bigList, athlete_chosen = None):
    """
    allAthleteInfo function will ask you for an athlete and it will give the user all the information it has on the athlete
    
    Parameters:
    -----------
    bigList: list
        A nested list with format [[athlete 1], [athlete 2], ...]]
    athlete_chosen: str
        The chosen athlete, if there is one, to look up. Set to None if not given
    
    Returns:
    --------
    None
    """
    
    if athlete_chosen == None: #If it is chosen, that means this is coming from a function other than main so the user may want to see the information above, so don't clear it if it is an actual name
        os.system("cls")

    while True:
        if athlete_chosen == None:
            athlete = input("Name an athlete: ")
        else:
            athlete = athlete_chosen

        counter = 1 #Used for printing
        found = False #Used to see if the athlete was found or not

        for fullinfo in bigList: #For every list in the nested list
            if athlete == fullinfo[0]: #fullinfo[0] is the name
                found = True #Athlete is found, lets set this to True
                print(f"Olympics Game Number {counter}")
                print(f"\tName: {fullinfo[0]}")
                print(f"\tGender: {fullinfo[1]}")
                print(f"\tAge: {fullinfo[2]}")
                print(f"\tHeight (cm): {fullinfo[3]}")
                print(f"\tWeight (kg): {fullinfo[4]}")
                print(f"\tCountry of origin: {fullinfo[5]}")
                print(f"\tGame: {fullinfo[6]}")
                print(f"\tYear: {fullinfo[7]}")
                print(f"\tSeason: {fullinfo[8]}")
                print(f"\tCity of Olympic: {fullinfo[9]}")
                print(f"\tSport: {fullinfo[10]}")
                print(f"\tEvent: {fullinfo[11]}")
                print(f"\tMedal: {fullinfo[12]}")
                print(f"\tEdition: {fullinfo[13]}")
                print("-------------------------------")
                counter +=1

        if not found:
            print("Athlete not found")
            print("If athlete was entered in this session. Please close file and re-open\n") #As said in addData() function, we're not going to reopen Olympic Cleaned Data multiple times due to it's size
            continue
        print()
        break


def seasonInfo(bigList):
    """
    seasonInfo function will ask the user for the year and season and provide the total amount of trophies, including Gold, Silver, and Bronze. Additionally it adds the average height and age
    """
    
    os.system("cls")
    while True:
        year = input("What year? ")
        season = input("What season? ").capitalize()
        season = year + " " + season

        indexseason = []
        
        GoldMedals = 0
        SilverMedals = 0
        BronzeMedals = 0
        
        totalheight = 0 #All athletes of that seasons height added together. Used to calculate mean
        totalage = 0 #All athletes of that seasons age added together. Used to calculate mean
        
        counter = 0
        found = False

        for fullinfo in bigList: #For every list in the nested list
            if fullinfo[6] == season: #fullinfo[6] is the season, such as 1948 Summer
                indexseason.append(counter)
                found = True
            
            counter += 1
        
        for i in indexseason:
            if bigList[i][12] == "Gold":
                GoldMedals += 1
            elif bigList[i][12] == "Silver":
                SilverMedals += 1
            elif bigList[i][12] == "Bronze":
                BronzeMedals += 1
            
            try:
                totalheight += int(float(bigList[i][3])) #Convert to float in case it's a decimal. Then convert to int so there is no decimals
                totalage += int(float(bigList[i][2])) #Convert to float in case it's a decimal. Then convert to int so there is no decimals
            except ValueError:
                continue #There is a chance that there is a comma error even though 99.9999% of cases have been handled. So if there is an error, just skip it.
        
        if not found:
            print("Season not found")
            continue
        
        #Find means
        meanheight = totalheight//len(indexseason)
        meanage = totalage//len(indexseason)

        print(f"""City: {bigList[indexseason[0]][9]}
Gold Medals: {GoldMedals}
Silver Medals: {SilverMedals}
Bronze Medals: {BronzeMedals}
Average Height: {meanheight} cm
Average Age: {meanage} years old\n""")
        break

    
def countryInfo(bigList):
    """
    Select a country and see all athletes from that country and the amount of medals won of that country ever

    Parameters:
    -----------
    bigList: list
        A nested list formatted [[athlete 1 data], [athlete 2 data], ...]
    
    Reeturns:
    ---------
    None
    """
    
    os.system('cls')
    countries = [] #All countries that have participated in the Olympics from 1896 to 2016
    
    for i in bigList:
        countries.append(i[5]) #i[5] is the country the athlete plays for
    countries = list(set(countries)) #Remove duplicates by turning to a set, then turn it back to a list
    
    while True:
        country = input("Select a country to view stats on: ")
        
        if country not in countries: #Meaning the given country has never been to the Olympics
            print("Chosen country has not been in the olympics")
            continue
        
        break

    athletes = [] #All athletes of that country

    #The {variable name} medals that country has won
    totalGold = 0
    totalSilver = 0
    totalBronze = 0

    for i in bigList:
        if i[5] == country:
            athletes.append(i[0]) #Append the name
            if i[12] == 'Gold': #i[12] is the medal type. If No Medal... well it doesn't even matter
                totalGold += 1
            elif i[12] == 'Silver':
                totalSilver += 1
            elif i[12] == 'Bronze':
                totalBronze += 1
    
    print("\nAthletes: ")
        
    athletes = list(set(athletes))
    counter = 1
    
    for athlete in athletes:
        print(f"{counter}. {athlete}") #Print all athletes with it's number
        counter += 1
    
    print(f"All Athletes in the Olympics from {country} ⬆️")
    print(f"\nGold Medals: {totalGold}")
    print(f"Silver Medals {totalSilver}")
    print(f"Bronze Medals: {totalBronze}\n")


def olympicRecords(bigList):
    """
    olympicRecords is a function that will find 6 olympic records of all time including oldest, youngest, tallest, shortest, heaviest, and lightest athletes along with their country and sport
    
    Parameters:
    -----------
    bigList: list
        A nested list formatted [[athlete 1 data], [athlete 2 data], ...]
    
    Returns:
    --------
    None
    """
    
    os.system("cls")
    
    oldest_age = -1 #Age automatically is older than this
    oldest_athlete = ""
    oldest_sport = ""
    oldest_country = ""
    
    youngest_age = 1000 #Age automatically younger than this
    youngest_athlete = ""
    youngest_sport = ""
    youngest_country = ""
    
    tallest_height = -1
    tallest_athlete = ""
    tallest_sport = ""
    tallest_country = ""
    
    shortest_height = 1000
    shortest_athlete = ""
    shortest_sport = ""
    shortest_country = ""
    
    heaviest_weight = -1
    heaviest_athlete = ""
    heaviest_sport = ""
    heaviest_country = ""
    
    lightest_weight = 1000
    lightest_athlete = ""
    lightest_sport = ""
    lightest_country = ""

    for i in bigList:
        try:
            #Convert to float to consider decimals, convert to int to remove them
            age = int(float(i[2]))
            height = int(float(i[3]))
            weight = int(float(i[4]))

            #Update values. No max() and min() because those functions loop through the bigList while it's already looping through the bigList, so it practically crashes your computer due to too much memory
            if age > oldest_age:
                oldest_age = age
                oldest_athlete = i[0]
                oldest_sport = i[10]
                oldest_country = i[5]
    
            if age < youngest_age:
                youngest_age = age
                youngest_athlete = i[0]
                youngest_sport = i[10]
                youngest_country = i[5]
    
            if height > tallest_height:
                tallest_height = height
                tallest_athlete = i[0]
                tallest_sport = i[10]
                tallest_country = i[5]
    
            if height < shortest_height:
                shortest_height = height
                shortest_athlete = i[0]
                shortest_sport = i[10]
                shortest_country = i[5]
    
            if weight > heaviest_weight:
                heaviest_weight = weight
                heaviest_athlete = i[0]
                heaviest_sport = i[10]
                heaviest_country = i[5]
    
            if weight < lightest_weight:
                lightest_weight = weight
                lightest_athlete = i[0]
                lightest_sport = i[10]
                lightest_country = i[5]

        except ValueError:
            continue

    print(f"Oldest Athlete: {oldest_athlete}; {oldest_age} years old. Sport: {oldest_sport}; Country: {oldest_country}")
    print(f"\nYoungest Athlete: {youngest_athlete}; {youngest_age} years old. Sport: {youngest_sport}; Country: {youngest_country}")
    print(f"\nTallest Athlete: {tallest_athlete}; {tallest_height} cm tall. Sport: {tallest_sport}; Country: {tallest_country}")
    print(f"\nShortest Athlete: {shortest_athlete}; {shortest_height} cm tall. Sport: {shortest_sport}; Country: {shortest_country}")
    print(f"\nHeaviest Athlete: {heaviest_athlete}; {heaviest_weight} kg. Sport: {heaviest_sport}; Country: {heaviest_country}")
    print(f"\nLightest Athlete: {lightest_athlete}; {lightest_weight} kg. Sport: {lightest_sport}; Country: {lightest_country}\n")


def feelingLucky(bigList):
    """
    feelingLucky is a function where the computer picks a random athlete and gives you some statistics. It then gives you the option to view full statistics by calling the allAthleteInfo function
    
    Parameters:
    -----------
    bigList: list
        A nested list with a format of [[athlete 1], [athlete 2], ...]
    
    Returns:
    --------
    None
    """
    
    os.system("cls")

    length = len(bigList) #Just the number of elements in the CSV file
    randomindex = random.randint(0, length-1) #A random index
    name = bigList[randomindex][0] #The name of the lucky person
    pronoun = [] #Will determine based on whether the bigList[index][1] is Male or Female
    indexes = [] #Indexes that the athlete is 

    for i in bigList:
        if i[0] == name:
            indexes.append(bigList.index(i)) #Update indexes list

    #Used for final remarks if they won no medals message
    country = bigList[randomindex][5]
    sport = bigList[randomindex][10]
    
    print(f"The random forgotten athlete is {name} from {bigList[randomindex][5]}!")
    print(f"{name} played in {len(indexes)} olympic game(s) including: \n")

    for i in indexes:
        print(f"{bigList[i][6]}; {bigList[i][10]}; {bigList[i][11]}") #Prints the season, the sport, and then the event
    print()
    
    #Updates Pronoun List
    if bigList[indexes[0]][1] == "Male":
        pronoun = ['he', 'his']
    else:
        pronoun = ['she', 'her']
    
    goldMedals = 0
    silverMedals = 0
    bronzeMedals = 0

    for i in indexes:
        if bigList[i][12] == 'Gold':
            goldMedals += 1
        elif bigList[i][12] == "Silver":
            silverMedals += 1
        elif bigList[i][12] == "Bronze":
            bronzeMedals += 1

    totalMedals = goldMedals+silverMedals+bronzeMedals
    
    #If they won 0 medals, then I don't want to say they won nothing because that makes them sound bad, so I put a cool message instaed
    if totalMedals > 0:
        #I took the name and split it by the space and took the 0th index for first. Then I stripped any quotes because some names have nicknames. Then I capitalized it
        print(f"{name.split(" ")[0].strip('"').capitalize()} won {totalMedals} medal(s) in {pronoun[1]} carreer including {goldMedals} gold medal(s) {silverMedals} silver medal(s) and {bronzeMedals} bronze medal(s). Amazing!")
    
    else:
        print(f"{name.split(" ")[0].strip('"').capitalize()} never won a medal, but {pronoun[0]} was chosen by {pronoun[1]} country, {country}, to represent the whole nation in {sport}.") 
        print(f"{pronoun[0].capitalize()} played {pronoun[1]} favorite sport at the highlest level it gets, the Olympics, all for {sport}, one of the things {pronoun[0]} loved. Amazing!")
        print()
    
    ages = [] #All ages the athlete was during his olympic time
    
    for i in indexes:
        ages.append(bigList[i][2]) #Append all ages of that person at anytime in the olympics into the list
    
    ages = list(set(ages)) #Remove the duplicates
    ages.sort()
    
    #Grammar cases
    if len(ages) == 1:
        print(f"{pronoun[0].capitalize()} played in the olympics when {pronoun[0]} was {ages[0]} years old")
    
    elif len(ages) == 2:
        print(f"{pronoun[0].capitalize()} played in the olympics when {pronoun[0]} was {ages[0]} and {ages[1]} years old")
    
    elif len(ages) >= 3:
        ages.insert(-1, "and")
        ages = ", ".join(ages)
        ages = ages[:-4] + ages[-3:] #Remove the -4th index because it would be 21, 25, 27, and, 29 otherwise. the comma after and is the -4th string because no athlete is under 10 or over 100
    
        print(f"{pronoun[0].capitalize()} played in the olympics when {pronoun[0]} was {ages} years old")
    
    print(f"\nWould you like to see all the data on {name}?")
    
    answer = "x"
    
    while answer not in ['y', 'n']:
        answer = input("(y/n): ").lower()
    
    if answer == 'y':
        print() #For an enter
        allAthleteInfo(bigList, name) #Prints all the data on the chosen athlete
    print()

def quitWithMessage():
    """
    quitWithMessage is a function that will quit the program with the exit() function and give a friendly goodbye before they leave
    
    Paramters:
    ----------
    None
    
    Returns:
    --------
    None
    """
    
    os.system("cls")

    #Friendly Goodbye Message
    print("Thanks for using our program!")
    print("I hope you had fun learning about the forgotten athletes of the Olympics!")
    print("Come back any time!")
    print("\n\n\n") #Otherwise the PS C:\Users\... is too close and it's better to put it down
    exit()


def main():
    """
    The MAIN function, where all the action happens
    
    Parameters:
    -----------
    None
    
    Returns:
    --------
    None
    """
    
    os.system("cls")
    
    #Friendly startup message
    print("Hello! This is a program to discover old athletes of the olympics, since its founding, 1896!\n")
    print("Please turn on Auto-Save feature for best results:")
    print("(VS CODE): File --> Auto Save --> Enabled --> Back to program terminal --> Choose 7 as choice --> Re-Run program\n")

    with open("Olympic Cleaned Dataset.csv", 'r') as inFile:
        readinFile = inFile.readlines()
        readinFile.pop(0) #Delete the titles
        bigList = [] #List of lists where each list is information on the athlete
        
        for i in readinFile:
            line = i.strip("\n").split(",")
            # skip if the data does not have 14 columns
            if len(line) == 14:
                bigList.append(line)
    
    while True:
        print("""Pick an option!:
        Pick 1: Add information of an Olympic Athlete
        Pick 2: Select information on an Olympic athelete
        Pick 3: Stats on an olympic year and season
        Pick 4: Select information on a country
        Pick 5: Olympic Records
        Pick 6: I'm Feeling Lucky!
        Pick 7: Quit
        """)
        
        while True:
            try:
                choice = int(input("Choice: "))
                if choice < 1 or choice > 7:
                    raise ValueError
                break
    
            except ValueError:
                print("Please enter a number from 1 to 7")

        if choice == 1:
            addData(bigList)
            
        elif choice == 2:
            allAthleteInfo(bigList)
            
        elif choice == 3:
            seasonInfo(bigList)
                
        elif choice == 4:
            countryInfo(bigList)
        
        elif choice == 5:
            olympicRecords(bigList)
        
        elif choice == 6:
            feelingLucky(bigList)

        elif choice == 7:
            quitWithMessage()                

#The first and last action, main()
main()