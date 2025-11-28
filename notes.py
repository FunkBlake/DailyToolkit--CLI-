from datetime import datetime

def write_note():
    text = input("输入你的笔记：\n")
    filename = datetime.now().strftime("note_%Y%m%d.txt")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"已保存到 {filename}")
