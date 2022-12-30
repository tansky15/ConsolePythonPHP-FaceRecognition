<?php
include "../Domain/Alert.php";
//{"nom_du_suspect": nom_complet, "ip": ip, "geomap": geomap, "nom_camera": nom_camera
$alert = new Alert();
$ip = $alert->setIpDuSysteme($_GET["ip"]);
$camera = $alert->setNomCamera($_GET["nom_camera"]);
$suspect = $alert->setNomDuSuspect($_GET["nom_du_suspect"]);

$bdd = new PDO("mysql:host=localhost;dbname=test;charset=utf8", "root", "");

$sendSql = $bdd->prepare("INSERT INTO iisprotect(ip,camera,suspect) values(?,?,?)");
$sendSql->execute(array($ip,$camera, $suspect));
echo "Le suspect " . $suspect . " a ete reperer dans la camera " . $camera . " d'ont l'adresse ip est " . $ip; 
?>