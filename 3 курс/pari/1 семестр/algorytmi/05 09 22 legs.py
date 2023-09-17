def change_legs(legs: list):
    first_leg = legs[0]
    legs.append(first_leg)

    start_leg = 0
    end_leg = 0
    
    for i in range(1, len(legs)):
        if legs[i] != first_leg:
            if start_leg == 0:
                start_leg = i
            else:
                end_leg = i

        else:
            if start_leg != 0:
                if not end_leg:
                    print(start_leg + 1, "! НОГА!!")

                else:
                    print("С", start_leg + 1, "по", end_leg + 1, "! НОГА!!")
                
                start_leg = 0
                end_leg = 0


change_legs(["R", "R", "L", "R", "L", "L", "L", "R", "L"])