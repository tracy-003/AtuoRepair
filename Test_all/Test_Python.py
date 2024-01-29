import sys
import subprocess

def test(output_Path, test_in, test_out):
    try:
        ans = subprocess.run(
            ['python', output_Path]
            # ['python', 'PY01\\ou.py']
            , input = str(test_in) + "\n"
            , encoding="utf-8"
            , capture_output = True
            , text = True # inputの確認
            , timeout=5
        )
    except subprocess.TimeoutExpired:
        # print error
        print("Timeout", file=sys.stderr)
        # exit()
        return False

    return str(ans.stdout) == str(test_out)