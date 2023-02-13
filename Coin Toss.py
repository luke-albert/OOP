# i am inporting the name of the file and not the class(the name of the class is coin)
import CoinClass as c


# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = (
        c.Coin()
    )  # this creates an instance called 'my_coin' of the class 'Coin()'

    # Display the side of the coin that is facing up.
    # notice you do not have to supply the argument/parameter; make sure you use the variable and not c.Coin()
    print("This side is up:", my_coin.get_sideup())

    # Toss the coin.
    print("I am going to toss the coin ten times:")
    for count in range(10):
        my_coin.toss()
        my_coin.__sideup = (
            "Heads"  # this overides what is happening with the toss method
        )

        # Display the side of the coin that is facing up.
        print("This side is up:", my_coin.get_sideup())


# Call the main function.
main()


# this is the file that we will actually run
