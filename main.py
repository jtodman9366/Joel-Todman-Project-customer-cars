print("~Tales at UMBC~\n (A place of fiction)")
print("========================")
print("Welcometo the UMBC\nCar Customization Form!")
print("========================")

# Make & Model Selection 
print("1. Select your car mske & model choice ")
print("  a.dodge")
print("  b.toyota")
print("  c.lexus")
print("  d.camary")
choice  = input("Please Enter 'a' - 'd' ")

#Upgrade Options
print()
print("2. Would you like to upgrade from  4-door sedan w/o sunroof to a 2-doorsedan with sunroof")
upgrade  = input("Please Enter 'yes' or 'no' ")

#Car Exterior
print()
print("3. What color would you like the exterior of your car? ")
ExteriorColor = input("Please Enter your exterior color you would like: ")

#Deluxe Package
print()
print("4. Would you like the Deluxe weather package? ")
deluxePackage  = input("Please Enter 'yes' or 'no' ")

#Car Engine
print()
print("5. What type of Engine would you like?")
print("  a.I-4 Entry Engine")
print("  b.V-6 Performance Engine")
print("  c.ECO Deisel Engine")
engineType = input("Please Enter 'a' - 'c' ")

#Heated Seats
print()
print("6. Would you like the Heated Seats option? ")
heatedSeats  = input("Please Enter 'yes' or 'no' ")
print()
print("========================")
print("~ Summary~ ")
print(f"Make & Model Option: {choice}\nUpgrade to 2-door Sedan With Sunroof: {upgrade}\nExterior Color: {ExteriorColor}\nDeluxe Weather Package: {deluxePackage}\nEngine Option: {engineType}\nHeated Seats: {heatedSeats}")
