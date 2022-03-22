"""Print out all the melons in our inventory."""


from melons import melon_names, melon_prices, melon_seedlessness, all_melon_info 

#  I will pass the dictionary as an argument
def print_melon(all_melon_info):
    """Print each melon with corresponding attribute information."""

    for melon, attributes  in all_melon_info.items():
        print(melon)

        for attribute, value in attributes.items():
            print(f"{attribute}: {value}")

    
#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])
print_melon(all_melon_info)