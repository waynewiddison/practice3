"""
Learn about functions/definitions
Use the keyword: def <name>():
"""

def even_or_odd(number):
# Find if either even or odd: param number: input number
# : return: "even" on even numbers
# "odd" on odd numbers
# must have at least one statement,
# so we'll use the dummy statmement pass


     if number % 2 == 0:
        print ("even")
     else:
        print ("odd")

def main():
# call function
    print(__name__)
    even_or_odd(89)
    even_or_odd(22)

if __name__ == "__main__":
    main()
    exit(0)
