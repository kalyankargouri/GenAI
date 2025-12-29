sentence= input("enter the sentence:")
print((sentence))
print("Number of   sentence",len (sentence))


words=sentence.split()
print("Number of  words",len(words))

vowel="aeiouAEIOU"
vowel_count= 0
for cha in sentence:
    if cha in vowel:
        vowel_count+=1
print("count of vowel is:",vowel_count)


