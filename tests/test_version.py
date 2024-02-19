from clite.commands.version import run


class TestVersionCommand:
    def test_run(self):
        assert run() == 0
