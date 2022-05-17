inputvar1 = input("Please type an author: ")

booksdict = { "Margaret Atwood": ["The Handmaiden's Tale", "The Edible Woman", "Lady Oracle"] ,  "J.R.R. Tolkien": ["The hobbit", "Lord Of the Rings"], "Agatha Christie": ["Murder on the Orient Express", "Dial M for Murder", "Poitrot and the Big Mustache"] }
valuefromkeyvar = booksdict[inputvar1]
stingfromalistvar = ", ".join(sorted(valuefromkeyvar))
print(stingfromalistvar)