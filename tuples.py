numbers = (1,2,3)

x,y,z = numbers
print(x)

# DIctionaries
# store key value pairs
customer={
    "name": "Peter",
    "age": 20,
    "is_single": True
}
print(customer.get("age"))

phone_number = input("Phone: ")
names = {
    "1": "One",
    "2": "two",
    "3": "three"
}
output = ""
for cha in phone_number:
    output += names.get(cha, "!") + " "
print(output)