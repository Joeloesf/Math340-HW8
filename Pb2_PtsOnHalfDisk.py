import random
import math
import statistics


def F_S(s: float):
    return (1/math.pi) * math.acos(-s * math.sqrt(1/(1+s**2)))


def F_RandTHETA(r: float, theta: float):
    if (0 <= r <= 1) and (-math.pi/2 <= theta <= math.pi/2):
        return ((r**2)/math.pi) * (theta + math.pi/2)
    elif (0 <= r <= 1) and (theta >= math.pi/2):
        return r**2
    elif (r >= 1) and (-math.pi/2 <= theta <= math.pi/2):
        return ((1)/math.pi) * (theta + math.pi/2)
    elif (r >= 1) and (theta >= math.pi/2):
        return 1
    elif (r <= 0) or (theta <= -math.pi/2):
        return 0
    else:
        raise Exception("None of the conditions were true")
    

def F_R(r: float):
    if (r <= 0):
        return 0
    elif (0 <= r <= 1):
        return r**2
    elif (r >= 0):
        return 1
    else:
        raise Exception("None of the conditions were true")
    

def F_THETA(theta: float):
    if (theta <= -math.pi/2):
        return 0
    elif (-math.pi/2 <= theta <= math.pi/2):
        return (1/math.pi) * (theta + math.pi/2)
    elif (theta >= math.pi/2):
        return 1
    else:
        raise Exception("None of the conditions were true")
    

def F_THETA_sqrd(theta: float):
    if (theta <= 0):
        return 0
    elif (0 <= theta <= (math.pi/2)**2):
        return (2 * math.sqrt(theta))/math.pi
    elif (theta >= (math.pi/2)):
        return 1
    else:
        raise Exception("None of the conditions were true")


def F_Dn(d: float):
    if (d <= 0):
        return 0
    elif (0 <= d <= 1):
        return 1 - (1-d)**(2*n)
    elif (d >= 0):
        return 1
    else:
        raise Exception("None of the conditions were true")


if __name__ == "__main__" : 

    num_of_points = 10000
    test_s = 3
    test_r = 0.5
    test_theta = -0.5
    test_theta_sqrd = 0.4

    points = []

    while len(points) < num_of_points :
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if (x > 0) and (x**2 + y**2 < 1) :
            d = {
                "x": x, 
                "y": y,
                "s": y/x,
                "r": math.sqrt(x**2+y**2),
                "theta": math.atan(y/x)
            }
            points.append(d)

    s_count = 0
    rtheta_count = 0
    r_count = 0
    theta_count = 0
    theta_sqrd_count = 0

    for point in points :
        if (point["s"] <= test_s) :
            s_count += 1
        if (point["r"] <= test_r) and (point["theta"] <= test_theta) :
            rtheta_count += 1
        if (point["r"] <= test_r) :
            r_count += 1
        if (point["theta"] <= test_theta):
            theta_count += 1
        if (point["theta"]**2 <= test_theta_sqrd):
            theta_sqrd_count += 1

    n = 10
    num_samples = 100000
    test_Dn = 0.1
    Dn_count = 0
    Dn_list = []

    for _ in range(num_samples):
        sampled_points = [points[random.randint(0,num_of_points-1)] for _ in range(n)]
        
        Mn = 0
        for point in sampled_points:
            Ri = point["r"]
            if Ri > Mn:
                Mn = Ri
        Dn = 1 - Mn

        Dn_list.append(Dn)

        if (Dn <= test_Dn):
            Dn_count += 1


    empirical_Dn = Dn_count/num_samples
    theoretical_Dn = F_Dn(test_Dn)

    # print("empirical_Dn: " + str(empirical_Dn))
    # print("theoretical_Dn: " + str(theoretical_Dn))

    # empirical_mean_Dn = statistics.mean(Dn_list)
    # theoretical_exp_Dn = 1/(2*n + 1)
    # print("empirical_mean_Dn: " + str(empirical_mean_Dn))
    # print("theoretical_exp_Dn: " + str(theoretical_exp_Dn))

    empirical_stdev = statistics.stdev(Dn_list)
    theoretical_stdev = math.sqrt(n/((n+1)*(2*n + 1)**2))
    print("empirical_stdev: " + str(empirical_stdev))
    print("theoretical_stdev: " + str(theoretical_stdev))
