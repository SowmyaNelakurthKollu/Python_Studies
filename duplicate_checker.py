def duplicate_checker(dict_ex):
    
    only_values = list(dict_ex.values()) #this line stores the values in each key to a list

    if len(only_values) != len(set(only_values)): #here the list of values are converted to set data structure.
        return True


sample_dict = {
                "brand": "Ford",
                "model": "Mustang",
                "year": 1964,
                "years": 1964
}

if duplicate_checker(sample_dict):
    print("The sample dictionary contains duplicates")
else:
    print("The sample dictionary doesn't contain duplicates")
