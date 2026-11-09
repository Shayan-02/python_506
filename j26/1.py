import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 21)
y = np.abs(x)

with plt.xkcd():
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(x, y, marker="D", linewidth=3, label="abs(x)")

    ax.set_title("Hand Drawn Chart")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.legend()
    ax.grid(True)

    plt.show()
