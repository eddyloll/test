<?php
require_once __DIR__ . '/../database/db.php';

function check_ip($ip_address) {
    $pdo = get_connection(true);
    
    // ip_scams テーブルから一致するIPを検索
    $stmt = $pdo->prepare("SELECT target_value, title, description FROM ip_scams WHERE target_value = ?");
    $stmt->execute([$ip_address]);
    $result = $stmt->fetch(PDO::FETCH_ASSOC);
    
    echo "\n[IPチェック結果] 対象: {$ip_address}\n";
    if ($result) {
        echo "⚠️ 警告: データベースに登録されている危険/監視対象のIPです！\n";
        echo "  - タイトル: {$result['title']}\n";
        echo "  - 詳細    : {$result['description']}\n";
    } else {
        echo "✅ 安全: 一致する脅威データは見つかりませんでした。\n";
    }
}

// 直接実行された場合のテスト
if (basename(__FILE__) === basename($_SERVER['SCRIPT_FILENAME'])) {
    echo "テストするIPアドレスを入力してください: ";
    $input_ip = trim(fgets(STDIN));
    if ($input_ip !== '') {
        check_ip($input_ip);
    }
}