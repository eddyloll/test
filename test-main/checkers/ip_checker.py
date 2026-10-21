import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db import get_connection

def check_ip():
    print("\n--- 🌐 IPアドレスチェッカー ---")
    ip_input = input("調べたいIPアドレスを入力してください: ").strip()
    
    if not ip_input:
        print("⚠️ IPアドレスが入力されていません。")
        return

    conn = get_connection()
    cursor = conn.cursor()
    
    # ip_scams テーブルを検索
    cursor.execute("SELECT title, description FROM ip_scams WHERE target_value = %s", (ip_input,))
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if result:
        print(f"\n🚨 【危険】このIPアドレスは不審なアクセス元として登録されています！")
        print(f"タイトル: {result[0]}")
        print(f"詳細: {result[1]}")
    else:
        print(f"\n✅ 【安全】このIPアドレスはデータベースに見つかりませんでした。")

if __name__ == "__main__":
    check_ip()