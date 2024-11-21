def calculate_velocity(distance,time):
    return distance/time

def  calculate_acceleration(velocity,time):
    return velocity/time

def area_of_circle(r):
    return float(2 *3.14* (r*r))

def gravitational_force(m1,m2,G,r):
    return float((m1*m2*G)/(r*r))

def work_done(time,force,distance):
    return float((force*distance)/(time))


options="""
1.Velocity
2.Acceleration
3.Area of a circle
4.Gravitational force
5.Work done"""

prompt='Among these options pick which you want to solve:'

print(options)
print(prompt)


question=int(input("Enter the number you want to solve here:"))

if question ==1:
    print('Input the parameters to solve for velocity below.')

    distance=float(input('Enter the value for distance here:'))
    time=int(input('Enter the value for time here:'))

    print(calculate_velocity(distance,time))

elif question==2:
    print('Enter the parameters to solve for Acceleration below:')

    velocity=float(input('Enter the value for velocity here:'))
    time=int(input('Enter the value for time here:'))

    print(calculate_acceleration(velocity,time))

elif question==3:
    print('Enter the parameters to solve for the area of a circle below.')

    radius=float(input('Enter the value for radius here:'))

    print(area_of_circle(radius))

elif question==4:
    print('Enter the parameters to solve for gravitational force below.')

    m1=int(input('Enter the value of the first mass here:'))
    m2=int(input('Enter the value of the second mass here:'))
    G=int(input('Enter the value for gravity here:'))
    r=float(input('Entern the value for radius here:'))

    print(gravitational_force(m1,m2,G,r))

elif question==5:
    print('Enter the parameters to solve for work done below.')

    time=int(input('Enter the value for time here:'))
    distance=float('Enter the value for distance here:')
    force=float(int('Enter the value for force here:'))

    print(work_done(time,force,distance))

else:
    print('Oops!!Please pick a correct option..')
