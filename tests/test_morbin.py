import sys

from pathier import Pathier, Pathish

from morbin import Morbin, Output

root = Pathier(__file__).parent


class Python(Morbin):
    @property
    def program(self) -> str:
        return Pathier(sys.executable).stem

    def execute(self, file: str, *args: str) -> Output:
        return self.run(file, *args)

    def text(self, text: str) -> Output:
        return self.execute(str(root / "dummy.py"), "-t", text)


def assert_output(output: Output):
    assert output.return_code[0] == 0
    assert output.stdout.strip("\n") == "yeet"


def test_morbin():
    py = Python(capture_output=True)
    output = py.execute(str(root / "dummy.py"), "--text", "yeet")
    print(output)
    assert_output(output)
    output = py.text("yeet")
    assert_output(output)


def test__context_capture():
    py = Python()
    with py.capturing_output():
        output = py.text("yeet")
    assert_output(output)


def test__output_add():
    py = Python(capture_output=True)
    output = py.text("yeet") + py.text("yeet")
    assert output.return_code == [0, 0]
    assert output.stdout == "yeet\nyeet\n"
