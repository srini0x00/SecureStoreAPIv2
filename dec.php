<?php

require 'db.php';

$token = 'wk3eQ9tu9LM%2Beq3I0pzst1I191hWOa9f%2BdpmRBQ6kCXJlDimqSzuLvxqAVP3v5x78cU8TW9SARQ6TCzPMjkJfw%3D%3D';

$token = rawurldecode($token);

$dectoken = exec('python aesdecrypt.py '.$token, $output);  

$str = preg_replace('/[\x00-\x1F\x80-\xFF]/', '', $dectoken);
$str = trim($str);

$query = "SELECT * FROM user WHERE token='".$str."'";
echo $query;

 $selectquer = $mysqli->query($query);

         if($selectquer->num_rows > 0) {

             while($row = $selectquer->fetch_assoc()) {
         
             $username = $row['username'];
             $email = $row['email'];
             $token = $row['token'];
             $password = $row['password'];
             
           		echo $username;
           		echo $email;
           		echo $token;
           		echo $password;

             }
        }
        else{
        	echo 'else loop';
        	echo $selectquer->num_rows;
        }

?>
