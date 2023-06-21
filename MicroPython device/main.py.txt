from machine import ADC, Pin
import time


def main():
    # Setup

    # PINs used by potentiometers
    PINs = [25, 33, 32, 35, 34]

    # Number of potentiometers is equal to the number of PINs 
    number_of_potentiometers = len(PINs)

    # Initialise the list of potentiometer objects
    ADCs = []

    # Initialise the list of volume levels
    volume_levels = []

    # Instead of writing Pin(PINs[i]) for every PIN we do it in a for loop and keep objects in a ADCs list 
    for i in range(number_of_potentiometers):
        ADCs.append(ADC(Pin(PINs[i])))
    
    # Same with volume levels, there will be as many volume levels as there are potentiometers
    for i in range(number_of_potentiometers):
        volume_levels.append(0)
    
    # initialise previous volume list, we will compare it to the current volume and print data only upon changes
    previous_volume_levels = []
    for i in range(number_of_potentiometers):
        previous_volume_levels.append(0)
    
    # attenuation
    for i in ADCs:
        i.atten(ADC.ATTN_11DB)
    
    separator = " "
    
    # an infinite loop
    while True: 
        # we calculate a volume level (0-100) for every potentiometer
        for i in range(number_of_potentiometers):
            # 100 - value because for some reason my potentiometers only work in reverse (anticlockwise is max)
            volume_levels[i] = 100 - int(ADCs[i].read()/4095*100)
        
        if volume_levels != previous_volume_levels:
            # and we construct a message to be send to PC 
            print(separator.join(map(str, volume_levels)))
        
        for i in range(number_of_potentiometers):
            previous_volume_levels[i] = volume_levels[i]
        
              
        # a sleep function
        time.sleep(0.05)


main()
 
