from collections import deque

def is_palindrome(s):
    char_queue = deque()
    
    # Враховувати що рядки повинні бути нечутливі до регістру та пробілів
    s = s.lower().replace(" ", "")
    
    for char in s:
        char_queue.append(char)
    
    # Обійдемо з двох сторін
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    
    return True

# Тест
input_strings = ["І розморозь зором зорі", "Три психи пили Пилипихи спирт", "око", "не падіндром"]
for string in input_strings:
    print(f"{string}: {is_palindrome(string)}")