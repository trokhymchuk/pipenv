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


def test_input_pandas_no_extension():
    expected_pandas_dataframe = pandas.DataFrame({
        "a": ["1", "artem"],
        "b": ["2", "trokhymchuk"],
        "c": ["3", "artem"],
    })

    test_content = expected_pandas_dataframe.to_csv(index=False)

    with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8', delete=True) as tmp_file:
        tmp_file.write(test_content)
        tmp_file.flush()
        result = input_pandas(tmp_file.name)

    # print(expected_pandas_dataframe)
    # print("===")
    # print(result)
    pandas.testing.assert_frame_equal(result, expected_pandas_dataframe)
