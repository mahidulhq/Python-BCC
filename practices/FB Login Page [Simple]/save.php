<?php

include "connect.php";

$userid = $_POST['userid'];
$password = $_POST['password'];

$sql = "INSERT INTO users(userid, password)
        VALUES('$userid', '$password')";

mysqli_query($conn, $sql);

echo "Login data saved successfully!";

?>
