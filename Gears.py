from math import *

diameterSunGear=float(input("Enter the desired diameter of the sun gear:: "))

module=float(input("Enter the desired module:: "))

ratio=float(input("Enter the desired ratio of ring to sun gear:: "))

pitch=module
diameterPlanetGear=diameterSunGear*(ratio-1)/2
diameterRingGear=ratio*diameterSunGear
numTeethSunGear=diameterSunGear/pitch
numTeethPlanetGear=diameterPlanetGear/pitch
numTeethRingGear=diameterRingGear/pitch

print("Diameter of Sun Gear:: " + str(diameterSunGear) + " mm\n" +
      "         of Planet Gear:: " + str(diameterPlanetGear) + " mm\n" +
      "         of Ring Gear:: " + str(diameterRingGear) + " mm\n" +
      "Number of Teeth on Sun Gear:: " + str(numTeethSunGear) + "\n" +
      "                on Planet Gear:: " + str(numTeethPlanetGear) + "\n" +
      "                on Ring Gear:: " + str(numTeethRingGear) + "\n" +
      "Pitch:: " + str(pitch) + "\n" +
      "Module:: " + str(module) + "\n" +
      "Ratio Sun:Planet:Ring:: 1:" + str((ratio-1)/2) + ":" + str(ratio) + "\n")
