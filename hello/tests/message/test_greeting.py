from hello.message.greeting import get_greeting, get_greeting_with_name


def test_get_greeting():
    result = get_greeting()
    assert result == "Hello World!"


def test_get_greeting_with_name():
    result = get_greeting_with_name(name="David")
    assert result == "Hello David!"
