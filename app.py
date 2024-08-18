import json_mod

page = "home"
devider = "===================="

anime_data = json_mod.read_json("anime.json")



def show_home():
    while True:  # Loop to keep showing the menu until valid input is received
        print(" ")
        print (devider)
        print ('Home')
        print (devider)

        print("1 - View/Edit")
        print("2 - Create")
        cmd = input("> ")

        if cmd == "1":
            page = "edit"
            show_view()
            break  # Exit the loop after handling the input

        elif cmd == "2":
            page ="create"
            show_create()
            break  # Exit the loop after handling the input

        else:
            print ("-----")
            print("Invalid input. Please enter 1 or 2.")  # Notify the user of invalid input
            print ("-----")
    
    
def show_create():
    while True:
        print(" ")
        print (devider)
        print ('Create')
        print (devider)

        animeName = input("Enter name: ")
        if animeName == '' or animeName == " ":
            pass
        else: 
            new_anime_id = len(anime_data) + 1
            anime_data[animeName] = {
                "id": new_anime_id,
                "ep": 0
            }
            json_mod.write_json("anime.json", anime_data)
            page = "home"
            show_home()
            break


def show_view (): 
    while True:
        print(" ")
        print (devider)
        print ("View")
        print (devider)

        print ("0 - back")
        for name, details in anime_data.items():
            print (f"{details["id"]} - {name} ({details["ep"]})")
        cmd = input ("> ")

        if cmd == "0":
            show_home()
            break
        else:
            for n, details in anime_data.items():
                if int(cmd) == details["id"]:
                    show_edit(name=n)
                    break
        
            
def show_edit (name):
    print(" ")
    print (devider)
    print ('Edit')
    print (devider)
    
    ep_num = input("Enter episode number: ")
    anime_data[name]['ep'] = int(ep_num)
    json_mod.write_json("anime.json", anime_data)
    show_home()




show_home()