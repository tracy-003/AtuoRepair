# それぞれに振り分ける
from langs2ast.java import Java2ast
def main(input_path,logger, language_type):
    if language_type == "java":
        tree_body = Java2ast.main(input_path, logger)
        return tree_body
    

    else:
        logger.error("この言語は対応していません")
        exit(1)