class WordCounter:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        words = self.text.split()
        counts = {}
        for word in words:
            cleaned = word.lower().strip(",.!?")
            counts[cleaned] = counts.get(cleaned, 0) + 1
        return counts
