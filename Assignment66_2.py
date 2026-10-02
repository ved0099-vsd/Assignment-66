import numpy as np
import matplotlib.pyplot as plt

def main():

    print("----------------------------------------")
    print("Activation Functions")
    print("----------------------------------------")

    # Input values from -10 to 10
    x = np.linspace(-10, 10, 100)

    # Sigmoid
    sigmoid = 1 / (1 + np.exp(-x))

    # ReLU
    relu = np.maximum(0, x)

    # Tanh
    tanh = np.tanh(x)

    # Plot Sigmoid
    plt.plot(x, sigmoid)
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.title("Sigmoid Activation Function")
    plt.grid()
    plt.show()

    # Plot ReLU
    plt.plot(x, relu)
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.title("ReLU Activation Function")
    plt.grid()
    plt.show()

    # Plot Tanh
    plt.plot(x, tanh)
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.title("Tanh Activation Function")
    plt.grid()
    plt.show()

    print("Sigmoid : Output is between 0 and 1")
    print("ReLU : Negative values become 0")
    print("Tanh : Output is between -1 and 1")


if __name__ == "__main__":
    main()