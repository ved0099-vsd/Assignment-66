import math

def main():

    print("----------------------------------------")
    print("Loss Calculation")
    print("----------------------------------------")

    Actual = [1, 0, 1, 1]
    Predicted = [0.9, 0.2, 0.8, 0.7]

    #---------------------------------------
    # Mean Squared Error
    #---------------------------------------

    print("Mean Squared Error")

    MSE = 0

    for i in range(len(Actual)):

        Error = Actual[i] - Predicted[i]

        MSE = MSE + (Error * Error)

    MSE = MSE / len(Actual)

    print("MSE : ", MSE)

    #---------------------------------------
    # Binary Cross Entropy
    #---------------------------------------

    print("Binary Cross Entropy")

    BCE = 0

    for i in range(len(Actual)):

        BCE = BCE + (
            Actual[i] * math.log(Predicted[i]) +
            (1 - Actual[i]) * math.log(1 - Predicted[i])
        )

    BCE = -BCE / len(Actual)

    print("Binary Cross Entropy : ", BCE)

    #---------------------------------------
    # Explanation
    #---------------------------------------

    print("----------------------------------------")
    print("Explanation")
    print("----------------------------------------")

    print("MSE is generally used for Regression.")
    print("Binary Cross Entropy is generally used for Binary Classification.")


if __name__ == "__main__":
    main()