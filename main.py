def print_horizontal_bar(value):
    num_visual_units = 60
    num_chars = int(value * num_visual_units)  # adjust 20 to change the length of the bar
    bar = '|' + '#' * num_chars + '-' * (num_visual_units - num_chars) + '|'
    print(bar)
print_horizontal_bar(.75)
