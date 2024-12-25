hashmap = {
    101: 'John Doe',
    102: 'Jane Smith',
    103: 'Peter Johnson'
}

sorted_map = dict(sorted(hashmap.items(), key=lambda x: x[1]))
print(sorted_map)