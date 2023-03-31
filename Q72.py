#Q72
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

def hash_spam(string):
    x = count_hashtag(string)
    if x >=4 :
        print("this tweet will be considered as a spam!")
    else:
        return None


print(count_hashtag("I have a three ###s"))
hash_spam("I have three ###s")
hash_spam("I have five #####s")
