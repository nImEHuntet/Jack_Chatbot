Write-Host "Welcome to (jack) the chatbot 0.0.1"
Write-Host "By ayushmaan karmokar." -ForegroundColor Red -BackgroundColor Yellow -NoNewline
Write-Host
Write-Host
Write-Host
Write-Host ("Hello " + $env:USERNAME)
python -V
$version = python -V
Write-Host $version
if($version -eq "Python 3.8.0"){
   write-host("you have python 3.8.0 - running script")
   python jack_0.0.1.py
}else {
   write-host("not python 3.8.0 sys exit.")
}
Read-Host -Prompt "Press Enter to continue"
