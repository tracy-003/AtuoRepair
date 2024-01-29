# https://atmarkit.itmedia.co.jp/ait/articles/2105/11/news015.html
from chardet import detect
import shutil
import codecs

import return_language

import codecs
import io

class Object:
    def __init__(self, input_path):
        self.input_path = input_path
        # バイナリーコード
        self.b_code = None
        # 文字コード
        self.code_char = ""
        # 更新後のテンポラリーファイル
        self.temp_path = "_temp." + return_language.kaku_from_Path(self.input_path)
        
    def update_file(self):
        # 文字コードを取得する。
        self.code_char = self.get_code_char()
        print(str(self.code_char) + "です。")
        # utf-8以外の場合、utf-8に変換する。
        if self.code_char != "utf-8":
            self.exchange_to_temp()
            self.copy_2_input()
            
        
            
        
    def get_code_char(self):
        # バイナリーファイルで読み込み
        with open(self.input_path, 'rb') as f:
            self.b_code = f.read()
        s = detect(self.b_code)['encoding']
        # print(self.input_path)        
        return detect(self.b_code)['encoding']
    
    def exchange_to_temp(self):
        # ファイルをコピーする。
        shutil.copyfile(self.input_path, self.temp_path)
        
    def copy_2_input(self):
        # ファイルをコピーする。
        print("self.code_char", self.code_char)
        # shutil.copyfile(self.temp_path, self.input_path)
        src_codec = codecs.lookup(self.code_char) # 変換前の文字コード
        dest_codec = codecs.lookup("utf_8") # 変換後の文字コード
        # ファイルオブジェクトを開く
        # https://dev.classmethod.jp/articles/python-encoding/
        # print("*" * 10, self.temp_path)
        # print("*" * 10, self.input_path)
        
        with open(self.temp_path, "rb") as src, open(self.input_path, "wb") as dest:
            
            # 変換ストリームを作成
            stream = codecs.StreamRecoder(
                src,
                dest_codec.encode, src_codec.decode,
                src_codec.streamreader, dest_codec.streamwriter,
            )
            reader = io.BufferedReader(stream)

            # 書き込み
            while True:
                data = reader.read1()
                if not data:
                    break
                dest.write(data)
                dest.flush()