print("Enter the range (Natural numbers only)")
uper_limit=int(input("From: "))
lower_limit=int(input("To: "))
total_p_no = 0
total_c_no = 0
for r in range(uper_limit, lower_limit):
    if r < 1:
        print("Enter a valid range")
        break
    elif r==1:
        print("1 is called a unique number. Its nither a prime or composite number")
    for n in range(2, r):
        if (r%n)==0:
            print(r,"is composite")
            total_c_no += 1
            break
    else:
        print(r,"is prime")
        total_p_no += 1

print("Total prime numbers in given range is",total_p_no)
print("Total composite numbers in given range is",total_c_no)