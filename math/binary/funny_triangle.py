from fractions import Fraction
import math

# Given side lengths of the triangle
a = 1.0 # side a
b = 1.2037037037037037  # side b
c = 1.023076923076923  # side c

# Check if the triangle inequality holds
if a + b > c and a + c > b and b + c > a:
    # Law of Cosines to find angle C (opposite side c)
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    if -1 <= cos_C <= 1:
        angle_C_rad = math.acos(cos_C)  # Convert to radians
        angle_C_deg = math.degrees(angle_C_rad)  # Convert radians to degrees

        # Law of Cosines to find angle A (opposite side a)
        cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
        angle_A_rad = math.acos(cos_A)
        angle_A_deg = math.degrees(angle_A_rad)

        # Law of Cosines to find angle B (opposite side b)
        cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
        angle_B_rad = math.acos(cos_B)
        angle_B_deg = math.degrees(angle_B_rad)

        # Output the angles
        print(f"Angle A: {angle_A_deg} degrees")
        print(f"Angle B: {angle_B_deg} degrees")
        print(f"Angle C: {angle_C_deg} degrees")
    else:
        print("Invalid cosine value, triangle cannot exist.")
else:
    print("The sides do not satisfy the triangle inequality. No valid triangle.")

"""

"""


# theta_deg = 90.000010925  # angle in degrees

# # Convert the angle to radians
# theta_rad = math.radians(theta_deg)

# # Apply the Law of Cosines to calculate the third side (c)
# c_squared = a**2 + b**2 - 2 * a * b * math.cos(theta_rad)
# c = math.sqrt(c_squared)

# # Output the third side
# print(f"The third side of the triangle is: {c}")