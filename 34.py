def countVowels(word):
    vowels = "АУЕЭОЯИЫЮуеэоаыяию"
    return sum(1 for char in word if char in vowels)

def check_rhythm(poem):
    phrases = poem.split()
    syllable_counts = [countVowels(phrase.replace("-", "")) for phrase in phrases]
    
    if len(set(syllable_counts)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)