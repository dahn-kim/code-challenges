def unique_names(names1, names2):
    # YOUR CODE GOES HERE
    list = names1 + names2
    return set(list)

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2))
