import matplotlib.pyplot as plt
import os

OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_bar_chart(data, x_key, y_key):
    x = [item[x_key] for item in data]
    y = [item[y_key] for item in data]

    plt.figure()
    plt.bar(x, y)
    plt.xlabel(x_key)
    plt.ylabel(y_key)
    plt.title(f"{y_key} by {x_key}")

    file_path = os.path.join(OUTPUT_DIR, f"{x_key}_{y_key}.png")
    plt.savefig(file_path)
    plt.close()

    return file_path