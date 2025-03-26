import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')

house = patches.Rectangle((3, 2), 4, 4, edgecolor='black', facecolor='lightblue')
ax.add_patch(house)

roof = patches.Polygon([[2.5, 7], [5, 9], [7.5, 7]], edgecolor='black', facecolor='brown')
ax.add_patch(roof)

door = patches.Rectangle((4.5, 2), 1, 2, edgecolor='black', facecolor='saddlebrown')
ax.add_patch(door)

left_window = patches.Rectangle((3.5, 4), 1, 1, edgecolor='black', facecolor='white')
right_window = patches.Rectangle((5.5, 4), 1, 1, edgecolor='black', facecolor='white')
ax.add_patch(left_window)
ax.add_patch(right_window)

def create_explosion(ax, num_squares):
    for _ in range(num_squares):

        x = random.uniform(3, 7)
        y = random.uniform(2, 6)
        size = random.uniform(0.1, 0.5)  
        angle = random.uniform(0, 360)   

        square = patches.Rectangle((x, y), size, size, angle=angle, edgecolor='black', facecolor='orange', alpha=0.7)
        ax.add_patch(square)

create_explosion(ax, 30)

explosion = patches.Circle((5, 4), 1, edgecolor='black', facecolor='red')
ax.add_patch(explosion)

ax.axis('off')

plt.show()
