count = 0
total_length = 0
with open("week11/tweets-1.txt", "r", encoding='utf-8') as f:
    for line in f:
        # if line.startswith("@VirginAmerica "):
            line = line.replace("@VirginAmerica ", "").strip('\n')
            length = len(line)
            print(f"The sentence: \"{line}\" has {length} characters.")
            total_length += length
            count += 1
print(f"Total number of tweets: {count}, and the average length of the tweets is {total_length/count:.2f} characters.")