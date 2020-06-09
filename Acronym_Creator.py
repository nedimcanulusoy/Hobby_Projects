
original_text = input("Enter your sentence: ")
original_text = original_text.upper()
original_text_List = original_text.split()

for each in original_text_List:
    print(each[0], end='')
print()