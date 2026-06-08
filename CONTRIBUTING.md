# Contributing to Demo Project

## Purpose

This is a demonstration project for testing the multi-agent PR review system. Contributions should focus on:

1. Creating test cases for different issue types
2. Demonstrating the review system's capabilities
3. Evaluating the multi-agent approach

## Creating Test PRs

### Good Test PR Examples

1. **Security Fix**
   - Fix SQL injection in `src/api/users.py`
   - Expected: Positive security review

2. **Performance Optimization**
   - Add pagination to `get_all_users()`
   - Expected: Performance agent approval

3. **Architecture Improvement**
   - Refactor `transform_data()` to strategy pattern
   - Expected: Architecture agent approval

4. **Introduce Issues** (for testing)
   - Add code with known vulnerabilities
   - Expected: Agents flag issues

### PR Guidelines

1. **One concept per PR** - Easier to review
2. **Clear description** - Explain what and why
3. **Test the review** - Does it catch the issues?
4. **Document findings** - For thesis evaluation

## Testing Issues to Add

Feel free to add PRs that test:

- [ ] XSS vulnerabilities
- [ ] CSRF issues
- [ ] Race conditions
- [ ] Memory leaks
- [ ] Slow algorithms (O(n³), etc.)
- [ ] Circular dependencies
- [ ] God classes
- [ ] Tight coupling
- [ ] Missing error handling

## Review Process

1. Create PR
2. Wait for automated review (~30-60s)
3. Check review comment
4. Analyze results
5. Document for thesis

## Questions?

This is a thesis project. For questions about the review system, see the main repository README.
