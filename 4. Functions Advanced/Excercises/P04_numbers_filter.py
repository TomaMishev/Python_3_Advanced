# Create a function called even_odd_filter() that can receive a different number of named arguments. The keys will be
# "even" and/or "odd", and the values will be a list of numbers. When the key is "odd", you should extract only the
# odd numbers from its list. When the key is "even", you should extract only the even numbers from its list. The
# function should return a dictionary sorted by the length of the lists in descending order. There will be no case of
# lists with the same length. Submit only your function in the judge system.

def even_odd_filter(**kwargs):
    final_dictionary = {}
    for key, el in kwargs.items():
        if key == "odd":
            final_dictionary[key] = [int(x) for x in el if x % 2 != 0]
        elif key == "even":
            final_dictionary[key] = [int(x) for x in el if x % 2 == 0]

    return dict(sorted(final_dictionary.items(), key=lambda x: x[-len(x)]))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
