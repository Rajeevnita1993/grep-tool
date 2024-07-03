import subprocess

def test_simple_pattern():
    result = subprocess.run(['python', 'grep_tool/my_grep.py', 'A', 'rockbands.txt'], capture_output=True, text=True)

    assert "AC/DC" in result.stdout
    assert result.returncode == 0
