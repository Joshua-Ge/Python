"""This is a calculator that calculates the atomic mass of atoms in U"""

use = "yes"

while use == "yes":
    protons = input("How many protons are in your atom? >> ")
    nutrons = input("How many nutrons are in your atom? >> ")

    protons = int(protons)
    nutrons = int(nutrons)

    atomicMass = protons + nutrons

    print(atomicMass, "U")

    use = input("Would you like to use this again? >> ")
