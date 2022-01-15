GlowScript 3.1 VPython
G=6.67e-11
RE=6.378e6
ME=5.972e24
mm=7.348e22
Rm=1.7371e6
rem=384.4e6

Earth = sphere(pos = vector(0,0,0), radius=5*RE, texture=textures.earth)
moon = sphere(pos=Earth.pos+vector(rem,0,0), radius=5*Rm, make_trail=True)
Earth.p = vector(0,0,0)
moon.p = vector(0,0,0)

t = 0
dt = 360

month=24*3600*28

while t<month:
  rate(1000)
  r = moon.pos - Earth.pos
  F = -G*ME*mm*norm(r)/mag(r)**2
  moon.p = moon.p + F*dt
  Earth.p = Earth.p -F*dt
  
  moon.pos = moon.pos + moon.p*dt/mm
  Earth.pos = Earth.pos + Earth.p*dt/ME
  
  t = t + dt
  
  
  

