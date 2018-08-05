def tempWriter(temps,filepath):
    """Converts list of temperatures in celsius to fahrenheit
    and writes these to a file defined by filepath. """
    with open(filepath, "w") as file:
        for c in temps:
            if (c>-273.15):
                f = c * 9/5 + 32
                file.write(str(f)+"\n")

temperatures=[10,-20,0,30, 20]
tempWriter(temperatures, "temp.txt")
