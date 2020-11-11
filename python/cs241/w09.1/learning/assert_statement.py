"""this code:
    if not <some_test>:
        raise AssertionError(<message>)
Is the same of:
    assert <some_test>, <message>"""

x = 5
y = 3
assert x < y, "x has to be smaller than y"
