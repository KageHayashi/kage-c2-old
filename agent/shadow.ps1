$host_name = [System.Net.Dns]::GetHostName()
$sentinel_link = ("http://" + $ip + ":" + $port)