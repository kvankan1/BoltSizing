import numpy as np
from math import sin, cos

#====================================================Set Up Inital Classes========================================================================#
class Bolt:
    def __init__(self, ultimate_tensile_stress: np.array, yield_strength: np.array, proof_stress:float, elongation_fracture:float, rockwell_hardness:np.array, alpha = float):
        self.ultimate_tensile_stress = ultimate_tensile_stress #[Nom, Min] [Mpa]
        self.yield_strength = yield_strength                   #[Nom, Min] [Mpa]
        self.proof_stress = proof_stress                       #[Mpa]
        self.elongation_fracture = elongation_fracture         #[%]
        self.rockwell_hardness = rockwell_hardness             #[]
        self.alpha = alpha                                     #[rad]

class Fastener:
    def __init__(self, E: float, ultimate_tensile_stress: float, yield_strength: float):
        self.E = E                                              #[Gpa]
        self.utlimate_tensile_stress = ultimate_tensile_stress  #[Mpa]
        self.yield_strength = yield_strength                    #[Mpa]

class ReactionForces:
    def __init__(self, Rz: float, Ry: float, Rx: float, angle_normal_z: float, angle_normal_x:float, angle_normal_y:float):
        self.Rz = Rz                               #[N] 
        self.Ry = Ry                               #[N]
        self.Rx = Rx                               #[N]
        self.angle_normal_x = angle_normal_x     #angle from normal axis of the screw to the x axis [rad]
        self.angle_normal_y = angle_normal_y     #angle from normal axis of the screw to the y axis [rad]
        self.angle_normal_z = angle_normal_z     #angle from normal axis of the screw to the z axis [rad]

        self.Rn = Rz*cos(angle_normal_z)            #Normal Force [N]
        self.Rt = np.sqrt((Rx*cos(angle_normal_x))**2 + (Ry*cos(angle_normal_y))**2 )    ##Vector summation and magnitude to get transverse force

#====================================================Set Up Inital Functions========================================================================#

def RoundUpAndGetIndex(input_value, values_array):
    # Filter the values that are greater than or equal to the input value
    filtered_values = [value for value in values_array if value >= input_value]

    # Find the minimum of the filtered values
    rounded_value = min(filtered_values)

    # Find the index of the rounded value in the original array
    original_index = list(values_array).index(rounded_value)

    return original_index

def GetNominalDiameterPreload(Fa, Fq, ut):
    if Fa < Fq/ut:
        load = Fq
        steps = 4
    else: 
        load = Fa
        steps = 2
    
    load_array = np.array([250, 400, 630, 1000, 1600, 2500, 4000, 6300, 10000, 16000, 25000, 40000, 63000, 100000, 160000, 250000, 400000, 630000])    #[N]
    nominal_diameter_array = np.array([0, 0, 0, 3, 3, 3, 4, 5, 6, 8, 10, 12, 14, 18, 22, 27, 33, 39])               #[mm]

    index = RoundUpAndGetIndex(load, load_array) + steps      #Get the index that corresponds to the list by rounding it up to the closest load, add corresponding steps
    nominal_diameter = nominal_diameter_array[index]            
    F_Mmin = load_array[index]                                                          
    F_Mmax = load_array[index + 1]                           #Another step for using a torque wrench, see p116

    return nominal_diameter, F_Mmin, F_Mmax



#nominal_diameter, F_Mmin, F_Mmax = (GetNominalDiameterPreload(600, 200, 0.2))









##Assume Kb = 3*Kp
K_p = 1.
K_b = 3*K_p

##Assume x/s = 1
x_s = 1.

Fastener_6082_T6 = Fastener(E= 71., ultimate_tensile_stress = 140, yield_strength = 260)



Bolt_10_9 = Bolt(ultimate_tensile_stress = np.array([1000., 1040.]),
                 yield_strength = np.array([900., 940.]),
                 proof_stress = 830. , 
                 elongation_fracture= 9. , 
                 rockwell_hardness= np.array(["CS32", "CS39"]),
                 alpha = np.pi/3)





