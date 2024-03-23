def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    return {keys[i]: values[i] for i in range(len(keys))}

def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    return  {**d1, **d2}  # implement me

def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """

    return {lst[i]: d1 for i in range(len(lst))}

def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    #for i in range data dict if key is in keylist add to new dict

    #print(keylist)
    #for k in range(len(datadict)):

            #print(list(datadict.keys())[k])
    new_dict = {}
   # for i in range(len(datadict)):
    #    if list(datadict.keys())[i] in keylist:
     #       print(list(datadict.keys())[i],list(datadict.values())[i])

    return {list(datadict.keys())[i]: list(datadict.values())[i] for i in range(len(datadict)) if list(datadict.keys())[i] in keylist}


def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    pop_holder = {datadict.pop(keylist[i]) for i in range(len(keylist))}
    return datadict
def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    return key in datadict.keys() or key in datadict.values()

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    for i in range(len(ddd)):
        if list(ddd.values())[i] == min(ddd.values()):
            return list(ddd.keys())[i]
def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    for i in range(len(ddd)):
        if list(ddd.values())[i] == max(ddd.values()):
            return list(ddd.keys())[i]