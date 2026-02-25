import os
script_path="script.py"
if not os.path.exists(script_path):
        print(f"错误：脚本文件 {script_path} 不存在")
else:
    print(f"脚本文件 {script_path} 存在")
