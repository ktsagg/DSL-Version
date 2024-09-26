from JoinLexico import color_numbers


def test_replace_numbers_with_div():
    assert color_numbers("1.") == "[b][c brown]1.[/c][/b]"
    assert color_numbers("2.") == "[b][c brown]2.[/c][/b]"
    assert color_numbers("3.") == "[b][c brown]3.[/c][/b]"
    print(color_numbers("Hello 4. test 12."))
    assert (
        color_numbers("Hello 4. test 12.")
        == "Hello [b][c brown]4.[/c][/b] test [b][c brown]12.[/c][/b]"
    )
