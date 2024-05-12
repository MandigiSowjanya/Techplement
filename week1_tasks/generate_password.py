import random
import string
import argparse

def gen_pwd(length, lowercase=False, uppercase=False, digits=False, special_characters=False):
    chars = ""
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if special_characters:
        chars += string.punctuation
    
    if not chars:
        raise ValueError("At least one character type must be selected")

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate random passwords")
    parser.add_argument("-l", "--length", type=int, required=True, help="Length of the password")
    parser.add_argument("-uc", "--uppercase", action="store_true", help="Include uppercase letters")
    parser.add_argument("-lc", "--lowercase", action="store_true", help="Include lowercase letters")
    parser.add_argument("-d", "--digits", action="store_true", help="Include digits")
    parser.add_argument("-sc", "--special-characters", action="store_true", help="Include special characters")
    
    args = parser.parse_args()

    try:
        password = gen_pwd(args.length, args.uppercase, args.lowercase, args.digits, args.special_characters)
        print("Password generated:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

