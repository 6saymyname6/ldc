import os
import json


class Tools:

    @staticmethod
    def print(*args, **kwargs):
        file_path = None
        # 如果最后一个位置参数看起来像文件路径，提取它
        if len(args) >= 2 and isinstance(args[-1], str) and ('/' in args[-1] or '\\' in args[-1] or '.txt' in args[-1]):
            args_list = list(args)
            file_path = args_list.pop()
            args = tuple(args_list)

        msg = " ".join([str(arg) for arg in args])
        print(msg)

        if file_path:
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(str(msg) + "\n")

    @staticmethod
    def new_dir(file_path):
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        return file_path
