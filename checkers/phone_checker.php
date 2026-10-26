<?php
require_once __DIR__ . '/../database/db.php';

function check_phone($phone_number) {
    $pdo = get_connection(true);
    
    $stmt = $pdo->prepare("SELECT target_value, title, description FROM phone_scams WHERE target_value = ?");
    $stmt->execute([$phone_number]);
    $result = $stmt->fetch(PDO::FETCH_ASSOC);
    
    echo "\n[電話番号チェック結果] 対象: {$phone_number}\n";
    if ($result) {
        echo "⚠️ 警告: サポート詐欺や架空請求の連絡先として登録されています！\n";
        echo "  - タイトル: {$result['title']}\n";
        echo "  - 詳細    : {$result['description']}\n";
    } else {
        echo "✅ 安全: 一致する脅威データは見つかりませんでした。\n";
    }
}

if (basename(__FILE__) === basename($_SERVER['SCRIPT_FILENAME'])) {
    echo "テストする電話番号を入力してください: ";
    $input_phone = trim(fgets(STDIN));
    if ($input_phone !== '') {
        check_phone($input_phone);
    }
}