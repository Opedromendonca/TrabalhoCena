import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')

house = patches.Rectangle((3, 2), 4, 4, edgecolor='black', facecolor='lightblue')
ax.add_patch(house)

roof = patches.Polygon([[2.5, 6], [5, 8], [7.5, 6]], edgecolor='black', facecolor='brown')
ax.add_patch(roof)

door = patches.Rectangle((4.5, 2), 1, 2, edgecolor='black', facecolor='saddlebrown')
ax.add_patch(door)

left_window = patches.Rectangle((3.5, 4), 1, 1, edgecolor='black', facecolor='white')
right_window = patches.Rectangle((5.5, 4), 1, 1, edgecolor='black', facecolor='white')
ax.add_patch(left_window)
ax.add_patch(right_window)

ax.axis('off')

plt.show()
