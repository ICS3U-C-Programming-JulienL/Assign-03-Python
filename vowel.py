#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: November 6, 2023
# This program program shows whether a letter is a vowel or consonant


def main():
    # get alphabet guess
    alphabet_guess_string = input("How many letters are in the alphabet? ")

    try:
        # convert alphabet guess to an integer
        alphabet_guess_int = int(alphabet_guess_string)

        # if the user guessed 26
        if alphabet_guess_int == 26:
            print("Right! There are 26 letters in the alphabet!")
        else:
            print("Wrong! There are 26 letters in the alphabet!")

        # get alphabet character
        alphabet_character = input(
            "Chose a word, and pick a character out of it. Enter it into the program and I will see if it is a vowel or a consonant: "
        )
        alphabet_character_str_lower = str.lower(alphabet_character)

        # if alphabet character is a, e, i, o, or u, tell the user it is a vowel.
        if (
            alphabet_character == "a"
            or alphabet_character_str_lower == "e"
            or alphabet_character_str_lower == "i"
            or alphabet_character_str_lower == "o"
            or alphabet_character_str_lower == "u"
        ):
            print("{} is a vowel".format(alphabet_character))
        elif alphabet_character_str_lower == "y":
            # if the user enter y, ask how many other vowels are in their word
            y_consonant = input(
                (
                    "Y can be both. Are there are any other vowels in your word including y (yes/no)?"
                )
            )

            # if there is more than 1 vowel in their word, y is a consonant
            if y_consonant == "yes":
                print("{} is a consonant".format(alphabet_character))
            elif y_consonant == "no":
                # if there is 1 vowel in their word, y is a vowel
                print("{} is a vowel".format(alphabet_character))
            else:
                print("Please enter yes or no for this section of the program")
        else:
            # otherwise their letter is a vowel
            print("{} is a consonant".format(alphabet_character))

    except:
        # if the user didn't enter an integer, tell them to do so
        print(
            "{} is not an integer. Please enter a positive integer for your guess.".format(
                alphabet_guess_string
            )
        )


if __name__ == "__main__":
    main()
