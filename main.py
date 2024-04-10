# Check if a line is Empty in Python 

# ✅ check if a line is NOT empty
with open('example.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        if line.strip():
            print('The line is NOT empty ->', line)
        else:
            print('The line is empty')

print('------------------------------------------')

# ✅ check if a line is empty
with open('example.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        if line.strip() == "":
            print('The line is empty')
        else:
            print('The line is NOT empty', line)