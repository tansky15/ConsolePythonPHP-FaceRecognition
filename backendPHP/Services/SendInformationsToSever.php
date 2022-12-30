<?php
//connection a la base de donnees 
$bdd = new PDO("mysql:host=localhost;dbname=test;charset=utf8", "root", "");
//recuperation des informations envoyer par le server 
$ip = htmlspecialchars($_GET["ip"]);
$camera = htmlspecialchars($_GET["nom_camera"]);
$suspect = htmlspecialchars($_GET["nom_du_suspect"]);
$longitude = htmlspecialchars($_GET['longitude']);
$latitude = htmlspecialchars($_GET['latitude']);
//preparation de la requette 
$sendSql = $bdd->prepare("INSERT INTO iisprotect(ip,camera,suspect,longitude,latitude) values(?,?,?,?,?)");
//execution de la requette
$sendSql->execute(array($ip,$camera, $suspect,$longitude,$latitude));
//renvoie d'une confirmations 
echo  $suspect . " a ete reperer dans la camera " . $camera . " d'ont l'adresse ip est " . $ip. ", localiser a (long: ".$longitude.", lat:".$latitude." )"; 
?>