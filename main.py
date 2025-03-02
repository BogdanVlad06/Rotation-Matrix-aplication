import matplotlib.animation as animation 
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Arc
from matplotlib.offsetbox import AnchoredText

def rotation_matrix(angle = 45, convert2rad=True):
    if convert2rad:
        a_rad = np.deg2rad(angle)
    else:
        a_rad = angle
    a_sin = np.sin(a_rad)
    a_cos = np.cos(a_rad)
    A = np.array([[a_cos, -a_sin], 
                  [a_sin, a_cos]])
    return A

def update_vector(vector, nx, ny):
    vector.set_UVC(nx, ny)

    
def animate(frame, obj):
    global angle
    angle += 5
    nV = np.matmul(rotation_matrix(angle), V)
    update_vector(obj, nV[0], nV[1])
    return obj,
    

fig, (ax, ax1) = plt.subplots(1, 2 )

V = np.array([0.5,0])
angle = 0

vector = ax.quiver(1, 1, V[0], V[1], angles='xy', scale_units='xy', scale = 1)
anim = animation.FuncAnimation(fig, animate, frames=60, fargs=(vector, ), interval=25, blit=True)

# Axes settings for representation
ax.set_xlim([0, 2])
ax.set_ylim([0, 2])
ax.set_aspect('equal')

ax.set_title("Rotation of a vector (θ = 5°) each frame (60 fps)")
ax.grid()

# Ilustrative rotation
ax1.set_xlim([0, 1.5])
ax1.set_ylim([0, 1.5])
ax1.set_aspect('equal')

theta = 45; #45°
point = np.matmul(rotation_matrix(15), [1, 0])

ax1.quiver(0, 0, point[0], point[1], angles='xy', scale_units='xy', scale=1)
ax1.scatter(point[0], point[1], color = 'black', s=5, label=f'P({round(point[0], 2)}, {round(point[1], 2)})')
ax1.text(point[0] + 0.01, point[1] + 0.01, 'P(x,y)', fontsize=12)

rot_point = np.matmul(rotation_matrix(theta), point)

ax1.quiver(0, 0, rot_point[0], rot_point[1], angles='xy', scale_units='xy', scale=1, color='red')
ax1.scatter(rot_point[0], rot_point[1] , color = 'red', s=5, label=f'P\'({round(rot_point[0], 2)}, {round(rot_point[1], 2)})')
ax1.text(rot_point[0] + 0.01, rot_point[1] + 0.01, 'P\'(x\',y\')', fontsize=12)

ax1.text(0.2, 0.2, f'θ = {theta}°', color='blue', fontsize=12)
arc = Arc((0,0), 0.5, 0.5, theta1=15, theta2=60, color='blue')
ax1.add_patch(arc)

ax1.grid()
ax1.legend()
ax1.set_title("Rotation of a vector using rotation matrix with θ")

# anim.save('rotation_animation.mp4', writer='ffmpeg', fps=30)

plt.show()
