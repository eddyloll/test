<?php
require_once __DIR__ . '/../database/db.php';

function check_mail($mail_address) {
    $pdo = get_connection(true);
    
    $stmt = $pdo->prepare("SELECT target_value, title, description FROM mail_scams WHERE target_value = ?");
    $stmt->execute([$mail_address]);
    $result = $stmt->fetch(PDO::FETCH_ASSOC);
    
    echo "\n[メールチェック結果] 対象: {$mail_address}\n";
    if ($result) {
        echo "⚠️ 警告: 迷惑メール・詐欺メールの送信元として登録されています！\n";
        echo "  - タイトル: {$result['title']}\n";
        echo "  - 詳細    : {$result['description']}\n";
    } else {
        echo "✅ 安全: 一致する脅威データは見つかりませんでした。\n";
    }
}

if (basename(__FILE__) === basename($_SERVER['SCRIPT_FILENAME'])) {
    echo "テストするメールアドレスを入力してください: ";
    $input_mail = trim(fgets(STDIN));
    if ($input_mail !== '') {
        check_mail($input_mail);
    }
}