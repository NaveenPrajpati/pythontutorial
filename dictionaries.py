

a={
    "name":'naveen',
    "sum":3,"roll":34
}
print(a)
print(len(a))
print(a.items())
print(a.keys())
print(a.values())

a.update({"sum":4,"marks":55})
print(a)
print(a.get("name")) # give None
print(a["name"]) # give error
