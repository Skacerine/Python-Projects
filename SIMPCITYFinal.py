#Author
#Date
#Information about the app

def load_save(): #Loads the game from a txtfile
    count_b =0
    file = open("savefile.txt","r")
    for line in file:
        city_map = eval(line)
    for rows in city_map:
        for boxes in rows:
            if boxes == " ":
                count_b += 1
    count_a = 17 - count_b #Make sure the turn is correct when loading
    file1 = open("remainfile.txt","r")
    for zine in file1:
        countbuilding = eval(zine)
    return [city_map,count_a,countbuilding]

def SIMPCITY(): #displays game map
        max_row = len(city_map)
        max_col = len(city_map[0])
        z = 0
        print("     A     B     C     D  ")
        print("  +-----+-----+-----+-----+")
        for row in range(max_row):
            z += 1
            print(z, end = " ")
            for column in range(max_col):    
                 print("|{:>4s}".format(city_map[row][column]), end = " ")
            print("|")
            print("  +-----+-----+-----+-----+")
countbuilding = {"BCH":8,"FAC":8,"HSE":8,"SHP":8,"HWY":8} #random building generator for option 1 and 2
import random

def BUILDING_GENERATOR():# For random building generator for option 1 and 2
    buildings = []
    for count in countbuilding.keys():
        if countbuilding[count]>0:
            buildings.append(count)
    randombuilding1 = buildings[random.randint(0,len(buildings)-1)]
    randombuilding2 = buildings[random.randint(0,len(buildings)-1)]
    randombuildinglist = [randombuilding1,randombuilding2]
    return randombuildinglist

def BUILDING_DEDUCTOR(): # Deduct buildings from dictionary
    countbuilding[Randombuildinglist[0]] -= 1
    countbuilding[Randombuildinglist[1]] -= 1
    
def DISPLAY_REMAININGS(): #See remaining buildings
    buildingcount = []
    buildingcount.append(countbuilding.get("HSE"))
    buildingcount.append(countbuilding.get("FAC"))
    buildingcount.append(countbuilding.get("SHP"))
    buildingcount.append(countbuilding.get("HWY"))
    buildingcount.append(countbuilding.get("BCH"))
    print("Building"," "*11,"Remaining")
    print("-"*8," "*11,"-"*9)
    print("HSE"," "*11,"{:>6}".format(buildingcount[0]))
    print("FAC"," "*11,"{:>6}".format(buildingcount[1]))
    print("SHP"," "*11,"{:>6}".format(buildingcount[2]))
    print("HWY"," "*11,"{:>6}".format(buildingcount[3]))
    print("BCH"," "*11,"{:>6}".format(buildingcount[4]))
    
def AdjCheck(): #Option 1 and 2 position orthogonally adjacent checker
    up = True 
    down = True 
    left = True
    right= True
    middle = True
    if row != 0:
        up = (city_map[row-1][column] == " ")
    if row != 3:
        down= (city_map[row+1][column] == " ")
    if column != 0:
        left= (city_map[row][column-1] == " ")
    if column != 3:
        right= (city_map[row][column+1] == " ")
    middle = (city_map[row][column] != " ")
    if (up) and (down) and (left) and (right):
        check = False
    elif (middle):
        check = False
    else:
        check = True
    return check

def building_type(building_type): #building scores for checking HSE 's surround
    if building_type == "HSE":
        return 1
    elif building_type == "FAC":
        return -100
    elif building_type == "BCH":
        return 2
    elif building_type == "SHP":
        return 1
    else:
        return 0
    
def shop_check(building,shp_s_build): #Gets back the score for shops
    try:
        if building == "SHP":
            shp_s_build.remove("SHP")
        if building == "FAC":
            shp_s_build.remove("FAC")
        if building == "HSE":
            shp_s_build.remove("HSE")
        if building == "BCH":
            shp_s_build.remove("BCH")
        if building == "HWY":
            shp_s_build.remove("HWY")
    except:
        pass
    return shp_s_build

def MAP_SCAN(): #Scorechecking
    factory_counter = 0
    factory_s = 0
    shop_s = 0 
    house_s = 0
    highway_s = 0
    beach_s = 0
    l_hse_score =[]
    l_fac_score =[]
    l_shp_score =[]
    l_hwy_score =[]
    l_bch_score =[]
    building_masterlist = [l_hse_score,l_fac_score,l_shp_score,l_hwy_score,l_bch_score]
    building_typelist = ["HSE","FAC","SHP","HWY","BCH"]
    for plots in range(len(city_map)):
        for boxes in range(len(city_map[plots])):
            if city_map[plots][boxes] == "HSE":
                s_house = HSE_score(plots,boxes)
                house_s += s_house
                l_hse_score.append(s_house) #print(house_s) #print(building_s) statements are for checking*
            if city_map[plots][boxes] == "FAC":
                s_factory = FAC_score(plots,boxes,factory_s,factory_counter)
                factory_counter += 1
                factory_s += s_factory #print(factory_s)
            if city_map[plots][boxes] == "SHP":
                s_shop = SHP_score(plots,boxes)
                shop_s += s_shop
                l_shp_score.append(s_shop)  #print(shop_s)
            if city_map[plots][boxes] == "HWY":
                s_hwy = HWY_score(plots,boxes)
                highway_s += s_hwy
                l_hwy_score.append(s_hwy) #print(highway_s)
            if city_map[plots][boxes] == "BCH":
                s_beach = BCH_score(plots,boxes)
                beach_s += s_beach
                l_bch_score.append(s_beach)  #print(beach_s)
            total = house_s + factory_s + shop_s + highway_s + beach_s
            building_totalscore = [house_s,factory_s,shop_s,highway_s,beach_s]
    if factory_counter >= 4:
        for four in range(4):
            l_fac_score.append(4)
        for one in range(factory_counter-4):
            l_fac_score.append(1)
    elif factory_counter <4:
        for number in range(factory_counter):
            l_fac_score.append(factory_counter)
    for i in range(len(building_masterlist)):
        string = ""
        if len(building_masterlist[i]) > 0: 
            for l in building_masterlist[i]: #[4,4,4,4,1] ---> 4 + 4 + 4 + 4 + 1 +
                string += (str(l) + " + ")
            string = string.rstrip(" + ") # 4 + 4 + 4 + 4 
            print("{}: {} = {}".format(building_typelist[i],string,building_totalscore[i]))      
    print("Total score: {}".format(total))
    return total

def FAC_score(plots,boxes,factory_s,factory_counter): #Gets back the score for Factory
    fac_score = 0
    if factory_counter == 0:
        fac_score = 1
    if factory_counter == 1:
        fac_score = 3
    if factory_counter == 2:
        fac_score = 5
    if factory_counter == 3:
        fac_score = 7
    if factory_s >= 16:
        fac_score = 1
    return fac_score

def HSE_score(plots,boxes): #Gets back the score for House
    hse_score = 0
    if plots != 0:
        up_building = (city_map[plots-1][boxes])
        score = building_type(up_building)
        hse_score += score
    if plots != 3:
        down_building = (city_map[plots+1][boxes]) 
        score = building_type(down_building)
        hse_score += score
    if boxes != 0:
        left_building = (city_map[plots][boxes-1])  
        score = building_type(left_building)
        hse_score += score 
    if boxes != 3:
        right_building = (city_map[plots][boxes+1])  
        score = building_type(right_building)
        hse_score += score
    if hse_score < 0:
        hse_score = 1
    return hse_score

def SHP_score(plots,boxes): #Gets back the score for Shops
    shp_score = 0
    shp_s_build = ["SHP","FAC","HSE","BCH","HWY"]
    if plots != 0:
        up_building = (city_map[plots-1][boxes])
        shp_s_build = shop_check(up_building,shp_s_build)
    if plots != 3:
        down_building = (city_map[plots+1][boxes])
        shp_s_build = shop_check(down_building,shp_s_build)
    if boxes != 0:
        left_building = (city_map[plots][boxes-1])   
        shp_s_build = shop_check(left_building,shp_s_build)
    if boxes != 3:
        right_building = (city_map[plots][boxes+1])
        shp_s_build = shop_check(right_building,shp_s_build)
    shp_score = 5 - len(shp_s_build)
    return shp_score

def HWY_score(plots,boxes): #Gets back the score for Highway
    hwy_score = 0
    counter = 0
    non_high = ["SHP","FAC","HSE","BCH"," "]
    if boxes != 0:
        left_building = (city_map[plots][boxes-1])
        if left_building == "HWY":
            counter += 1
    if boxes != 3:
        right_building = (city_map[plots][boxes+1])
        if right_building == "HWY":
            counter +=1
    if counter == 0:
        hwy_score = 1
    if counter == 1:
        hwy_score = 2
    if counter == 2:
        hwy_score = 3
    for i in range(len(city_map[plots])):
        for e in range(len(non_high)):
            if city_map[i] == ["HWY","HWY","HWY",non_high[e]]:
                hwy_score = 3
            if city_map[i] == ["HWY","HWY",non_high[e],"HWY"]:
                hwy_score = 5
                msg = "2 + 2 + 1"
                return msg
            if city_map[i] == ["HWY",non_high[e],"HWY","HWY"]:
                hwy_score = 5
                msg = "1 + 2 + 2"
                return msg
            if city_map[i] == [non_high[e],"HWY","HWY","HWY"]:
                hwy_score = 3
            elif city_map[i] == ["HWY","HWY","HWY","HWY"]:
                 hwy_score = 4
        return(hwy_score)
    
def BCH_score(plots,boxes): #Gets back the score for Beach
    bch_score = 0
    if boxes == 0:
        bch_score += 3
    elif boxes == 3:
        bch_score += 3
    else:
        bch_score +=1
    return bch_score

def game_save(): #Saves the game into a txtfile
    file = open("savefile.txt",'w')
    file.truncate() #whenever new file is made
    file.write(str(city_map) + "\n")
    
def remain_save(): #Saves the remaining buildings into a txtfile
    file = open("remainfile.txt",'w')
    file.truncate()
    file.write(str(countbuilding) +"\n")
    
def save_score(play_name): #Saves scores into a file
    total = MAP_SCAN()
    scorefile = open("scorefile.txt","a")
    scorefile.write(play_name + ','+str(total)+"\n")
    scorefile.close()
    lists = high_score()
    highscore_list = lists[0]
    name_list = lists[1]
    return scorefile,total,highscore_list,name_list

def open_score(): #Retrieve scores from scorefile
    file= open("scorefile.txt","r")
    score_list=[]
    score_list.append()
    return score_list

def print_high_Scores(highscore_list, name_list): #Highscore menu
    print("-"*9," HIGH SCORES ","-"*9)
    print("Pos","Player"," "*16,"Score")
    print("-"*3,"-"*6," "*16,"-"*5)
    numberl = len(highscore_list)
    if numberl > 10:
        numberl = 10
    for score in range(0,numberl):
        print(" {:2d}.{:20s}{:>8d}".format((score+1),(name_list[score]),(highscore_list[score])))
    print("-"*33)
    
def sort_score(highscore_list, name_list): #Sorts the name to the score
          l = len(highscore_list)
          for i in range(0,l):
              for j in range(0,l-i-1):
                  if highscore_list[j] < highscore_list[j+1]:
                      tempscore = highscore_list[j]
                      highscore_list[j] = highscore_list[j+1]
                      highscore_list[j+1] = tempscore
                      tempname = name_list[j]
                      name_list[j] = name_list[j+1]
                      name_list[j+1] = tempname
          return highscore_list, name_list
        
def high_score():
    highscore_list=[]
    name_list = []
    file= open("scorefile.txt","r") #put score into notepad
    for line in file:
        line = line.strip("\n")
        line = line.split(',')
        highscore_list.append(int(line[1]))
        name_list.append(line[0])
    scores = sort_score(highscore_list, name_list)
    return scores[0], scores[1] #Printing of score

def print_position(play_name):  #Gets the position for final line before highscore at turn 17
    values = save_score(play_name)
    total = values[1]
    highscore_list = values[2]
    name_list = values[3]
    position_number = (name_list.index(play_name) +1 )
    print("Congratulations! You made the high score board at postion {}".format(position_number))
    
while True: #Start game# Main Menu
    print("Welcome, mayor of Simp City!")
    print("-"*28)
    print("1. Start new game")
    print("2. Load saved game")
    print("3. Show high scores")
    print()
    print("0.Exit") 
    try:
        menuchoice = int(input("Your choice?" )) 
        if menuchoice == 1:
            countbuilding = {"BCH":8,"FAC":8,"HSE":8,"SHP":8,"HWY":8}
            turn = 1
            city_map = [[" "," "," "," "],\
            [" "," "," "," "],\
            [" "," "," "," "],\
            [" "," "," "," "]]
        elif menuchoice == 2:
            turn = load_save()[1]
            city_map = load_save()[0]
            countbuilding = load_save()[2]
        elif menuchoice == 3:
            try:
                lists1 = high_score()
                print_high_Scores(lists1[0], lists1[1])
            except:
                print("There are no highscores.")
                print("-"*9," HIGH SCORES ","-"*9)
                print("Pos","Player"," "*16,"Score")
                print("-"*3,"-"*6," "*16,"-"*5)
                print("-"*33)
            continue
        elif menuchoice == 0:
            break
        else:
            print("Invalid option,please try again.")
            continue
    except:
        print("Invalid option,please try again.")
        continue
    while True: #1.1 Start the turn from 1 to 16
        if turn <= 16:
            print ("Turn",turn)
            SIMPCITY()
            Randombuildinglist = BUILDING_GENERATOR()  
            print("1. Build a {}".format(Randombuildinglist[0]))
            print("2. Build a {}".format(Randombuildinglist[1]))
            print("3. See remaining buildings") 
            print("4. See current score")
            print()
            print("5. Save game")
            print("0. Exit to main menu")
            try:
                gamechoice = int(input("Your choice?"))
                if gamechoice == 1 or gamechoice == 2: #Game choices to build buildings onto the map
                    BUILDING_DEDUCTOR() #Deducts them from dictionary and remaining building list
                    try:
                        coordinates = input("Build where?")
                        if len(coordinates) != 2:
                            print("Invalid option,please try again.")
                        elif len(coordinates) == 2:
                            if coordinates[0] == "a":
                                column = 0
                            elif coordinates[0] =="b":
                                column = 1
                            elif coordinates[0] =="c":
                                column = 2
                            elif coordinates[0] =="d":
                                column = 3
                            row = int(coordinates[1]) - 1
                            if turn == 1:
                                city_map[row][column] = Randombuildinglist[gamechoice-1]
                                turn += 1
                            elif turn != 1:
                                check = AdjCheck() #Checking if there are adj buildings
                                if check:
                                    city_map[row][column] = Randombuildinglist[gamechoice-1]
                                    turn +=1
                                else:
                                    print("You must build next to an exisiting build.")
                    except:
                        print("Invalid option,please try again.")
                        continue
                elif gamechoice == 3: #To display remaining buildings
                    DISPLAY_REMAININGS()
                elif gamechoice == 4: #To display the scoring system
                    MAP_SCAN()
                elif gamechoice == 5: #To save the game map as well as the remaining buildings
                    game_save()
                    remain_save()
                    print("Game saved!")
                elif gamechoice == 0: #End the game and exit back to the main menu
                    break
                else:
                    print("Invalid option,please try again.")
                    continue
            except:
                print("Invalid option,please try again.")
                continue
        elif turn == 17: #Prevents turn from going after 17
            print("Final layout of Simp City:")
            SIMPCITY()
            while True:
                play_name = input("Please enter your name (max 20 chars): ")
                if len(play_name)<= 20:
                    break
            print_position(play_name)
            lists1 = high_score()
            print_high_Scores(lists1[0], lists1[1])
            break
