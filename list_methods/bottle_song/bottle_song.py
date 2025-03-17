number_words = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
}

def recite(start, take=1):
    LINE_3 = "And if one green bottle should accidentally fall,"
    song = []
    for i in range(take):
        if start == 1:
            LINE_1_2 = "One green bottle hanging on the wall,"
            LINE4 = "There'll be no green bottles hanging on the wall."
        else:
            LINE_1_2 = f"{number_words[start].title()} green bottles hanging on the wall,"
            if start == 2:
                LINE4 = "There'll be one green bottle hanging on the wall."
            else:
                LINE4 = f"There'll be {number_words[start-1]} green bottles hanging on the wall."

        song.append(LINE_1_2)
        song.append(LINE_1_2)
        song.append(LINE_3)
        song.append(LINE4)
        song.append("")

        start -= 1

    return song[:-1]
