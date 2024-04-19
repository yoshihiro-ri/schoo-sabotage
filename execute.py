import subprocess
import time

def run_auto_click():
    while True:
        try:
            # auto-click.pyを実行
            subprocess.run(["python3", "auto-click.py"])
        except Exception as e:
            print("エラーが発生しました。auto-click.pyを再実行します。")
            print("エラー内容:", str(e))
        time.sleep(1)  # 1秒待ってから再実行

if __name__ == "__main__":
    run_auto_click()