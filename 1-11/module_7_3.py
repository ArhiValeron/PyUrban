class WordsFinder():
    """
    Класс, который создаёт словарь следующего вида:
    {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
    Содержит метод get_all_words(), который возвращает словарь следующего вида:
    {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
    Содержит метод find(), который возвращает словарь, где ключ - название файла, значение - позиция первого
    слова в списке слов этого файла.
    Содержит метод count(), который возвращает словарь, где ключ - название файла, значение - количество слова
    word в списке слов этого файла.
    """
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = self.get_all_words()

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                all_words_in_one_file = []
                for line in file:
                    line = line.lower().replace(',', '').replace('.', '').replace('=', '').replace('!', '').replace('?', '').replace(';', '').replace(':', '').replace(' - ', ' ')
                    words = line.split()
                    all_words_in_one_file = all_words_in_one_file + words
                all_words[name] = all_words_in_one_file
        return all_words

    def find(self, word_):
        word = word_.lower()
        answer = {}
        for file_name, words in self.all_words.items():
            if word in words:
                answer.update({file_name:words.index(word) + 1})
        return answer

    def count(self, word_):
        word = word_.lower()
        answer = {}
        for file_name, words in self.all_words.items():
            count = words.count(word)
            if count > 0:
                answer[file_name] = count
        return answer





####################################################################################################################
finder2 = WordsFinder('../products.txt')
print(finder2.get_all_words())
print(finder2.find('Groceries'))
print(finder2.count('PoTato'))