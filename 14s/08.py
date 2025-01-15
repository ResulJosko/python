a = {"kitap" : "book",
"bilim" : "knowledge",
"kompyuter" : "computer"}

a["talyp"] = "student"
print(a)

a = {"kitap" : "book",
"bilim" : "knowledge",
"kompyuter" : "computer"}

a.setdefault("talyp", "student")
print(a)