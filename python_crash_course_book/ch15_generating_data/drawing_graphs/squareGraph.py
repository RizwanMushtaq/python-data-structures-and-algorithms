import matplotlib.pyplot as plt


def squareGraph() -> None:
    x_values = range(1, 1001)
    y_values = [x**2 for x in x_values]
    plt.style.use("Solarize_Light2")
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, linewidth=5)
    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("square of values", fontsize=14)
    plt.show()


if __name__ == "__main__":
    squareGraph()
