THINGS = []


def setUpModule():
    THINGS.append(1)


def tearDownModule():
    while THINGS:
        THINGS.pop()


def test(p):
    assert THINGS, "setup didn't run I think"


test.paramList = (1,)  # type: ignore[attr-defined]
