import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db import get_connection

def check_mail():
    print("\n--- ✉️ メールアドレスチェッカー ---")
    mail_input = input("調べたいメールアドレスを入力してください: ").strip()
    
    if not mail_input:
        print("⚠️ メールアドレスが入力されていません。")
        return

    conn = get_connection()
    cursor = conn.cursor()
    
    # mail_scams テーブルを検索
    cursor.execute("SELECT title, description FROM mail_scams WHERE target_value = %s", (mail_input,))
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if result:
        print(f"\n🚨 【危険】このメールアドレスは過去の詐欺事例に登録されています！")
        print(f"タイトル: {result[0]}")
        print(f"詳細: {result[1]}")
    else:
        print(f"\n✅ 【安全】このメールアドレスはデータベースに見つかりませんでした。")

if __name__ == "__main__":
    check_mail()