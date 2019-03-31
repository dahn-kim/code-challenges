def group_by_owners(files):

    my_dict = {}
    for key, value in files.items():
        if value not in my_dict:
            my_dict[value] = [key]
        else:
            my_dict[value].append(key)

    return my_dict


files = {'Code.py': 'Stan', 'Output.txt': 'Randy', 'Input.txt': 'Randy'}

print(group_by_owners(files))
