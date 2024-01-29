# Javaを中間言語(AST)にするプログラムのながれ
# (これが呼び出される)
from langs2ast.java import Java2ast00
import ast

# import astunparse

from base64 import encode
import json
import ast
import astunparse
import json
from logging import getLogger, config
# ディレクトリの移動
import os 

# ANTLRで構文解析をして木として返却
from langs2ast.java import J_ast_analyze_executor

def main(input_path, arg_logger):
    # このパスは絶対"Java"になる
    logger = arg_logger
    # 構文解析をして木として返却
    tree = make_tree(input_path)
    # print(tree)
    print(astunparse.unparse(tree))
    # exit()
    # その木をpythonのASTに変換
    return tree

def make_tree(input_path):
    # ここで、構文解析の結果を返却
    ast_bodys = J_ast_analyze_executor.main(input_path)
    # exit()
    # import MojiCode
    # obj = MojiCode.Object(input_path)
    # print(obj.get_code_char())
    # exit()
    # 以下動作しない？？
    # logger.info(ast_bodys)
    print(ast_bodys)
    if None in ast_bodys:
        # logger.error("astの中にNoneが含まれています。")
        # logger.error(ast_bodys)
        # エラー出力：("astの中にNoneが含まれています。")
        import sys
        print("astの中にNoneが含まれています。", sys.stderr)
        print("エラー", ast_bodys, sys.stderr)
        import Send_Mail
        Send_Mail.send_message("エラーのお知らせ", "asrの中にNoneが含まれています。\n" + str(ast_bodys))
        exit(1)
    
    
    # つくられたbody_astを全体のastに入れ込む
    ast_object = Java2ast00.main(ast_bodys)
    # 作られたastをファイルに表示
    txt = ast.dump(ast_object)
    f = open("ast00.txt", "w")
    f.write(txt)
    f.close()
    return ast_object

if __name__ == '__main__':
       
    path = os.getcwd()
    if path == 'C:\\Users\\user\\new_study':
        os.chdir('C:\\Users\\user\\new_study\\trans\\make_middle')
    
    # ロガーの設定
    with open('log_config.json', 'r') as f:
        log_conf = json.load(f)

    config.dictConfig(log_conf)

    logger = getLogger(__name__)
    logger.info("start")
    
    input_path = r"testJava00.java"
    
    obj = main(input_path, logger)
    print("$" * 300)
    print(obj)
    print(astunparse.unparse(obj))
    print(ast.dump(obj))
    logger.info("finish")