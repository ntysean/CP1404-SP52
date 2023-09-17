from unreliable_car import UnreliableCar



def main():

    # create cars with different reliabilities
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    for i in range(1, 3):
        print("Attempting to drive {}km:".format(i))
        print("{:3} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:3} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    # print the final states of the cars
    print(good_car)
    print(bad_car)
main()