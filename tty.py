import sys
import shlex

commands = [
    "login",
    "logout",
]

def process(text):
    re_text = shlex.split(text)
    if re_text[0] not in commands:
        print(f"Invalid arguments: {re_text[0]}")
    else:
        pass


def main():
    while True:
        try:
            text = input(">>> ")
            process(text)
        except BaseException as error:
            sys.exit(f"\nFailed due to {error.__class__.__name__}")

if __name__ == "__main__":
    main()