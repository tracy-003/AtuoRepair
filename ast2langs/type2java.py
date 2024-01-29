def ex(type_python):
    if type_python == int:
        return "int"
    elif type_python == float:
        return "float"
    elif type_python == str:
        return "String"
    elif type_python == bool:
        return "boolean"
    else:
        print("未対応の型(int, floatなど)です。" + str(type_python))
        print("type2java.pyのex()を修正してください。")
        return None