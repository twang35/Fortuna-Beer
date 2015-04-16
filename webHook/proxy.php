<?php
header("Content-type: text/javascript; charset=utf-8");
// $c = $_GET['a'];
// $s = file_get_contents('http://yourdomain.com/json/' . $c . '.json');
$s = file_get_contents('http://api.brewerydb.com/v2/search?type=beer&q=asdf&key=5b3814c58c765b0d58b67d3525c4850b&format=json');
header("Access-Control-Allow-Origin: *");
echo $_GET['callback'] . '(' . $s . ');';
?>