import mysql.connector

def get_connection():
    """MySQLデータベースに接続する関数"""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pa$$w0rd",  # 先ほど接続できたパスワードを入力してください
        database="my_app_db"               # 使用するデータベース名
    )

def create_table():
    """テーブルが存在しない場合は作成する"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            role VARCHAR(50)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def add_user():
    """新しいデータを追加（INSERT）する"""
    print("\n--- データの追加 ---")
    name = input("名前を入力してください: ").strip()
    role = input("役割・役職を入力してください (例: 開発者, デザイン): ").strip()

    if not name:
        print("⚠️ 名前は必須入力です。追加をキャンセルしました。")
        return

    conn = get_connection()
    cursor = conn.cursor()
    
    sql = "INSERT INTO users (name, role) VALUES (%s, %s)"
    cursor.execute(sql, (name, role))
    conn.commit()
    
    print(f"✅ 「{name}」を追加しました！（ID: {cursor.lastrowid}）")
    
    cursor.close()
    conn.close()

def show_users():
    """全データを取得・表示（SELECT）する"""
    print("\n--- データ一覧表示 ---")
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name, role FROM users")
    rows = cursor.fetchall()
    
    if not rows:
        print("登録されているデータはありません。")
    else:
        print(f"{'ID':<5} | {'名前':<15} | {'役割':<15}")
        print("-" * 40)
        for row in rows:
            user_id, name, role = row
            role_text = role if role else "（未設定）"
            print(f"{user_id:<5} | {name:<15} | {role_text:<15}")
    
    cursor.close()
    conn.close()

def main():
    # アプリ起動時にテーブルを確認・作成
    create_table()
    
    while True:
        print("\n=========================")
        print(" データベース操作メニュー ")
        print("=========================")
        print("1: データを見れる（一覧表示）")
        print("2: データを入力する（新規追加）")
        print("9: 終了")
        
        choice = input("番号を選択してください: ").strip()
        
        if choice == "1":
            show_users()
        elif choice == "2":
            add_user()
        elif choice == "9":
            print("\nアプリを終了します。お疲れ様でした！")
            break
        else:
            print("⚠️ 1, 2, 9 のいずれかの番号を入力してください。")

if __name__ == "__main__":
    main()