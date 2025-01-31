<?php 
// Procesamiento de la petición... 
 
// Variables que queremos empaquetar en JSON 
$error = 60; 
$error_msg = "Error en la fecha de nacimiento"; 
 
// Array asociativo con las variables 
$datos = array( 
  "error" => $error, 
  "error_msg" => $error_msg 
); 
 
// Convertimos el array a JSON 
$json_resultado = json_encode($datos); 
 
// Devolver el resultado 
echo $json_resultado; 
?>