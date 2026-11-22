import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/raw.csv")

fig, ax = plt.subplots(figsize=(5, 3.5))
ax.plot(df["x"], df["y"], "o")
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.tight_layout()
fig.savefig("figures/raw.png", dpi=150)
