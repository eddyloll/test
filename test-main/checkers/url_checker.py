import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db import get_connection

def check_url():
    print("\n--- 🔗 URLチェッカー ---")
    url_input = input("調べたいURLを入力してください: ").strip()
    
    if not url_input:
        print("⚠️ URLが入力されていません。")
        return

    conn = get_connection()
    cursor = conn.cursor()
    
    # url_scams テーブルを対象にし、プレースホルダーを %s に変更
    cursor.execute("SELECT title, description FROM url_scams WHERE target_value = %s", (url_input,))
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if result:
        print(f"\n🚨 【危険】このURLは過去の詐欺事例に登録されています！")
        print(f"タイトル: {result[0]}")
        print(f"詳細: {result[1]}")
    else:
        print(f"\n✅ 【安全】このURLはデータベースに見つかりませんでした。")

if __name__ == "__main__":
    check_url()