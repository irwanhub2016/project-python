import datetime

x=datetime.datetime.now()
print(x)

fruits = ["anggur", "jambu", "melon", "apel"]
fruits[2]="jeruk"
print (fruits[2])

thistuple = ("apple", "banana", "cherry")
#thistuple[2]="cherry"
print(thistuple[2])

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = set(("apple", "banana", "cherry"))
thisset.remove("banana")
print(thisset)