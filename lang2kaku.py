def main(lang_name):
    if lang_name == "python":
        return ".py"
    elif lang_name == "java":
        return ".java"
    else:
        exit("lang2kaku.py: main: 未対応の言語です。")

def return_com(lang_name):
    if lang_name == "python":
        return "# "
    elif lang_name == "java":
        return "// "
    else:
        exit("lang2kaku.py: main: 未対応の言語です。")
