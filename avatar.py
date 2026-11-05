# import matplotlib.pyplot as plt

# fig , ax  = plt.subplots(figsize = (5,5))
# fig.patch.set_facecolor("#1e3af5")
# ax.set_facecolor("#1e3af5")
# ax.text(0.5,0.5,"SR",fontsize = 100, color = "white",ha = "center",va = "center" , fontweight = "bold")
# ax.axis("off")
# plt.savefig("avatar.png",dpi= 100, facecolor = fig.get_facecolor())



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

fig, ax = plt.subplots(figsize=(5, 5))
fig.patch.set_facecolor("#0b0b1a")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# focus lines radiating from the center
for angle in np.linspace(0, 2 * np.pi, 60):
    x = [0.5 + 0.3 * np.cos(angle), 0.5 + 1.2 * np.cos(angle)]
    y = [0.5 + 0.3 * np.sin(angle), 0.5 + 1.2 * np.sin(angle)]
    ax.plot(x, y, color="#3d5afe", linewidth=1.5, alpha=0.5)

# slanted letters with a pink outline
text = ax.text(0.5, 0.5, "SR", fontsize=110, color="white",
               ha="center", va="center", fontweight="bold", style="italic")
text.set_path_effects([pe.withStroke(linewidth=10, foreground="#ff2d95")])

ax.axis("off")
plt.savefig("avatar.png", dpi=100, facecolor=fig.get_facecolor())