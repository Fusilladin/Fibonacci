#FIBONACCI

try:
    nterms = int(float(input('How many Fibonacci numbers do you want to generate?  ')))
except ValueError as e1:
    pass

n1 = 0
n2 = 1
count = 0
try:
    nterms <= 0
except NameError as e2:
    print('Please type a number.')
else:
    if nterms <= 0:
        print('Please choose a positive number.')
    elif nterms == 1:
        print(n1)
    else:
        while count < nterms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1



# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
