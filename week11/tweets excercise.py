with open("week11/tweets-1.txt", "r", encoding='utf-8') as f:
    for line in f:
        # if line.startswith("@VirginAmerica "):
            line = line.replace("@VirginAmerica ", "").strip('\n')
            length = len(line)
            print(f"The sentence: \"{line}\" has {length} characters.")
        
