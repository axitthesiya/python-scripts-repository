def paragraph_checker(paragraph):
    paragraph_string = ' '.join(paragraph)

    print("🚀 Original Paragraph 🚀 :")
    print(paragraph_string)
    action = input("🟢 \n Do you want to update any word (U) or delete any word (D)? (U/D) 🟢 :").upper()

    if action == "U":
        word_to_update = input("🟡 Enter the word you want to update 🟡 :")
        if word_to_update not in paragraph_string.split():
            print("🔴 The word is not found in the original paragraph.🔴")
            return
        new_word = input("🟡 Enter the new word 🟡: ")
        paragraph_string = paragraph_string.replace(word_to_update, new_word)
        print("🚀\n Updated Paragraph 🚀 :")
    elif action == "D":
        word_to_delete = input("🟢 Enter the word you want to delete 🟢 : ")
        if word_to_delete not in paragraph_string.split():
            print("🔴 The word is not found in the original paragraph. 🔴")
            return
        paragraph_string = paragraph_string.replace(word_to_delete, "")
        print(" 🚀\n After Deleted  Word 🚀 ")
    else:
        print("🔴 Invalid choice! 🔴")
        return

    print(paragraph_string)


def main():
    print(" 🚀 Write About Your Self Note In This Paragraph.... 🚀 ")
    user_paragraph = input("🟢 Enter a paragraph 🟢 :")
    paragraph_data_structure = user_paragraph.split()
 
    try:
        paragraph_checker(paragraph_data_structure)
    except Exception as e:
        print(" 🔴Error 🔴 :", e)


if __name__ == "__main__":
    main()
