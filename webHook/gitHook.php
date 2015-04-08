<?php 
try
{
  $payload = json_decode($_REQUEST['payload']);
}
catch(Exception $e)
{
  exit(0);
}

// exec('/home/ubuntu/Blind-Bet/webHook/pull.sh');

echo "Done";
?>