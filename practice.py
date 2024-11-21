values = [(3, 'b', "hello"), (2, 'a', "world"), (1, 'c', "ok")]
sorted_values = sorted(values, key=lambda x: x[1], reverse=True) 
print(list(sorted_values))