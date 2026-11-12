def christmas_tree(row=5, column=10):
    star = ""
    for i in range(0, row):
        min = (column//2) - i
        max = (column//2) + i
        for j in range(0, column):
            if min <= j <= max:
                star += "*"
            else:
                star += " "
        star += "\n"
    return star


print(christmas_tree(10, 20))
