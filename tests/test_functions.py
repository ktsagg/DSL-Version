from JoinLexico import format_accento_string, format_definizione_string


def test_format_accento_list():
    assert format_accento_string("[abc adss] ") == "/[i][c maroon]abc adss[/c][/i]/ "
    assert format_accento_string("[aaa bbb] ") == "/[i][c maroon]aaa bbb[/c][/i]/ "


def test_format_definizione_string():
    assert format_definizione_string("1.") == "[b][c brown]1.[/c][/b]"
    assert format_definizione_string("2.") == "[b][c brown]2.[/c][/b]"
    assert format_definizione_string("13.") == "[b][c brown]13.[/c][/b]"
    assert (
        format_definizione_string("Hello 4. test 12.")
        == "Hello [b][c brown]4.[/c][/b] test [b][c brown]12.[/c][/b]"
    )
