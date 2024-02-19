from unittest import mock

from clite.commands.version import run


class TestVersionCommand:
    @mock.patch("clite.commands.version.__version__", "1.0-test")
    def test_run(self, capsys):
        ran = run()
        captured = capsys.readouterr()

        assert ran == 0
        assert captured.out == "version: 1.0-test\n"
