from hello.message.greeting import get_greeting, get_greeting_with_name


if __name__ == "__main__":
    print(get_greeting())
    print(get_greeting_with_name(name="David"))
