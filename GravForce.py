import sys

# Define a main() function that prints a little greeting.
def main():
  G = float(6.67e-11)
  print 'Input mass of object 1.'
  v = float(raw_input())
  mass1 = v
  print 'Enter velocity of object 1.'
  vel1 = float(raw_input())
  print 'Input mass of ojbect 2.'
  v = float(raw_input())
  mass2 = v
  print 'Enter velocity of object 2.'
  vel2 = float(raw_input())
  print 'Input distance between objects.'
  v = float(raw_input())
  radius = v
  print 'Enter time interval for analysis'
  timeint = float(raw_input())
  #print 'Enter a file name with a .txt extension.'
  #filename = raw_input()
  #print 'accel1, newvel1, disttrav1, accel2, newvel2, disttrav2, distance remaining'
  #file = open(filename, 'w')
  counter=0
  while (radius > 0):
    counter=counter+1
    initialtime=0
    Force=float((G*mass1*mass2)/radius**2)
    #print 'The force between these objects is',Force,'N'
    accel1=Force/mass1
    newvel1=vel1+(accel1*timeint)
    disttrav1=(vel1*timeint)+(0.5*accel1*timeint**2)
    accel2=Force/mass2
    newvel2=vel2+(accel2*timeint)
    disttrav2=(vel2*timeint)+(0.5*accel2*timeint**2)
    newradius=radius-(disttrav1+disttrav2)
    elapsedtime=initialtime+timeint*counter
    #print accel1,',',newvel1,',',disttrav1,',',accel2,',',newvel2,',',disttrav2,',',newradius,',',
    #file.write(newradius)
    #file.write(elapsedtime)
    radius=newradius
    vel1=newvel1
    vel2=newvel2
  print 'GREAT SCOTT!!! A collision!!!'
  print elapsedtime,' seconds from start to collision.'
  #file.close()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
