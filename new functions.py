print("WELCOME TO VEHICLE MUSIC SYSTEM")
name=input("enter user name :")
print(f"WELCOME TO VEHICLE MUSIC SYSTEM {name}!")
vehicle_model=input("enter vehicle model: ")
print(type(vehicle_model))
flag= True
songs=[]
category_data={}
recently_played=[]
def songs_list():
    return ["believer", "faded", "perfect", "thunder", "shape of you"]

def ViewAvailableSongs():
            print("Entered into view Songs Section")
            songs1=list(songs_list())
            for user_song in songs:# it checks the user song in songs list 
                songs1.append(user_song[0])
          
            for index,song in enumerate(songs1):#'''enumrate used to track the index (it prints with index )'''
                print(f"{index}.{song}" )
            options1=input("Do u want to view Category wise?(yes/No)")
       
            match options1:
                case "yes":
                    print("\n1.Devotional")
                    print("2.Love")
                    print("3.Melody")
                    print("4.Mass hit")
                    print("5.Latest")
                    print("6.Exit")
                    select = int(input("select category : ")) 
                    match select:
                                           
                        case 1:
                            for user_type in songs:  
                                if user_type[2] == "Devotional":#'''it checks the usertype matches with given category'''
                                    print(user_type[0], "with duration",user_type[1])
                    
                        case 2:
                            for user_type in songs:
                                if user_type[2] == "Love":
                                    print(user_type[0],"with duration", user_type[1])
                    
                        case 3:
                            for user_type in songs:
                                if user_type[2] == "Melody":
                                    print(user_type[0],"with duration", user_type[1])
                    
                        case 4:
                            for user_type in songs:
                                if user_type[2] == "Mass hit":
                                    print(user_type[0],"with duration", user_type[1])
                    
                        case 5:
                            for user_type in songs:
                                if user_type[2] == "Latest":
                                    print(user_type[0], "with duration",user_type[1])
                    
                 
                        case 6:
                            print("Thank you ")
                            print("Exited From View Section ")
                            #break
                case "No":
                    print("Thank you ")
def PlaySongs():
            print("Entered into PlaySong Section ")
            song2 = list(songs_list())# create a copy of default songs list

            for s in songs:
                song2.append(s[0])# s[0] represents song name from tuple

            for i, s in enumerate(song2):# display songs with index numbers
                print(f"{i}.{s}")

            song_number = int(input("enter song number: "))

            if 0 <= song_number < len(song2):# checks whether selected song number exists in list range
                current_song = song2[song_number]
                print("now playing :", current_song)
                recently_played.append(current_song) # stores song in recently played list
            else:
                print("Invalid Selection")
def AddNewSongs():
    print("Entered into Add Songs Section")
    while True:
               
                print("1.Devotional")
                print("2.Love songs")
                print("3.Melody songs")
                print("4.Mass hit")
                print("5.Latest")
                print("6.Exit ")
                category=input("select category: ")
                match category:
                    case "1":
                          
                           
                            if  category == "1":
                                song = input("enter song : ")
                                song_duration=float(input("enter song duration: "))
                                songs.append((song,song_duration,"Devotional"))#'''it appends the data of song name and song duration in songs'''
                                category_data.setdefault(category, set()).add((song, song_duration))
                                #'''In category data if category is not available it creates the new set with set default and adds the data of song name & song duration'''
                                print({song,song_duration})
                                print(f"devotional songs playing {song}  with {song_duration}")
                                print(songs)
                            
                        
                                         
                       
        
                        
                    case "2":
                            if  category == "2":
                                song = input("enter song : ")
                                song_duration=float(input("enter song duration: "))
                                songs.append((song,song_duration,"Love"))
                                category_data.setdefault(category, set()).add((song, song_duration))
                                print({song,song_duration})
                       
                                print(f" love  songs playing {song}  with {song_duration}")
                                print(songs)
                            
                      
                    case "3":
                            if  category == "3":
                                song = input("enter song : ")
                                song_duration=float(input("enter song duration: "))
                                songs.append((song,song_duration,"Melody"))
                                category_data.setdefault(category, set()).add((song, song_duration))
                                print({song,song_duration})
                                print(f" melody  songs playing {song}  with {song_duration}")
                                print(songs)
                            
                      
                      
                    case "4":
                            if  category == "4":
                                song = input("enter song : ")
                                song_duration=float(input("enter song duration: "))
                                songs.append((song,song_duration,"Mass hit"))
                                category_data.setdefault(category, set()).add((song, song_duration))
                                print({song,song_duration})
                                print(f"Mass hit songs playing {song}  with {song_duration}")
                                print(songs)
                                
                       
                    case "5":
                            if  category == "5":
                                song = input("enter song : ")
                                song_duration=float(input("enter song duration: "))
                                songs.append((song,song_duration,"Latest"))
                                category_data.setdefault(category, set()).add((song, song_duration))
                                print({song,song_duration})
                                print(f"Latest songs playing {song}  with {song_duration}" )
                                print(songs)
                                
                        
                       
                    case "6":
                        if category == "6":
                            print("exited from Add Song Section")     
                            break
                
                songs1=songs_list()+songs
                print(songs1)
def RemoveSongs():
            print("Entered into Remove Songs Secton ")   
            print("1.only selected song from multiple songs")
            print("2.single song")
            print("3.ALL songs")
            print("4.Delete songs in Category")
            print("5.Exit ")

            category = input("select category: ")

            match category:

                case "1" | "2":
                    name = input("enter song: ")
                    before = len(songs)

                    for song in songs:
                        if song[0] == name:#'''song[0] represents the song name in songs list and it checks with the user input if it matches then song removes from the list'''
                            songs.remove(song)
                            print("song Removed")
                            break
                    else:
                        print("No songs Available")

                    after = len(songs)
                    print("songs Deleted:", before - after)
                    print("songs Remaining:", after)

                case "3":
                    songs.clear() #'''.clear() is used to remove all songs at once '''
                    category_data.clear()   
                    print("songs Removed")
                    print("No songs Available")
                
                case "4":
                    
                    print("1.Devotional")
                    print("2.Love songs")
                    print("3.Melody songs")
                    print("4.Mass hit songs")
                    print("5.LATEST SONGS")

                    remove = input("select category: ")

                    category1 = {
                        "1": "Devotional",
                        "2": "Love",
                        "3": "Melody",
                        "4": "Mass Hit",
                        "5": "Latest"
                    }

                    if remove in category1:
                        before = len(songs)

                        # remove songs of selected category
                        songs[:] = [s for s in songs if s[2] != category1[remove]]
                        '''songs[;] it creates the copy of the list'''
                        # also remove from category_data (set)
                        if remove in category_data:
                             category_data[remove].clear()

                        after = len(songs)

                        print("songs Deleted:", before - after)
                        print("songs Remaining:", after)
                        print("Exited From Remove Song Section")
                    else:
                        print("Invalid selection")
def SearchSongs():
            print("Entered into Search Song Section")

            song_name=input("enter song name: ")
            print(song_name)
            all_songs = songs_list()
            songs1=songs_list()+songs # combines default songs and user-added songs
           
            for item in songs1:

                if type(item) == tuple:  # checks whether item is tuple (user-added song)
                    all_songs.append(item[0]) # item[0] represents song name

                else:
                    all_songs.append(item)

            if song_name in all_songs: # checks whether entered song exists in songs list
                print("song found")
            else:
                print("song not found")
            find=input("Do u want search  Category wise?(yes/No) ")  # loops through user-added songs
            match find:
                case "yes":
                   
                        print("1.Devotional")
                        print("2.Love songs")
                        print("3.Melody songs")
                        print("4.Mass hit songs")
                        print("5.LATEST SONGS")
                        print("6.Exit ")
                        search1= input("select category: ")
                      
                        for song in songs:   
                            if search1 == "1" and song[2] == "Devotional":         # checks devotional category
                                print(song[0], "with duration", song[1]) 
                            elif search1 == "2" and song[2] == "Love":
                                print(song[0], "with duration", song[1] )
                            elif search1 == "3" and song[2] == "Melody":
                                print(song[0], "with duration", song[1]) 
                            elif search1 == "4" and song[2] == "Mass Hit":
                                print(song[0], "with duration", song[1] )
                            elif search1 == "5" and song[2] == "Latest":
                                print(song[0], "with duration", song[1])
                                                        
                                
                case "No":
                        print("song not found")
               
def RepeatSongs():
            print("Entered into Repeat Songs Section")
            song_name=input("enter song name: ")
            count=0                                    #initially the count is 0
            rep=int(input("enter repitions: "))
            while count < rep: # loop runs until count becomes equal to repetitions
                print(f"playing {song_name} multiple times")
                print("Exited from Repeat Song Section ")
                count += 1     # increments count by 1 after every iteration
            print(count)
def ShuffleSongs():
            print("Entered into Shuffle Song Section")
            song_number=int(input("enter song number:"))
            song2 = list(songs_list())
            for s in songs:
                song2.append(s[0])    # s[0] represents song name from tuple

            for index, song in enumerate(song2):
                print(f"{index}.{song}")
            if 0 <= song_number < len(song2):    #''' it compares the song number and length of the song list'''
                print("Shuffled playlist", song2[song_number])
                print("Exited from Shuffled Song Section")
            else:
                print("Invalid section")
def ViewRecentlyPlayed():
            print("Entered into View Recently Section ")
            if recently_played: # checks whether recently_played list contains songs
                print("Recently Played Songs:")
                for song in recently_played:     # loops through recently played songs list
                    print(song)
            else:
                print("No songs played yet")
                print("Exited from View Recently Played Section")
            
           
def ControlVolume():
            print("Entered into Volume Control Section")
            
            volume=50

        

            isExit = False
            min_volume = 0
            volume = 40
            max_volume = 100
            while(not isExit):
                choice = int(input(" 1.Increase Volume \n 2.Decrease Volume \n 3.Mute \n 4.Exit"))

                

                if choice == 1:
                    
                    volume = volume + 10
                    print("increasing volume",volume)
                    if volume >= max_volume:
                        volume =max_volume #'''if volume is more than 100 it doesn't change stays upto 100(Max Volume set to 100)'''
                elif choice == 2:
                    volume -= 10
                if volume < min_volume:
                    volume= min_volume # min volume set to 0
                elif choice == 3:
                    volume= 0
                
                elif choice == 4:
                    isExit = True
                    print("exit")
                

                total_blocks = 10  # total number of blocks displayed in volume bar
                # min_volume = 0
                
                volume_percentage = ((volume/max_volume)*100)  # calculates current volume percentage
                empty = (max_volume - volume_percentage)/total_blocks  # calculates empty blocks in volume bar

                filled = total_blocks - empty  # calculates filled blocks in volume bar

                bar = " "  # stores volume bar symbols
                
                for item in range(total_blocks):
                    if item<=filled:
                        bar += "#"   # adds filled blocks
                    else:
                        bar += "-"    # adds empty blocks
                print(f"Volume: [{bar}] {volume_percentage}%")
                print("Exited From Control Volume Section")
while True:
    print("1.View available songs")
    print("2.Play songs")
    print("3.Add new song")
    print("4.Remove songs")
    print("5.Search songs")
    print("6.Repeat songs")
    print("7.Shuffle playlist")
    print("8.View recently played songs")
    print("9.Control volume")
    print("10.Exit application")

    options=int(input("enter choice: "))
 
    match options:
    #view available songs 
        case 1:
            ViewAvailableSongs()
              
              
        case 2:
    #play songs 
           PlaySongs()
        case 3:
    #Add New Songs
           AddNewSongs() 
        case 4:
    # Remove Songs 
            RemoveSongs()  
            
        case 5:
    #search songs 
            
            SearchSongs()   
                
        case 6: 
    #Repeat songs
            RepeatSongs()
            
        case 7: 
    #shuffle songs 
            ShuffleSongs()
        
        case 8: 
    #view recently played songs 
            ViewRecentlyPlayed()
        case 9:
    #control volume
           ControlVolume()
        case 10:
            
            break               
print("Thank You for using vehicle Music System ")
