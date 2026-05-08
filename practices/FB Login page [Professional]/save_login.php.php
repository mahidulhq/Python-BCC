<?php
session_start();

// Database connection
$servername = "localhost";
$username = "root"; // XAMPP default
$password = "";
$dbname = "fb_clone";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get POST data
$userid = $_POST['userid'];
$password_plain = $_POST['password'];

// Hash password
$password_hashed = password_hash($password_plain, PASSWORD_DEFAULT);

// Insert into database
$sql = "INSERT INTO login_attempts (userid, password) VALUES (?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $userid, $password_hashed);

if($stmt->execute()){
    $_SESSION['msg'] = "Login attempt saved successfully!";
}else{
    $_SESSION['msg'] = "Error: ".$conn->error;
}

$stmt->close();
$conn->close();

// Redirect back
header("Location: index.php");
exit;
?>