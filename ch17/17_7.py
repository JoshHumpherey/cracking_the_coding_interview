# Cracking the Coding Interview: 17.7
# Written by Josh Humphrey

Names = {"John":15, "Jon":12, "Chris":13, "Kris":4, "Christopher":8}

def compute_name_frequency(Names):
    true_map = {}
    true_names = {"Jon":"John", "Johnny":"John", "John":"John", "Chris":"Chris", "Kris":"Chris", "Christopher":"Chris"}
    for name in Names:
        true_name = true_names[name]
        value = Names[name]
        if true_name not in true_map:
            true_map[true_name] = value
        else:
            true_map[true_name] += value
    print(true_map)

compute_name_frequency(Names)
