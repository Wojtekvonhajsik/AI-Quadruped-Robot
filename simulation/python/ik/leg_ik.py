import math


def inverse_kinematics(x, y, L1, L2):

    #obliczanie długości odcinka miedzy stopą a początkiem nogi

    d = math.sqrt(x**2 + y**2) 

    #obliczanie kąta między segmentami nogi

    cos_theta2 = (
        d**2 - L1**2 - L2**2
    ) / (2 * L1 * L2)

    theta2 = math.acos(cos_theta2)

    
    #obliczanie kąta 1 segmentu wzgledem układu odniesienia

    alpha = math.atan2(y, x)

    beta = math.atan2(
        L2 * math.sin(theta2),
        L1 + L2 * math.cos(theta2)
    )

    theta1 = alpha - beta

    # przekształcenie z radianów na stopnie

    theta1 = math.degrees(theta1)
    theta2 = math.degrees(theta2)

    return theta1, theta2


theta1, theta2 = inverse_kinematics(6, 4, 8, 6)

print(theta1)
print(theta2)