from textblob import TextBlob

myList = ["Frst", "Secod"]

correct_list = []

for word in myList:

    correct_list.append(TextBlob(word))

for word in correct_list:

    print(word.correct())