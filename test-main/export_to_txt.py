import os
from database.db import get_connection

def export_db_to_txt():
    # 書き出すテキストファイルのパス
    output_filename = "database_dump.txt"
    
    conn = get_connection()
    cursor = conn.cursor()
    
    tables = [
        ("url_scams", "🔗 URL詐欺データ"),
        ("mail_scams", "✉️ メール詐欺データ"),
        ("phone_scams", "📞 電話番号詐欺データ"),
        ("ip_scams", "🌐 IPアドレス詐欺データ")
    ]
    
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("=========================================\n")
        f.write("    ソーシャルエンジニアリング データベース一覧    \n")
        f.write("=========================================\n\n")
        
        for table_name, display_name in tables:
            f.write(f"-----------------------------------------\n")
            f.write(f"■ {display_name} ({table_name})\n")
            f.write(f"-----------------------------------------\n")
            
            # テーブルの全データを取得
            cursor.execute(f"SELECT id, target_value, title, description FROM {table_name}")
            rows = cursor.fetchall()
            
            if not rows:
                f.write("（データなし）\n\n")
            else:
                for row in rows:
                    f.write(f"ID          : {row[0]}\n")
                    f.write(f"対象の値    : {row[1]}\n")
                    f.write(f"タイトル    : {row[2]}\n")
                    f.write(f"詳細説明    : {row[3]}\n")
                    f.write("-" * 30 + "\n")
                f.write("\n")
                
    cursor.close()
    conn.close()
    
    print(f"✅ データベースの中身を '{output_filename}' に出力しました！")

if __name__ == "__main__":
    export_db_to_txt()