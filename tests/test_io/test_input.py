from app.io.input import input_builtin, input_pandas
import tempfile
import pandas


def test_input_builtin():
    test_content = "Temporary file content for testing."

    with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8', delete=True) as tmp_file:
        tmp_file.write(test_content)
        tmp_file.flush()
        result = input_builtin(tmp_file.name)

    assert result == test_content
