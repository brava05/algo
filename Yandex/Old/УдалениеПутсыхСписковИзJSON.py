import json
dict_counter, list_counter = 0, 0
def clean_struct(struct):
    global dict_counter, list_counter
    if isinstance(struct, dict):
        for key, value in struct.copy().items():
            cleaned_struct = clean_struct(value)
            if cleaned_struct is None:
                del struct[key]
            else:
                struct[key] = cleaned_struct
        if len(struct) == 0:
            dict_counter += 1
            return None
    if isinstance(struct, list):
        i = 0
        while i < len(struct):
            cleaned_struct = clean_struct(struct[i])
            if cleaned_struct is None:
                del struct[i]
            else:
                struct[i] = cleaned_struct
                i += 1
        if len(struct) == 0:
            list_counter += 1
            return None
    return struct
struct = json.loads(input())
clean_struct(struct)
print(dict_counter, list_counter)