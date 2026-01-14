item =  ['apple','orange','apple']
unique_item = set()
for i in item:
    if item  in unique_item:
        print("Duplicate: ",item)
        break
    unique_item.add(item)