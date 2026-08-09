firstname = input("enter your firstname: ")
lastname = input("enter your lastname: ")
fullname = firstname + " " + lastname
age = int(input("sen khod ra vared konid: "))

print("and your age is", age, "years old.")

# print
print("your firstname is", firstname, "\nyour lastname is", lastname, "\nyour fullname is", firstname, lastname, "your fullname is", fullname)

print("-"*40)
# f-string
print(f"your firstname is {firstname} \nyour lastname is {lastname} \nyour fullname is {firstname} {lastname}")

print("="*40)
# format
print("your firstname is {} \nyour lastname is {} \nyour fullname is {} {}".format(firstname, lastname, firstname, lastname))