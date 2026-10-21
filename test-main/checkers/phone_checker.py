import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.db import get_connection

def check_phone():
    print("\n--- 📞 電話番号チェッカー ---")
    phone_input = input("調べたい電話番号を入力してください: ").strip()
    
    if not phone_input:
        print("⚠️ 電話番号が入力されていません。")
        return

    conn = get_connection()
    cursor = conn.cursor()
    
    # phone_scams テーブルを検索
    cursor.execute("SELECT title, description FROM phone_scams WHERE target_value = %s", (phone_input,))
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if result:
        print(f"\n🚨 【危険】この電話番号は過去の詐欺事例に登録されています！")
        print(f"タイトル: {result[0]}")
        print(f"詳細: {result[1]}")
    else:
        print(f"\n✅ 【安全】この電話番号はデータベースに見つかりませんでした。")

if __name__ == "__main__":
    check_phone()