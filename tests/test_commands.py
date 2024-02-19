from unittest import mock

from clite.commands.commands import all_commands, available_commands


class TestCommandsCommand:
    @mock.patch("clite.commands.commands.files")
    def test_all_commands(self, files_mocker):
        def mock_iterdir():
            yield from ["one.py", "two.py"]

        files_mocker.return_value.iterdir = mock_iterdir
        commands = [cmd for cmd in all_commands()]
        assert commands == ["one", "two"]

    def test_available_commands(self, mocker):
        mocker.patch(
            "clite.commands.commands.all_commands", return_value=iter(["one", "two"])
        )

        assert available_commands() == "available commands:\n\none\ntwo"
