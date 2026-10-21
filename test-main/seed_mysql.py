import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from database.db import get_connection, init_db

def seed_data():

    init_db()

    conn = get_connection()
    cursor = conn.cursor()

    # 各テーブル用のテストデータ
    url_samples = [
        ('http://example-phishing.com', '偽銀行ログインサイト', '大手銀行を装ったフィッシング詐欺サイトです。口座情報の入力にご注意ください。')
    ]
    mail_samples = [
        ('scam@fake-service.jp', '架空請求・迷惑メール送信元', '「未払い料金があります」というメッセージを送りつけて不安を煽る迷惑メールアドレスです。')
    ]
    phone_samples = [
        ('090-0000-0000', 'サポート詐欺の偽窓口', 'PCの警告画面に表示される偽のマイクロソフトサポート問い合わせ窓口です。')
    ]
    ip_samples = [
        ('203.0.113.50', '悪意あるアクセス元IP', '多数のWebサイトに対してSSHブルートフォース攻撃（総当たり攻撃）を行っている不正IPアドレスです。')
    ]

    # 一括挿入
    cursor.executemany("INSERT INTO url_scams (target_value, title, description) VALUES (%s, %s, %s)", url_samples)
    cursor.executemany("INSERT INTO mail_scams (target_value, title, description) VALUES (%s, %s, %s)", mail_samples)
    cursor.executemany("INSERT INTO phone_scams (target_value, title, description) VALUES (%s, %s, %s)", phone_samples)
    cursor.executemany("INSERT INTO ip_scams (target_value, title, description) VALUES (%s, %s, %s)", ip_samples)

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ MySQLの4つのテーブルにテストデータを正常に流し込みました！")

if __name__ == "__main__":
    seed_data()