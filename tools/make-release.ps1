# Packs Belgica for a GitHub release / NOMM: belgica.zip with the map and its credits.
# Run in PowerShell:  & ".\make-release.ps1"
$ErrorActionPreference = "Stop"
$src = "$env:USERPROFILE\Downloads\OpenSkies-0.1.0\OpenSkies\data\out\belgica"
$out = "$env:USERPROFILE\Downloads\belgica-release"
$tmp = Join-Path $env:TEMP "belgica-release-staging"

if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force }
New-Item -ItemType Directory -Force $tmp, $out | Out-Null
Copy-Item "$src\belgica.nomap" $tmp
Copy-Item "$src\README.txt" "$tmp\CREDITS.txt"
Write-Host "Zipping (about 1.9 GB, no compression: the map is already compressed)..."
Compress-Archive -Path "$tmp\*" -DestinationPath "$out\belgica.zip" -CompressionLevel NoCompression -Force
Remove-Item $tmp -Recurse -Force

$zip = Get-Item "$out\belgica.zip"
$hash = (Get-FileHash $zip.FullName -Algorithm SHA256).Hash.ToLower()
Write-Host ""
Write-Host "Done: $($zip.FullName)"
Write-Host ("Size: {0:N0} bytes (GitHub limit 2,147,483,648)" -f $zip.Length)
Write-Host "SHA-256: $hash"
Invoke-Item $out
