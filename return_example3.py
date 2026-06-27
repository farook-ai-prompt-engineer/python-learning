def accuracy(score):
    if score >=90:
        return "deploy model"
    else:
        return "improve model"

result = accuracy(85)

print(result)

