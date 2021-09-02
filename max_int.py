
""" Forrit biður notanda endurtekið um slá inn tölu
    Forriti geymir hæstu tölu notanda
    Forritið keyrir þar til notandi slær in neikvæða tölu
    Þegar forritið slær inn neikvæða tölu prentar forritið hæstu tölu sem notandi sló inn """
    
max_int = 0
num_int = 0

while num_int >= 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    # Fill in the missing code
    if num_int > max_int:
        max_int = num_int
        
print("The maximum is", max_int)    # Do not change this line