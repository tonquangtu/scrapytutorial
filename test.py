list = ["anh tu", "em tung", "thuan cho", "trung cho"]

item = next((x for x in list if "thuanx" in x), None)

print(item)

# next(x for x in the_iterable if x > 3)