Get-ChildItem -Path . -Recurse -Filter "example_*.py" |
ForEach-Object {
   Write-Host "Running $($_.FullName)"
   python $_.FullName
}