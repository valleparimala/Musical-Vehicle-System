# print("WELCOME TO VEHICLE MUSIC SYSTEM")
# name=input("enter user name :")
# print(f"WELCOME TO VEHICLE MUSIC SYSTEM {name}!")
# vehicle_model=input("enter vehicle model: ")
# print(type(vehicle_model))
flag= True
songs=[]
def songs_list():
    return ["believer", "faded", "perfect", "thunder", "shape of you"]
while True:
    print("1.View available songs")
    print("2.Play songs")
    print("3.Add new song")
    print("4.Search songs")
    print("5.Repeat songs")
    print("6.Shuffle playlist")
    print("7.View recently played songs")
    print("8.Control volume")
    print("9.Exit application")

    options=int(input("enter choice: "))
 
    match options:
    #view available songs 
        case 1:
            songs1=list(songs_list())
            for user_song in songs:
                songs1.append(user_song["name"])
          
            for index,song in enumerate(songs1):
                print(f"{index}.{song}" )
            options1=input("Do u want to view Category wise?(yes/no)")
       
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
                                if user_type.get("category")=="Devotional":
                                    print(user_type.get("name"))
                        case 2:    
                            for user_type in songs:
                                if user_type.get("category")=="Love":
                                    print(user_type.get("name"))
                        case 3:
                            for user_type in songs:
                                if user_type.get("category")=="Melody":
                                    print(user_type.get("name"))
                        case 4:
                            for user_type in songs:
                                if user_type.get("category")=="Mass hit":
                                    print(user_type.get("name"))
                        case 5:
                            for user_type in songs:
                                if user_type.get("category")=="Latest":
                                    print(user_type.get("name"))
                        case 6:
                            print("Thank you ")
                            break
                case "no":
                    print("Thank you ")
                    break
              
              
        case 2:
    #play songs 
            song2=songs_list()
            song_number=int(input("enter song number:"))
            if 0 <= song_number < len(song2):
                print("now playing :",song2[song_number])
            else:
                print("Invalid Selection")
        case 3:
         
            while True:
                
                print("1.Devotional")
                print("2.Love songs")
                print("3.Melody songs")
                print("4.Mass hit songs")
                print("5.LATEST SONGS")
                print("6.Exit ")
                category=input("select category: ")
                match category:
                    case "1":
                        song = input("enter song : ")
                        song_duration=float(input("enter song duration: "))
                       
                        songs.append({
                                    "name": song,
                                    "category": "Devotional",
                                    "duration": song_duration
                           
                        })
                        print(f"devotional songs playing {song}  with {song_duration}")
                        
                    case "2":
                        song = input("enter song : ")
                        song_duration=float(input("enter song duration: "))
                      
                        songs.append({
                                    "name": song,
                                    "category": "Love",
                                    "duration": song_duration
                           
                        })
                        print(f" love  songs playing {song}  with {song_duration}")
                      
                    case "3":
                        song = input("enter song : ")
                        song_duration=float(input("enter song duration: "))
                       
                        songs.append({
                                    "name": song,
                                    "category": "Melody",
                                    "duration": song_duration
                           
                        })
            
                        print(f" melody  songs playing {song}  with {song_duration}")
                      
                    case "4":
                        song = input("enter song : ")
                        song_duration=float(input("enter song duration: "))
                       
                        songs.append({
                                    "name": song,
                                    "category": "Mass hit",
                                    "duration": song_duration
                           
                        })
                        print(f"mass hit songs playing {song}  with {song_duration}")
                       
                    case "5":
                        song = input("enter song : ")
                        song_duration=float(input("enter song duration: "))
                        songs.append({
                                    "name": song,
                                    "category": "Latest",
                                    "duration": song_duration
                           
                        })
                            
                        print(f"Latest songs playing {song}  with {song_duration}" )
                        
                       
                    case "6":
                        print("exit")
                        break
                
                songs1=songs_list()+songs
            print(songs1)
        case 4:
              song_name=input("enter song name: ")
              print(song_name)
              all_songs = songs_list()
              songs1=songs_list()+songs
              for song_name in songs1:
                  all_songs.append(song[0])

              if song_name in songs1:
                  print("song found")
              else:
                  print("song not found")
        case 5: 
#Repeat songs 
            song_name=input("enter song name: ")
            count=0
            rep=int(input("enter repitions: "))
            while count < rep:
                print(f"playing {song_name} multiple times")
                count += 1
            print(count)
 
        case 6: 
        #shuffle songs 
            song_number=int(input("enter song number:"))
            if 0 <= song_number < len(songs_list()):
                print("Shuffled playlist", songs_list()[song_number])
            else:
                print("Invalid section")
        
        case 7: 
        #view recently played songs 
            song_number=int(input("enter song number:"))
            song_list=songs_list()
            if 0<= song_number <len(song_list):
                
                current_song=song_list[song_number]
                recently_played= current_song
                print(recently_played)
            else: 
                print("Invalid section")
        case 8:
    #control volume
            print("1.Increase  2.Decrease  3.Mute")
            choice = int(input("enter choice: "))
            volume=50

        

            isExit = False
            min_volume = 0
            volume = 40
            max_volume = 100
            while(not isExit):
                choice = int(input(" 1.increase \n 2.decrease \n 3.mute \n 4.Exit"))

                

                if choice == 1:
                    
                    volume = volume + 10
                    print("increasing volume",volume)
                    if volume >= max_volume:
                        volume =max_volume
                elif choice == 2:
                    volume -= 10
                if volume < min_volume:
                    volume= min_volume
                elif choice == 3:
                    volume= 0
                
                elif choice == 4:
                    isExit = True
                    print("exit")
                

                total_blocks = 10
                # min_volume = 0
                
                volume_percentage = ((volume/max_volume)*100)
                empty = (max_volume - volume_percentage)/total_blocks
                filled = total_blocks - empty

                bar = " "
                
                for i in range(total_blocks):
                    if i<=filled:
                        bar += "#"
                    else:
                        bar += "-"
                print(f"Volume: [{bar}] {volume_percentage}%")
        case 9:
            print("Exit Application")
            print("Thank You for using vehicle Music System ")
            break