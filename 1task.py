# always use a lower case lettes
def print_ascii_lowercase(input_str):
    for char in input_str:
        if char.islower():
            print(f"🚀   ASCII code of '{char}': {ord(char)} ")

def main():
    user_input = input("🚀 Enter any string 🟢 : ")
    print("ASCII codes of lowercase characters in the input:")
    print_ascii_lowercase(user_input)

if __name__ == "__main__":
    main()
    