#ohms law calculator.py
while True:
    try:
        my_input = input("Enter Voltage (V)or 'exist' to stop ")
        if my_input.lower() == 'exist':
            break

        resistance = float(input("Enter resistance (R) in ohms: "))
        if resistance == 0:
            print("Resistance cannot be zero. Please enter a valid resistance.")
            continue

        voltage = float(input("Enter voltage (V) in volts: "))
        current = voltage / resistance
        print(f"The current (I) is {current} amperes.")
        #calculate power
        power = voltage * current
        print(f"The power (P) is {power} watts.")
        print(f"The resistance (R) is {resistance} ohms.")
        break
    except ValueError:
        print("Please enter a valid number.")