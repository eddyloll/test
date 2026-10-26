<?php
require_once __DIR__ . '/database/db.php';

// phpMyAdmin用のテーブル初期化と作成
function init_tables() {
    $pdo = get_connection(true);

    // 安全のため既存テーブルを一度削除して再作成
    $pdo->exec("DROP TABLE IF EXISTS url_scams;");
    $pdo->exec("DROP TABLE IF EXISTS mail_scams;");
    $pdo->exec("DROP TABLE IF EXISTS phone_scams;");
    $pdo->exec("DROP TABLE IF EXISTS ip_scams;");

    $tables = ["url_scams", "mail_scams", "phone_scams", "ip_scams"];
    foreach ($tables as $table) {
        $pdo->exec("CREATE TABLE {$table} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            target_value VARCHAR(255) NOT NULL,
            title VARCHAR(255) NOT NULL,
            description TEXT
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;");
    }
    echo "✨ phpMyAdmin用の4つのテーブルを完全に初期化しました！\n";
}

// 実行処理
init_tables();
$pdo = get_connection(true);

// 各テーブルに投入するサンプルデータ
$datasets = [
    "url_scams" => [
        ['http://example-phishing.com', '偽銀行ログインサイト', '大手銀行を装ったフィッシング詐欺サイトです。']
    ],
    "mail_scams" => [
        ['scam@fake-service.jp', '架空請求メール送信元', '未払い料金の請求を装う迷惑メールアドレスです。']
    ],
    "phone_scams" => [
        ['090-0000-0000', 'サポート詐欺の偽窓口', 'PCの警告画面に表示される偽サポート窓口です。']
    ],
    "ip_scams" => [
        ['185.220.101.5', '[DANGER] e-Tax Phishing', 'Bulletproof Hosting / Fake NTA Site'],
        ['210.140.10.10', '[SAFE] Official (NTA)', 'National Tax Agency Official IP']
    ]
];

foreach ($datasets as $table => $items) {
    $stmt = $pdo->prepare("INSERT INTO {$table} (target_value, title, description) VALUES (?, ?, ?)");
    foreach ($items as $item) {
        $stmt->execute($item);
    }
}

echo "✅ テストデータの流し込みが完了しました。phpMyAdminで中身を確認できます！\n";