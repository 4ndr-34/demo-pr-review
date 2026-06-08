#!/bin/bash
# Quick setup script for demo project

echo "========================================="
echo "Multi-Agent PR Review - Demo Setup"
echo "========================================="
echo ""

# Check if we're in the right directory
if [ ! -f "README.md" ]; then
    echo "❌ Error: Run this script from the demo-project directory"
    exit 1
fi

echo "Step 1: Initialize Git repository"
if [ ! -d ".git" ]; then
    git init
    echo "✓ Git repository initialized"
else
    echo "✓ Git repository already exists"
fi

echo ""
echo "Step 2: Create initial commit"
git add .
git commit -m "Initial commit: Demo project for multi-agent review" 2>/dev/null || echo "✓ Already committed"

echo ""
echo "Step 3: Setup complete!"
echo ""
echo "Next steps:"
echo "1. Create a GitHub repository:"
echo "   gh repo create demo-pr-review --public --source=. --remote=origin --push"
echo "   (or create manually at github.com/new)"
echo ""
echo "2. Add your OpenAI API key as a repository secret:"
echo "   Settings → Secrets → Actions → New secret"
echo "   Name: OPENAI_API_KEY"
echo "   Value: your-api-key"
echo ""
echo "3. Enable GitHub Actions:"
echo "   Settings → Actions → General"
echo "   Select 'Read and write permissions'"
echo ""
echo "4. Create your first test PR:"
echo "   git checkout -b fix/sql-injection"
echo "   # Edit src/api/users.py to fix SQL injection"
echo "   git commit -am 'Fix SQL injection vulnerability'"
echo "   git push -u origin fix/sql-injection"
echo "   # Then create PR on GitHub"
echo ""
echo "5. Watch the magic happen! 🚀"
echo "   The PR will be reviewed automatically within 60 seconds"
echo ""
