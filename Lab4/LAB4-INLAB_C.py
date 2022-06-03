def reverse(i):
    if i == "":
        return i
    else:
        return reverse(i[1:]) + i[0]


i = input("Enter a String to reverse:")
print(reverse(i))
