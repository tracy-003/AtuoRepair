# この関数を実行します。
# コマンド
import logging.config
from langs2ast.java.ast_Java.ast_processor import AstProcessor
from langs2ast.java.ast_Java.basic_info_listener import BasicInfoListener

from anytree import Node, RenderTree # 木構造

import os

def main(target_file_path):
    # 追加
    # パスからファイル名を取得(rootにする)
    # https://note.nkmk.me/python-os-basename-dirname-split-splitext/
    # print(basename_without_ext)
    basename_without_ext = os.path.splitext(os.path.basename(target_file_path))[0]
    print(basename_without_ext)

    # ★ポイント１
    proc = AstProcessor(logging, BasicInfoListener(basename_without_ext))
    # print("proc", proc)
    ast_listener = proc.execute(target_file_path)
    
    # 以下動作しない？？
    print("ast_info", ast_listener.java_ast_body)
    for pre, fill, node in RenderTree(ast_listener.root):
        print("%s%s" % (pre, node.name))
    return ast_listener.java_ast_body

if __name__ == '__main__':
    #logging_setting_path = '../resources/logging/utiltools_log.conf'
    #logging.config.fileConfig(logging_setting_path)
    logger = logging.getLogger(__file__)

    # target_file_path = '../tar/test.java'
    target_file_path = 'C:\\temp\\sample\\src\\tar\\test.java'

    main(target_file_path)
    
    
    