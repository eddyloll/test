<?php
require_once __DIR__ . '/database/db.php';

$pdo = get_connection(true);

$target_tables = [
    ["url_scams", "🔗 URL詐欺データ", "URL"],
    ["mail_scams", "✉️ メール詐欺データ", "メールアドレス"],
    ["phone_scams", "📞 電話番号詐欺データ", "電話番号"],
    ["ip_scams", "🌐 IPアドレス詐欺データ", "IPアドレス"]
];

echo "\n" . str_repeat("=", 60) . "\n";
echo "       ソーシャルエンジニアリング データベース全件一覧 (PHP)       \n";
echo str_repeat("=", 60) . "\n";

foreach ($target_tables as [$table_name, $display_title, $label]) {
    echo "\n■ {$display_title} ({$table_name})\n";
    echo str_repeat("-", 60) . "\n";
    
    $stmt = $pdo->query("SELECT id, target_value, title, description FROM {$table_name}");
    $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
    if (empty($rows)) {
        echo "  （登録されているデータはありません）\n";
    } else {
        foreach ($rows as $row) {
            echo "  [ID: {$row['id']}]\n";
            echo "    {$label} : {$row['target_value']}\n";
            echo "    タイトル: {$row['title']}\n";
            echo "    説明    : {$row['description']}\n";
            echo "    " . str_repeat("-", 50) . "\n";
        }
    }
}
echo "\n" . str_repeat("=", 60) . "\n";