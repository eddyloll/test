import mysql.connector

# 設定情報
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "Pa$$w0rd"  # ご自身のMySQLパスワードを設定してください
DB_NAME = "my_app_db"

def get_connection(use_db=True):
    """MySQLデータベースへの接続を取得する関数"""
    if use_db:
        return mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
    else:
        return mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS
        )

def init_db():
    """データベースと4つの専用テーブルを完全に初期化（再作成）する"""
    print("🔄 データベースの完全初期化処理を開始します...")
    
    # 1. データベース自体の存在確認と作成
    temp_conn = get_connection(use_db=False)
    temp_cursor = temp_conn.cursor()
    temp_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    temp_cursor.close()
    temp_conn.close()

    # 2. 対象データベースに接続して既存テーブルを一度削除してから再作成
    conn = get_connection(use_db=True)
    cursor = conn.cursor()

    # 安全のため既存のテーブルをすべて削除（リセット）
    cursor.execute("DROP TABLE IF EXISTS url_scams;")
    cursor.execute("DROP TABLE IF EXISTS mail_scams;")
    cursor.execute("DROP TABLE IF EXISTS phone_scams;")
    cursor.execute("DROP TABLE IF EXISTS ip_scams;")

    # 4つのテーブルを新しく作成
    cursor.execute("""
        CREATE TABLE url_scams (
            id INT AUTO_INCREMENT PRIMARY KEY,
            target_value VARCHAR(255) NOT NULL,
            title VARCHAR(255) NOT NULL,
            description TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE mail_scams (
            id INT AUTO_INCREMENT PRIMARY KEY,
            target_value VARCHAR(255) NOT NULL,
            title VARCHAR(255) NOT NULL,
            description TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE phone_scams (
            id INT AUTO_INCREMENT PRIMARY KEY,
            target_value VARCHAR(255) NOT NULL,
            title VARCHAR(255) NOT NULL,
            description TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE ip_scams (
            id INT AUTO_INCREMENT PRIMARY KEY,
            target_value VARCHAR(255) NOT NULL,
            title VARCHAR(255) NOT NULL,
            description TEXT
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("✨ データベースと4つのテーブルを完全に初期化（リセット）しました！")

if __name__ == "__main__":
    init_db()