import logging

integer = "The number is 1"
string = "The number is"

try:
    number = int(integer)  # Здесь возникнет ValueError, если integer не является числом
    print(string + str(number))
except TypeError as t_err:
    logging.warning("Error - {}. You cannot add a string to an integer, without converting the integer to a string first".format(t_err))
except ValueError as v_err:
    logging.warning("Error - {}. Your message".format(v_err))


if __name__ == "__main__":
    main()
