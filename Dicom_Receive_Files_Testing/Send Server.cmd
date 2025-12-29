@echo off
echo ========================================
echo Starting DICOM Server...
echo AE Title : STORE_SCP
echo Port     : 10500
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4"') do set IP=%%a
set IP=%IP: =%
echo IP Addr  : %IP%
echo ========================================
echo Press Ctrl+C to stop the server.
echo.

"C:\Users\Egidijus\Desktop\Dicom_Receive_files_testing\dcmtk-3.6.9-win32-dynamic\dcmtk-3.6.9-win32-dynamic\bin\storescp.exe" -v -aet STORE_SCP 10500 -od "C:\Users\Egidijus\Desktop\Dicom_Receive_files_testing\received"
  --rename --filename-extension .dcm
