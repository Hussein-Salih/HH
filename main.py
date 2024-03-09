def menu():
    print("1)problem 1")
    print("2)problem 2")
    print("3)problem 3")
    print("4)problem 4")
    print("5)problem 5")
    print("6)problem 6")
    print("0)exit")

menu()
chois = int(input("please choose one problem: "))
while chois != 0:
    if chois == 1:
        print('kosomak')
    elif chois == 2:
        # Get user input for a positive number
        num = int(input("enter a positive number"))


        # make a Function to check if a number is an Armstrong number
        def the_chek(number):

            len_number = len(str(number))  # Calculate the number of digits

            summ = 0  # Initialize a variable to store the sum

            orgnl_num = number  # Store the original number to compare later
            # Loop through each digit of the number
            while number > 0:
                dgt = number % 10  # Get the last digit of the number
                summ += dgt ** len_number  # Add the cube of the digit to the sum
                number = number // 10  # Remove the last digit by integer division
            # Check if the sum is equal to the original number
            if summ == orgnl_num:
                return True
            else:
                return False


        # call the function
        if the_chek(num):
            print("the number is armstrong")
        else:
            print("the number isn't armstrong")

    elif chois == 3:
        print("kosomak")

    elif chois == 4:
        # function to encrypt a massage using caesar cipher:
        def encrypted_version(text):
            new_wrd = ''  # Initialize an empty string to store the encrypted message

            # Iterate through each character in the input text
            for n in text:
                pos = ord(n)  # Get the ASCII code of the current character

                # Shift the ASCII code by 1 to encrypt the character
                new_chr = chr(pos + 1)

                # Append the encrypted character to the result string
                new_wrd += new_chr
            return new_wrd


        # get the input from the user
        txt = list(str(input("plaese enter the massage:")))

        # call the function
        t = encrypted_version(txt)
        print("the new massage is:", t)


    elif chois == 5:

        def check_lists(list1, list2):  # define the lists

            list1_sorted = sorted(list1)  # sort list1
            list2_sorted = sorted(list2)  # sort list2

            if list1_sorted == list2_sorted:  # check if the sorted lists equal each others
                return True
            else:
                return False


        list1 = list(input("enter a list"))  # enter the lists as integer
        list2 = list(input("enter another list"))

        if check_lists(list1, list2):  # print the answer depending on if the lists equal each other
            print("The lists are equal= True")
        else:
            print("The lists are equal= False")

    print("test")
    elif chois == 6:
        def print_factors(x):  # define (x) as the number to show the factors for
            print("The factors of", x, "are:")
            for i in range(1, x + 1):  # check the factors for the number
                if x % i == 0:
                    print(i)


        num = int(input("Enter the number"))  # enter the number to show the factors

        print_factors(num)  # show all the factors
    elif chois == 0:
        print("you exit from the program :)")
        break
    else:
        print("please choose a correct choise: ")
        menu()

    menu()
    chois = int(input("please choose one problem: "))