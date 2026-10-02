def main():

    print("----------------------------------------")
    print("Weight Update Using Gradient Descent")
    print("----------------------------------------")

    # Input
    x = 2

    # Initial weight
    weight = 0.5

    # Bias
    bias = 0.1

    # Target output
    target = 1

    # Learning rate
    learning_rate = 0.1

    #---------------------------------------
    # Step 1 : Calculate prediction
    #---------------------------------------

    print("Step 1 : Calculate prediction")

    prediction = (weight * x) + bias

    print("Prediction : ", prediction)

    #---------------------------------------
    # Step 2 : Calculate error
    #---------------------------------------

    print("Step 2 : Calculate error")

    error = target - prediction

    print("Error : ", error)

    #---------------------------------------
    # Step 3 : Calculate gradient
    #---------------------------------------

    print("Step 3 : Calculate gradient")

    gradient = error * x

    print("Gradient : ", gradient)

    #---------------------------------------
    # Step 4 : Update weight
    #---------------------------------------

    print("Step 4 : Update weight")

    old_weight = weight

    weight = weight + (learning_rate * gradient)

    print("Old Weight : ", old_weight)
    print("Updated Weight : ", weight)


if __name__ == "__main__":
    main()