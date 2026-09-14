count = 1
total = 0

# BUG: missing colon at the end of the while statement caused a SyntaxError.
# Fixed by adding the colon.
while count <= 5:
    total = total + count
    # BUG: the loop condition was "count < 5", which stopped the loop after
    # count reached 5 (last addition was 4), so total came out as 10 instead
    # of 15. No error was raised, just a wrong result. Fixed by changing
    # the condition to "count <= 5" so 5 is included in the sum.
    count = count + 1

# BUG: tried to concatenate a string with an integer ("... " + total),
# which raised a TypeError. Fixed by converting total to a string with str().
print("Sum of 1 to 5 is: " + str(total))
