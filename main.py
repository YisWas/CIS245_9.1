# My virtual car garage week 8 CSI

class Vehical:  # creating main class
    def __init__(self):
        self.vehical_options = {}

    def setMake(self, make):
        self.vehical_options['Make'] = make

    def setModel(self, model):
        self.vehical_options['Model'] = model

    def displayOptions(self):
        print("")
        print(f"Make: {self.vehical_options['Make']}")
        print(f"Model: {self.vehical_options['Model']}")
        print("")


class Car(Vehical):
    def setDoors(self, door):
        self.vehical_options['Door'] = door

    def displayOptions(self):
        print("")
        print("You have made a car here are the options you entered")
        super().displayOptions()
        print(f"door: {self.vehical_options['Door']}")
        print("")


class Pickup(Vehical):
    def setBedLength(self, bed_length):
        self.vehical_options['Bed Length'] = bed_length

    def displayOptions(self):
        print("")
        print("You have made a truck here are the options you entered")
        super().displayOptions()
        print(f"bed length: {self.vehical_options['Bed Length']}")
        print('')


def main():
    car_type = input("Please enter the type of vehical you wish to create [Car/Pickup]: ")
    while car_type.lower() != "car" and car_type.lower() != "pickup":
        print("Please enter a valid car!")
        car_type = input("Please enter the type of vehical you wish to create [Car/Pickup]: ")
    vehical_make = input("Please enter a vehical make: ")
    vehical_model = input("Please enter a vehical model: ")

    if car_type == "car":
        my_vehical = Car()
        door = input("How many doors does the car have? [2/4/6] : ")
        while door != "2" and door != "4" and door != "6":  #locking in the options
            print("Please enter a valid option! ")
            door = (input("How many doors does the car have? [2/4/6] : "))
        my_vehical.setDoors(door) #putting the option through the class
    elif car_type == "pickup":
        my_vehical = Pickup()
        bed_length = input("How long is the bed of the pickup? [5.8/6.5/8] : ")
        while bed_length != "5.8" and bed_length != "6.5" and bed_length != "8":
            print("Please enter a valid option! ")
            bed_length = input("How long is the bed of the pickup?: ")
        my_vehical.setBedLength(bed_length)

    my_vehical.setMake(vehical_make)
    my_vehical.setModel(vehical_model)
    my_vehical.displayOptions()

    runAgain = input("Do you want to make another Vehical? [y/n] ")
    if runAgain == "y":
        main()
    else:
        print("Thank you for using my program!")

main()