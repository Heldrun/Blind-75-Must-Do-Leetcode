def max_area(height_list):
    # takes a list of integers representing peaks on a graph.
    # calculates the maximum volume of water which could be stored between these two peaks
    volume = 0
    hash_table = {index:height_list[index] for index in range(len(height_list))}
    for i in range(len(height_list)-1):
        for j in range(i+1, len(height_list)):
            width = j-i
            if hash_table[i] > hash_table[j]:
                height = hash_table[j]
            else:
                height = hash_table[i]
            if (width * height) > volume:
                volume = width * height
    return volume
