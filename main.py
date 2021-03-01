from Cup import Cup 

def main():
 cup_for_tea = Cup (400, "clay", "red")
 cup_for_school = Cup ()
 cup_for_camp = Cup (300, "metal", "silver")

 place = Cup.getLocation()

 print (cup_for_tea.__str__() + place + "\n" + cup_for_school.__str__() \
     + place + "\n" + cup_for_camp.__str__() + place )

if __name__ == "__main__":
    main()