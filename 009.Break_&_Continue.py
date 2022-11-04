#Break Statement
Anime = "One Piece"
for i in Anime:
    print(i)
    if i == "P":
        print("Found data.")
        break
print("You are out of the loop")

#Continue Statement
for i in Anime:
    print(i)
    if i == " ":
        print("Found data")
        continue
print("Out of the loop")
   
