# HTTPS Data Exfiltration Lab (PoC)

Este laboratorio demuestra cómo exfiltrar archivos de manera controlada usando **HTTPS** con un servidor Python y un cliente PowerShell.

> ⚠️ Solo usar en entornos propios o laboratorios. No atacar sistemas ajenos.

---
## Componentes

### 1. Servidor HTTPS (Python)
- Escucha en el puerto 8443 con TLS/SSL.
- Recibe datos vía solicitudes POST.
- Guarda la información en `exfiltrated.txt`.
- Requiere un certificado SSL (`cert.pem`).
- Ejecutar:
```bash
python3 https_server.py
```

### 2. Cliente HTTPS (PowerShell)

- Deshabilita la validación de certificados (solo para laboratorio).
- Lee un archivo y lo envía vía POST al servidor HTTPS.
- Configurar:
```powershell
$File = "C:\Users\roman.gomez\Desktop\testing.txt"
$URL = "https://192.168.100.10:8443"
```
- Ejecutar:
```powershell
.\https_client.ps1
```
___
## Flujo

1. Servidor Python escucha en `0.0.0.0:8443` con TLS.
2. Cliente PowerShell envía el archivo al servidor.
3. Servidor recibe los datos, los almacena en `exfiltrated.txt` y confirma la recepción en consola.
---
## Requisitos

- Python 3.x con soporte SSL/TLS.
- PowerShell 5.1+ (Windows).
- Certificado SSL válido (`cert.pem`) para pruebas.
- Laboratorio controlado o red interna.
