def recite(start_verse, end_verse):
    number_words = {
        1: ["first", "a Partridge in a Pear Tree."],
        2: ["second", "two Turtle Doves"],
        3: ["third", "three French Hens"],
        4: ["fourth", "four Calling Birds"],
        5: ["fifth", "five Gold Rings"],
        6: ["sixth", "six Geese-a-Laying"],
        7: ["seventh", "seven Swans-a-Swimming"],
        8: ["eighth", "eight Maids-a-Milking"],
        9: ["ninth", "nine Ladies Dancing"],
        10: ["tenth", "ten Lords-a-Leaping"],
        11: ["eleventh", "eleven Pipers Piping"],
        12: ["twelfth", "twelve Drummers Drumming"]
    }
    
    if start_verse != end_verse:
        verses = []
        for verse_num in range(start_verse, end_verse + 1):
            verses.append(single_verse(verse_num, number_words))
        return verses
    
    return [single_verse(start_verse, number_words)]


def single_verse(verse_num, number_words):
    verse = f"On the {number_words[verse_num][0]} day of Christmas my true love gave to me: "
    
    if verse_num == 1:
        verse += number_words[1][1]
        return verse
    
    for i in range(verse_num, 0, -1):
        if i == verse_num:
            verse += number_words[i][1] + ", "
        elif i == 1:
            verse += "and " + number_words[i][1]
        else:
            verse += number_words[i][1] + ", "
    
    return verse