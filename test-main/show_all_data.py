import sys
import os

# パスを通す
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from database.db import get_connection

def display_all_records():
    conn = get_connection()
    cursor = conn.cursor()
    
    target_tables = [
        ("url_scams", "🔗 URL詐欺データ", "URL"),
        ("mail_scams", "✉️ メール詐欺データ", "メールアドレス"),
        ("phone_scams", "📞 電話番号詐欺データ", "電話番号"),
        ("ip_scams", "🌐 IPアドレス詐欺データ", "IPアドレス")
    ]
    
    print("\n" + "=" * 60)
    print("       データベース登録データ 全件一覧表示       ")
    print("=" * 60)
    
    for table_name, display_title, label in target_tables:
        print(f"\n■ {display_title} ({table_name})")
        print("-" * 60)
        
        cursor.execute(f"SELECT id, target_value, title, description FROM {table_name}")
        rows = cursor.fetchall()
        
        if not rows:
            print("  （登録されているデータはありません）")
        else:
            for row in rows:
                print(f"  [ID: {row[0]}]")
                print(f"    {label} : {row[1]}")
                print(f"    タイトル: {row[2]}")
                print(f"    説明    : {row[3]}")
                print("    " + "-" * 50)
                
    cursor.close()
    conn.close()
    print("\n" + "=" * 60)

if __name__ == "__main__":
    display_all_records()