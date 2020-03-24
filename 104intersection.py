#!/usr/bin/python3
import os
import math
import six
import sys

def h():
    print("USAGE\n    ./104intersection opt xp yp zp xv yv zv p\n\nDESCRIPTION\n    opt                surface option: 1 for a sphere, 2 for a cylinder, 3 for a cone\n    (xp, yp, zp)       coordinates of a point by which the light ray passes through\n    (xv, yv, zv)       coordinates of a vector parallel to the light ray\n    p                  parameter: radius of the sphere, radius of the cylinder, or\n                       angle formed by the cone and the Z-axis")

def sphere(vx, vy, vz, x, y, z, radius) :
    if (float(radius) <= 0) :
        print("WARNING: Use a radius sup as 0")
        sys.exit(84)
    a = float(vx) ** 2 + float(vy) ** 2 + float(vz) ** 2
    b = 2 * (float(vx) * float(x) + float(vy) * float(y) + float(vz) * float(z))
    c = float(x) ** 2 + float(y) ** 2 + float(z) ** 2 - int(radius) ** 2

    DELTA = b ** 2 - 4 * a * c

    print("Sphere of radius %s"%(radius))
    print("Line passing through the point (%s, %s, %s) and parallel to the vector (%s, %s, %s)"%(x, y, z, vx, vy, vz))
    if (DELTA < 0) :
        print("No intersection point.")
    elif (DELTA == 0):
        sol = -b / (2 * a)
        sol_x = float(vx) * sol + float(x)
        sol_y = float(vy) * sol + float(y)
        sol_z = float(vz) * sol + float(z)
        print("1 intersection point:")
        print("(%.3f, %.3f, %.3f)"%(sol_x, sol_y, sol_z))
    else :
        sol_1 = -(b - math.sqrt(DELTA)) / (2 * a)
        sol_2 = -(b + math.sqrt(DELTA)) / (2 * a)
        sol1_x = float(vx) * sol_1 + float(x)
        sol1_y = float(vy) * sol_1 + float(y)
        sol1_z = float(vz) * sol_1 + float(z)
        sol2_x = float(vx) * sol_2 + float(x)
        sol2_y = float(vy) * sol_2 + float(y)
        sol2_z = float(vz) * sol_2 + float(z)
        print("2 intersection points:")
        print("(%.3f, %.3f, %.3f)"%(sol1_x, sol1_y, sol1_z))
        print("(%.3f, %.3f, %.3f)"%(sol2_x, sol2_y, sol2_z))

def cylinder(vx, vy, vz, x, y, z, radius) :
    if (float(radius) <= 0) :
        print("WARNING: Use a radius sup as 0")
        sys.exit(84)
    a = float(vx) ** 2 + float(vy) ** 2
    b = 2 * (float(x) * float(vx) + float(y) * float(vy))
    c = float(x) ** 2 + float(y) ** 2 - int(radius) ** 2

    DELTA = b ** 2 - 4 * a * c

    print("Cylinder of radius %s"%(radius))
    print("Line passing through the point (%s, %s, %s) and parallel to the vector (%s, %s, %s)"%(x, y, z, vx, vy, vz))
    if (DELTA == float(0) and float(vx) == float(0) and float(vy) == float(0) and float(vz) == float(1)) :
        print("There is an infinite number of intersection points.")
        return()
    if (DELTA < 0) :
        print("No intersection point.")
    elif (DELTA == 0):
        sol = -b / (2 * a)
        sol_x = float(vx) * sol + float(x)
        sol_y = float(vy) * sol + float(y)
        sol_z = float(vz) * sol + float(z)
        print("1 intersection point:")
        print("(%.3f, %.3f, %.3f)"%(sol_x, sol_y, sol_z))
    else :
        sol_1 = -(b - math.sqrt(DELTA)) / (2 * a)
        sol_2 = -(b + math.sqrt(DELTA)) / (2 * a)
        sol1_x = float(vx) * sol_1 + float(x)
        sol1_y = float(vy) * sol_1 + float(y)
        sol1_z = float(vz) * sol_1 + float(z)
        sol2_x = float(vx) * sol_2 + float(x)
        sol2_y = float(vy) * sol_2 + float(y)
        sol2_z = float(vz) * sol_2 + float(z)
        print("2 intersection points:")
        print("(%.3f, %.3f, %.3f)"%(sol1_x, sol1_y, sol1_z))
        print("(%.3f, %.3f, %.3f)"%(sol2_x, sol2_y, sol2_z))

def cone(vx, vy, vz, x, y, z, angle) :
    if (float(angle) <= 0) :
        print("WARNING: Use a angle sup as 0")
        sys.exit(84)
    if (float(angle) >= float(90)) :
        print("WARNING: Use less than 90")
        sys.exit(84)
    alpha = float(angle) * math.pi
    alpha = alpha / 180
    a = float(vx) ** 2 + float(vy) ** 2 - float(vz) ** 2 * math.pow(math.tan(alpha), 2)
    b = 2 * (float(vx) * float(x) + float(vy) * float(y) - float(vz) * float(z) * math.pow(math.tan(alpha), 2))
    c = float(x) ** 2 + float(y) ** 2 - float(z) ** 2 * math.pow(math.tan(alpha), 2)

    DELTA = b ** 2 - 4 * a * c

    print("Cone with a %s degree angle"%(angle))
    print("Line passing through the point (%s, %s, %s) and parallel to the vector (%s, %s, %s)"%(x, y, z, vx, vy, vz))
    if (DELTA < 0) :
        print("No intersection point.")
    elif (DELTA == 0):
        sol = -b / (2 * a)
        sol_x = float(vx) * sol + float(x)
        sol_y = float(vy) * sol + float(y)
        sol_z = float(vz) * sol + float(z)
        print("1 intersection point:")
        print("(%.3f, %.3f, %.3f)"%(sol_x, sol_y, sol_z))
    else :
        sol_1 = -(b - math.sqrt(DELTA)) / (2 * a)
        sol_2 = -(b + math.sqrt(DELTA)) / (2 * a)
        sol1_x = float(vx) * sol_1 + float(x)
        sol1_y = float(vy) * sol_1 + float(y)
        sol1_z = float(vz) * sol_1 + float(z)
        sol2_x = float(vx) * sol_2 + float(x)
        sol2_y = float(vy) * sol_2 + float(y)
        sol2_z = float(vz) * sol_2 + float(z)
        print("2 intersection points:")
        print("(%.3f, %.3f, %.3f)"%(sol1_x, sol1_y, sol1_z))
        print("(%.3f, %.3f, %.3f)"%(sol2_x, sol2_y, sol2_z))

if __name__ == '__main__':
    a = len(sys.argv);
    if (a >= 10) :
        print("WARNING: Too many arguments")
        sys.exit(84)
    if (a < 2) or (a == 4):
        print("WARNING: Too few arguments")
        sys.exit(84);
    if (a == 2) :
        print(a);
        if (sys.argv[1] == "-h") :
            h()
        else :
            print("WARNING: Bad arguments")
            sys.exit(84)
    if (a > 4) :
        try :
            float(sys.argv[8])
            float(sys.argv[7])
            float(sys.argv[6])
            float(sys.argv[5])
            float(sys.argv[4])
            float(sys.argv[3])
            float(sys.argv[2])
        except :
            print("WARNING: ERROR Bad arguments")
            sys.exit(84)
        if (float(sys.argv[5]) == float(0) and float(sys.argv[6]) == float(0) and float(sys.argv[7]) == float(0)) :
            print("WARNING : Null Vector")
            sys.exit(84)
        if (sys.argv[1] == '1') :
            sphere(sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[8])
        elif (sys.argv[1] == '2') :
            cylinder(sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[8])
        elif (sys.argv[1] == '3') :
            cone(sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[8])
        elif (sys.argv[1] != 1 and sys.argv[1] != 2 and sys.argv[3] != 3) :
            print()
            sys.exit(84)