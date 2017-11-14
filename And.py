#declare awnser1 : string
#declare awnser2 : string
#output "Are you 18 or older [true/false]"
#input <-- awnser
print("Are you 18 or older [true/false]")
awnser1 = input()
print("Are you male [true/false]")
awnser2 = input()

if  awnser1 == "true" and awnser2 == "true":
    print("You can enter the matrix")
else:
    print("access denied")

