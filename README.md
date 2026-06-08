# Demo Project - Multi-Agent PR Review

This is a demonstration project showcasing the multi-agent PR review system.

## Purpose

- Demonstrate automated PR review with multi-agent system
- Provide examples of different code quality issues
- Test GitHub Actions integration
- Evaluate thesis hypothesis in real-world scenario

## Setup

1. Fork this repository
2. Add repository secrets:
   - `OPENAI_API_KEY` - Your OpenAI API key
   - `GITHUB_TOKEN` - Automatically provided by GitHub
3. Create a PR to trigger the review workflow

## Features

- Automatic PR review on every pull request
- Multi-agent analysis (Security, Performance, Architecture)
- Results posted as PR comments
- Quality score and grade assignment

## Sample PRs to Create

Create PRs with these issues to test the system:

1. **Security Issues** - SQL injection, XSS vulnerabilities
2. **Performance Issues** - N+1 queries, inefficient algorithms
3. **Architecture Issues** - SOLID violations, code smells
4. **Clean Code** - Well-written code to test positive cases

## Project Structure

```
demo-project/
├── src/
│   ├── api/          # API endpoints
│   ├── models/       # Data models
│   └── utils/        # Utility functions
├── tests/            # Test files
├── .github/
│   └── workflows/    # GitHub Actions
└── README.md
```
