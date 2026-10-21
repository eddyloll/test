import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from database.db import get_connection

def add_single_scam():
    print("\n" + "="*45)
    print("    ソーシャルエンジニアリング データベース登録ツール    ")
    print("="*45)
    print("1. URL詐欺データ (url_scams)")
    print("2. メール詐欺データ (mail_scams)")
    print("3. 電話番号詐欺データ (phone_scams)")
    print("4. IPアドレス詐欺データ (ip_scams)")
    print("0. 終了する")
    
    choice = input("\n登録したいデータの種類を選んでください (1-4): ").strip()
    
    if choice == '0':
        print("終了します。")
        return
    
    # 選択に応じたテーブル名と項目の日本語設定
    table_map = {
        '1': ("url_scams", "URL"),
        '2': ("mail_scams", "メールアドレス"),
        '3': ("phone_scams", "電話番号"),
        '4': ("ip_scams", "IPアドレス")
    }
    
    if choice not in table_map:
        print("⚠️ 無効な選択です。1〜4の番号を入力してください。")
        return
        
    table_name, target_label = table_map[choice]
    
    print(f"\n--- 【{target_label}】の新規データを入力 ---")
    target_value = input(f"対象の{target_label}を入力 (例: http://...): ").strip()
    title = input("タイトル（例: 〇〇偽サイト）を入力: ").strip()
    description = input("詳細説明を入力: ").strip()
    
    if not target_value or not title:
        print("⚠️ 「対象の値」と「タイトル」は必須です。登録をキャンセルしました。")
        return

    # データベースに登録
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        sql = f"INSERT INTO {table_name} (target_value, title, description) VALUES (%s, %s, %s)"
        cursor.execute(sql, (target_value, title, description))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print(f"\n✅ 【{table_name}】に新しいデータを登録しました！")
        
    except Exception as e:
        print(f"\n❌ エラーが発生しました: {e}")

if __name__ == "__main__":
    add_single_scam()