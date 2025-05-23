
def word_in_file(word, filename, case_sensitive=False):
    try:
        with open(filename, 'r') as file:
            for line in file:
                file_word = line.strip()
                if not case_sensitive:
                    word = word.lower()
                    file_word = file_word.lower()
                if word == file_word:
                    return True
        return False
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return False


def word_has_character(word, character_list):
    return any(char in word for char in character_list)


def word_complexity(word):
    LOWER = "abcdefghijklmnopqrstuvwxyz"
    UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DIGITS = "0123456789"
    SPECIAL = "!@#$%^&*()_+-=[]{}|;:',.<>?/`~"
    
    complexity = 0
    
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    
    return complexity


def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, 'dictionary.txt', case_sensitive=False):
        print(f"'{password}' is a dictionary word and is not secure.")
        return 0
    
    if word_in_file(password, 'toppasswords.txt', case_sensitive=True):
        print(f"'{password}' is a commonly used password and is not secure.")
        return 0
    
    if len(password) < min_length:
        print(f"'{password}' is too short and is not secure.")
        return 1
    
    if len(password) >= strong_length:
        print(f"'{password}' is long, length trumps complexity this is a good password.")
        return 5
    
    complexity = word_complexity(password)
    strength = 1 + complexity
    print(f"Password strength is {strength} based on complexity.")
    return strength


def main():
    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        
        if password.lower() == 'q':
            print("Exiting password checker...")
            break
        
        strength = password_strength(password)
        print(f"Password strength score: {strength}")


if __name__ == "__main__":
    main()
