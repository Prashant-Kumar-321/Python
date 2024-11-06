""" 
    KeyError

    :-- RULES TO BE LIKE THEM --: 
    Get an early start
    Exploit the anonymity of the internet 
    Get good help
    Exploit the your youth
    Be willing to make some sacrifices
"""

def main(): 
    spacecraft = {
        "name": "James Webb Space Telescope",
        "distance": 123,
    }
    
    spacecraft.update({
        "distance": 0.01,
        "Orbit": "Sun",
    })

    print(create_report(spacecraft))


def create_report(spacecraft): 
    unit = ""
    return f"""
    ========== REPORT ==========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")}
    Orbit: {spacecraft.get("Orbit", "Unknown")}

    =============================
    """


if __name__ == "__main__": 
    main()
