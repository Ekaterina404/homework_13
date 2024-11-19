from nltk.corpus import words
import nltk

# Загрузка словаря NLTK
nltk.download('words')
word_list = set(words.words())

class CaesarsCipher:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
        self.alphabet_size = len(self.alphabet)

    def encrypt(self, message: str, key: int) -> str:
        return ''.join(self._shift_character(char, key) for char in message)

    def decrypt(self, message: str, key: int) -> str:
        return ''.join(self._shift_character(char, -key) for char in message)

    def _shift_character(self, char: str, shift: int) -> str:
        if char in self.alphabet:
            new_index = (self.alphabet.index(char) + shift) % self.alphabet_size
            return self.alphabet[new_index]
        return char


def find_key_with_nltk(cipher: CaesarsCipher, encrypted_message: str):
    """
    Подбирает ключ для расшифровки, проверяя слова с использованием NLTK.
    """
    for key in range(cipher.alphabet_size):
        decrypted_message = cipher.decrypt(encrypted_message, key)
        words = decrypted_message.split()
        for word in words:
            if word in word_list:  # Проверяем, существует ли слово
                print(f"Подобранный ключ: {key}")
                print(f"Расшифрованное сообщение: {decrypted_message}")
                return key

    print("Ключ не найден.")
    return None


if __name__ == "__main__":
    # Зашифрованное сообщение
    encrypted_message = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"

    # Создаем шифр
    cipher = CaesarsCipher()

    # Ищем ключ с использованием NLTK
    key = find_key_with_nltk(cipher, encrypted_message)

    if key is not None:
        print(f"Ключ найден: {key}")
    else:
        print("Не удалось найти ключ.")
