# Open the text file
f = open("paragraph_1.txt", "r")

# Read the file
content = f.read()

# Close the file
f.close()

# Split the text by spaces
words = content.split(" ")

# Print Paragraph Analysis
print("Paragraph Analysis")
print("-----------------")

# Find the length of the words and print it
word_count = len(words)
print("Approximate Word Count: " +str(word_count))

# Split the text by periods
sentence = content.split(".")

# Find the length of the sentences and print it
sentence_count = len(sentence)
print("Approximate Sentence Count: " + str(sentence_count))

# Take the word count and divide it by the sentence count
letter_count = len(content)/len(words)
print("Average Letter Count: " + str(letter_count))

# Take the number of words and divide it by the number of sentences
sentence_length = len(words)/len(sentence)
print("Average Sentence Length: " + str(sentence_length))
