import math

def main():

    print("----------------------------------------")
    print("Single Artificial Neuron")
    print("----------------------------------------")

    # Input values
    x1 = 2
    x2 = 3

    # Weights
    w1 = 0.4
    w2 = 0.6

    # Bias
    bias = 0.5

    # Step 1 : Calculate weighted sum
    print("Step 1 : Calculate weighted sum")

    z = (x1 * w1) + (x2 * w2) + bias

    print("Weighted sum : ", z)

    # Step 2 : Apply sigmoid activation function
    print("Step 2 : Apply sigmoid activation function")

    output = 1 / (1 + math.exp(-z))

    print("Sigmoid output : ", output)

    # Step 3 : Display final output
    print("Step 3 : Final output")

    print("Final output : ", output)

    # Step 4 : Check whether output is close to 0 or 1
    print("Step 4 : Prediction")

    if output >= 0.5:
        print("Output is close to 1")
    else:
        print("Output is close to 0")


if __name__ == "__main__":
    main()