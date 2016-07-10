from visual import *

scaleFactor = 1200 #make the planets visible
dt = 60*60 #delta time
G = 6.67E-11#gravitational constant
force = vector(0.,0.,0.)
color.brown = (0.46,0.28,0.10)
#using standard SI units

sun = sphere()#create sun
sun.radius = 6.955E8*scaleFactor**(4./9.)    #add radius to sun
sun.mass = 1.98892E30   #add mass to sun
sun.pos = (0.,0.,0.)    #position the sun
sun.vel = vector(0.,0.,0.)  #add the velocity to sun
sun.color = color.yellow    #add colour to sun
sun.material = materials.emissive   #make sun see through
sun.light = local_light(pos = sun.pos, color = sun.color)   #add light to the sun
sun.force = vector(0.,0.,0,)

earth = sphere(make_trail = True, retain = 10000)#create earth
earth.radius = 6.371E6*scaleFactor #add radius to earth
earth.mass = 5.972E24   #add mass to earth 
earth.pos = (1.52098E11,0.,0.)  #give the earth a position
earth.vel = vector(0.,29283.9,0.)    #give the earth a velocity
earth.material = materials.earth    #give the earth texture
earth.force = vector(0.,0.,0,)

mars = sphere(make_trail = True, retain = 10000)#create mars
mars.radius = 3.39E6*scaleFactor #add radius to mars
mars.mass = 6.39E23   #add mass to mars 
mars.pos = (2.49230053E11,0.,0.)  #give mars a position
mars.vel = vector(0.,24130.833,0.)    #give mars a velocity
mars.color = color.red    #give mars color
mars.force = vector(0.,0.,0,)

mercury = sphere(make_trail = True, retain = 10000)#create mercury
mercury.radius = 2.4397E6 *scaleFactor #add radius to mars
mercury.mass = 3.3011E23   #add mass to mercury 
mercury.pos = (6.988169E10,0.,0.)  #give mercury a position
mercury.vel = vector(0.,47362,0.)    #give mercury a velocity
mercury.color = color.orange   #give mercury color
mercury.force = vector(0.,0.,0,)

venus = sphere(make_trail = True, retain = 10000)#create venus
venus.radius = 6.0518E6 *scaleFactor #add radius to venus in metres
venus.mass = 4.8765E24   #add mass to venus in kg
venus.pos = (1.08939000E11,0.,0.)  #give venus a position at aphelion
venus.vel = vector(0.,35020.,0.)    #give venus a velocity
venus.color = color.green   #give venus color
venus.force = vector(0.,0.,0,)

jupiter = sphere(make_trail = True, retain = 80000)#create jupiter
jupiter.radius = 6.9911E7 *scaleFactor #add radius to jupiter in metres
jupiter.mass = 1.8986E27   #add mass to jupiter in kg
jupiter.pos = (8.1604442E11,0.,0.)  #give jupiter a position at aphelion
jupiter.vel = vector(0.,1.307E4,0.)    #give jupiter a velocity
jupiter.color = color.red   #give jupiter color
jupiter.force = vector(0.,0.,0,)

saturn = sphere(make_trail = True, retain = 80000)#create saturn
saturn.radius = 5.8232E7 *scaleFactor #add radius to saturn in metres
saturn.mass = 5.6836E26   #add mass to saturn in kg
saturn.pos = (1.508844E12,0.,0.)  #give saturn a position at aphelion
saturn.vel = vector(0.,9.69E3,0.)    #give saturn a velocity
saturn.color = color.brown   #give saturn color
saturn.force = vector(0.,0.,0,)

uranus = sphere(make_trail = True, retain = 80000)#create uranus
uranus.radius = 2.5362E7 *scaleFactor #add radius to uranus in metres
uranus.mass = 8.6810E25   #add mass to uranus in kg
uranus.pos = (3.00841E12,0.,0.)  #give uranus a position at aphelion
uranus.vel = vector(0.,6.8E3,0.)    #give uranus a velocity
uranus.color = color.cyan   #give uranus color
uranus.force = vector(0.,0.,0,)

neptune = sphere(make_trail = True, retain = 80000)#create neptune
neptune.radius = 2.4622E7 *scaleFactor #add radius to neptune in metres
neptune.mass = 1.0243E26   #add mass to neptune in kg
neptune.pos = (4.5373E12,0.,0.)  #give neptune a position at aphelion
neptune.vel = vector(0.,5.43E3,0.)    #give neptune a velocity
neptune.color = color.blue   #give neptune color
neptune.force = vector(0.,0.,0,)

bodies = [sun,earth,mars,mercury,venus,jupiter,saturn,uranus,neptune]   #list of used planets
while True:
    rate(240)
    for bOne in range(len(bodies)-1):
        for bTwo in range(bOne+1, len(bodies)):
            dist = bodies[bTwo].pos-bodies[bOne].pos
            force = G*bodies[bOne].mass*bodies[bTwo].mass*dist/(mag(dist))**3
            bodies[bOne].force+=force
            bodies[bTwo].force-=force
    for body in bodies:
        body.vel += body.force*dt/body.mass
        body.pos += body.vel*dt
        body.force= vector(0.,0.,0.)

        
