import numpy as np
from sizing import ReactionForces, GetNominalDiameterPreload, RoundUpAndGetIndex


if __name__ == "__main__": 

    ut = 0.1  #Static Coefficient of friction at the interface, 0.1 to 0.28 for Steel-Aluminum Alloy (see p114 of german manual thing)


    Forces_1 = ReactionForces(Rx= -1066.4, Ry= 107.5, Rz=-221.93,angle_normal_x= 0, angle_normal_y= 0, angle_normal_z= 0)
    Forces_2 = ReactionForces(Rx= 768.41, Ry= 735.14, Rz=125.26,angle_normal_x= 0, angle_normal_y= 0, angle_normal_z= np.pi/4)
    Forces_3 = ReactionForces(Rx= -662.83, Ry= 220.21, Rz=-85.629,angle_normal_x= 0, angle_normal_y= 0, angle_normal_z= 0)
    Forces_4 = ReactionForces(Rx= 960.78, Ry= 837.15, Rz=-197.7,angle_normal_x= 0, angle_normal_y= 0, angle_normal_z= np.pi/4)

    for i in range(4):
        arr = [Forces_1, Forces_2, Forces_3, Forces_4]
        Force = arr[i]

        nominal_diameter, F_Mmin, F_Mmax = GetNominalDiameterPreload(Force.Rn, Force.Rt, ut)

        print(f"Support {i+1} :")
        print(f"Bolt Needed = M{nominal_diameter}")
        
        



