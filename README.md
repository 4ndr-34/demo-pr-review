# Demo PR Review Project

This project is designed to test the multi-agent PR review system.

## Purpose

Contains intentional code issues to validate that the review system can detect:
- Security vulnerabilities (SQL injection, XSS, weak passwords)
- Performance issues (N+1 queries, O(n²) algorithms)
- Architecture smells (god classes, code duplication, SOLID violations)

## Usage

1. Create a branch
2. Make changes
3. Open a Pull Request
4. Automated review runs via GitHub Actions
5. Results posted as PR comment

## Data Collection

All review results are automatically saved to the `data-collection` branch for thesis analysis.

## Testing Scenarios

- Fix security issues → See quality score improve
- Add performance optimization → Verify detection
- Refactor architecture → Check pattern recognition
- Submit clean code → Confirm positive feedback
