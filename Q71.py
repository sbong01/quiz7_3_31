#Q71
#saerin bong

def count_hashtag(string):
    index = 0
    total = 0
    while index < len(string):
        if string[index:index + 1] == "#":
            index += 1
            total += 1
        else:
            index += 1
    return total

print(count_hashtag("I have three ###s"))
