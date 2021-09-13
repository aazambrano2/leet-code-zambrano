def occur(s):
    if s == "":
        return 0
    if len(s) == 1 and s[0].lower() == "a":
        return 1
    first_letter = set()
    first_letter.add("a")
    first_letter.add("A")

    acc = 0
    for l in s:
        if l in first_letter:
            acc +=1
    return acc

print(occur("pablo had a job and was an alligator"))
print(occur("race a car"))




    