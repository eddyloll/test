<?php
require_once __DIR__ . '/../database/db.php';

function check_url($url_string) {
    $pdo = get_connection(true);
    
    $stmt = $pdo->prepare("SELECT target_value, title, description FROM url_scams WHERE target_value = ?");
    $stmt->execute([$url_string]);
    $result = $stmt->fetch(PDO::FETCH_ASSOC);
    
    echo "\n[URLチェック結果] 対象: {$url_string}\n";
    if ($result) {
        echo "⚠️ 警告: フィッシング詐欺サイト等の危険なURLとして登録されています！\n";
        echo "  - タイトル: {$result['title']}\n";
        echo "  - 詳細    : {$result['description']}\n";
    } else {
        echo "✅ 安全: 一致する脅威データは見つかりませんでした。\n";
    }
}

if (basename(__FILE__) === basename($_SERVER['SCRIPT_FILENAME'])) {
    echo "テストするURLを入力してください: ";
    $input_url = trim(fgets(STDIN));
    if ($input_url !== '') {
        check_url($input_url);
    }
}