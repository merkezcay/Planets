import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Güneş ve gezegenlerin özelliklerini tanımlayalım
class CelestialBody:
    def __init__(self, name, color, size, orbit_radius, orbit_speed):
        self.name = name
        self.color = color
        self.size = size
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.angle = 0

# Güneş sistemi objeleri oluşturalım
sun = CelestialBody('Sun', 'yellow', 8, 0, 0)
mercury = CelestialBody('Mercury', 'gray', 2, 50, 1.2)
venus = CelestialBody('Venus', 'orange', 3, 75, 0.9)
earth = CelestialBody('Earth', 'blue', 4, 100, 0.7)
mars = CelestialBody('Mars', 'red', 3.5, 150, 0.5)

bodies = [sun, mercury, venus, earth, mars]

# Animasyonun oluşturulması
fig, ax = plt.subplots()
ax.set_xlim(-200, 200)
ax.set_ylim(-200, 200)
ax.set_aspect('equal')

planet_circles = []
planet_dots = []

for body in bodies:
    circle = plt.Circle((0, 0), body.orbit_radius, color='gray', fill=False)
    planet_circles.append(ax.add_patch(circle))
    dot, = ax.plot([], [], 'o', color=body.color)
    planet_dots.append(dot)

def init():
    for dot in planet_dots:
        dot.set_data([], [])
    return planet_dots

def animate(frame):
    for i, body in enumerate(bodies):
        body.angle += body.orbit_speed
        x = body.orbit_radius * np.cos(np.radians(body.angle))
        y = body.orbit_radius * np.sin(np.radians(body.angle))
        planet_dots[i].set_data([x], [y])  # x ve y koordinatlarını listeye çevirerek set_data metoduna iletiyoruz
    return planet_dots

anim = FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)

plt.title('Solar System Animation')
plt.show()
