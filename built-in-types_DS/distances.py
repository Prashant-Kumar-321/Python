distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}


def  main():
    # for spacecraft in distances.keys(): 
    #     print(f"{spacecraft} is at {distances[spacecraft]} AU from Earth")
    
    # Check if a key is available in the dictionary
    print('New Horizons' in distances)

    # for distance in distances.values(): 
        # print(f"{distance} AU is {convert(distance)} KM")


def convert(au): 
    return round((au * 149597870700)/1000, 2)


if __name__ == "__main__": 
    main()