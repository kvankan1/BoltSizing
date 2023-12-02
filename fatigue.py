import numpy as np
from math import log10, exp
import matplotlib.pyplot as plt

#We are given forces but as inputs we need stresses:

minimum_normal_stress = 100 #[Mpa]
maximum_normal_stress = -50 #[Mpa]

stress_amp = 0.5*(maximum_normal_stress - minimum_normal_stress)
stress_mean = 0.5*(maximum_normal_stress + minimum_normal_stress)
stress_range = maximum_normal_stress - minimum_normal_stress

R = maximum_normal_stress/minimum_normal_stress

#Material Constants 
stress_endurance = 55.9 #[Mpa]
uts = 132. # [Mpa]
E = 12.9 # [Gpa] [Young's Modulus] This works when we accidentally forget to convert it back to Mpa for the equations so lets pretend like we did that. I wont tell if you dont
stress_yield = 131. #[Mpa]

#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9960376/
#Coefficients for high cycle fatigue basquin's law
basquin_A = 206. #[Mpa]
basquin_B = -0.039 #[Mpa]

#https://www.sciencedirect.com/science/article/pii/S1359836807000285
#coefficiencts for low cycle fatigue basquin's law, used to get coefficients for low cycle fatigue law
coffin_A = 98. #[Mpa]
coffin_B = -0.071 #[Mpa]

#Getting the coefficients for the manson coffin equation (now reffered to as mc)
mc_B = basquin_B
mc_sigma_fprime = basquin_A/(2**mc_B)

mc_epsilon_fprime = coffin_A/((2**coffin_B))
mc_epslion_C = coffin_B

# #Basquin's Law Constants:
# Not confident this part is correct 
# basquin_B = (log10(stress_endurance) - log10(0.9*uts))/3
# basquin_A = stress_endurance/(10**(6*basquin_B))


def basquin_eq(N):
    return basquin_A*(N**basquin_B)

#Correct Mean Stress using Goodman's rule if Mean Stress is not 0

if R != -1: 
    stress_range_mean_zero = stress_range*(1 - (stress_mean/uts))

def mc_eq(N):
    #return mc_epsilon_fprime*(2*N)**mc_epslion_C
    return mc_epsilon_fprime*exp(-(stress_mean/uts)**(stress_yield/uts))*((2*N)**mc_B) + E*mc_epsilon_fprime**((2*N)**mc_epslion_C)




cycles = np.logspace(0, 20)


# Plotting
plt.figure(figsize=(10, 6))

# Plot both functions on the same plot
plt.plot(cycles, basquin_eq(cycles), label='High Cycle Equation')
plt.plot(cycles, mc_eq(cycles), label='Low Cycle Equation')
plt.axhline(y=55.9, color='red', linestyle='--', label='Endurance Limit')
plt.axhline(y=abs(stress_range_mean_zero/2), color='black', linestyle='--', label='Goodmans Stress')



# Set log scale for both axes
plt.xscale('log')
plt.yscale('log')

# Labeling and title
plt.xlabel('N (Number of Cycles)')
plt.ylabel('Stress Amplitude [Mpa]')
plt.title('Basquin and Modified Equations')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Display legend
plt.legend()

# Show the plot
plt.show()





