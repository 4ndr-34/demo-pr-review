# Quick setup script for demo project (PowerShell)

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "Multi-Agent PR Review - Demo Setup" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

# Check if we're in the right directory
if (-not (Test-Path "README.md")) {
    Write-Host "Error: Run this script from the demo-project directory" -ForegroundColor Red
    exit 1
}

Write-Host "Step 1: Initialize Git repository"
if (-not (Test-Path ".git")) {
    git init
    Write-Host "Git repository initialized" -ForegroundColor Green
} else {
    Write-Host "Git repository already exists" -ForegroundColor Green
}

Write-Host ""
Write-Host "Step 2: Create initial commit"
git add .
git commit -m "Initial commit: Demo project for multi-agent review" 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "Initial commit created" -ForegroundColor Green
} else {
    Write-Host "Already committed" -ForegroundColor Green
}

Write-Host ""
Write-Host "Step 3: Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Create a GitHub repository:"
Write-Host "   - Go to github.com/new"
Write-Host "   - Name: demo-pr-review"
Write-Host "   - Public repository"
Write-Host "   - Don't initialize with README"
Write-Host ""
Write-Host "2. Push to GitHub:"
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/demo-pr-review.git"
Write-Host "   git branch -M main"
Write-Host "   git push -u origin main"
Write-Host ""
Write-Host "3. Add your OpenAI API key as a repository secret:"
Write-Host "   Settings → Secrets → Actions → New secret"
Write-Host "   Name: OPENAI_API_KEY"
Write-Host "   Value: your-api-key"
Write-Host ""
Write-Host "4. Enable GitHub Actions:"
Write-Host "   Settings → Actions → General"
Write-Host "   Select 'Read and write permissions'"
Write-Host ""
Write-Host "5. Create your first test PR:"
Write-Host "   git checkout -b fix/sql-injection"
Write-Host "   # Edit src\api\users.py to fix SQL injection"
Write-Host "   git commit -am 'Fix SQL injection vulnerability'"
Write-Host "   git push -u origin fix/sql-injection"
Write-Host "   # Then create PR on GitHub"
Write-Host ""
Write-Host "6. Watch the magic happen! " -ForegroundColor Green -NoNewline
Write-Host "🚀"
Write-Host "   The PR will be reviewed automatically within 60 seconds"
Write-Host ""
