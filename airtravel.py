"""
Learn about <insert topic here>
Use in conjunction with program airtravel
We created the class "flight"
Second, we will create class "Aircraft"
"""

class Flight:
    """
    A flight wih a particular passenger aircraft
    """

    def __init__(self, number):
        # Initializes Flight number
        # implementation details begin with an underscore '_'
        # Validate flight number: 5 characters long: Alpha Alpha Digit Digit Digit
        #    otherwise raise an exception
        # Test this condition
        """
        :param number: flight number
        :raise: ValueError (For invalid format)
        """
        if len(number) != 5:
           raise ValueError("Invalid flight number length".format(number))
        if not number[:2].isalpha():
            raise ValueError("No airline code {}".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code {}".format(number))
        if not number[2:].isdigit():
            raise ValueError("Invalid route code {}".format(number))
        self._number = number       # one underscore means I'm creating a private variable


    def number(self):
        """
        Flight number
        :return: flight number
        """
        return self._number[2:]

    def airline(self):
        return self._number[:2]


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    # right here, I could create functions for rows, seats, and num of seats per row

def main():
    """
    Test function
    :return:
    """
    pass



if __name__ == '__main__':
    main()
    exit(1)