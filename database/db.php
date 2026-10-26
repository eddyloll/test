<?php
// データベース接続設定 (XAMPPのデフォルト：パスワードなし)
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'my_app_db');

/**
 * データベース接続を取得する関数
 */
function get_connection($use_db = true) {
    $dsn = $use_db ? "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4" : "mysql:host=" . DB_HOST . ";charset=utf8mb4";
    try {
        $pdo = new PDO($dsn, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die("❌ データベース接続エラー: " . $e->getMessage());
    }
}