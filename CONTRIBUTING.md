# Contributing to Smart Retail Alert & Monitoring Platform

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Code of Conduct

Be respectful, inclusive, and professional in all interactions.

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a feature branch
4. Make your changes
5. Test your changes
6. Submit a pull request

## Development Setup

See [README.md](README.md) for local development setup instructions.

## Coding Standards

### Python
- Follow PEP 8
- Use Black for formatting
- Use Ruff for linting
- Add type hints
- Write docstrings

### TypeScript/React
- Use ESLint
- Use Prettier for formatting
- Follow React best practices
- Add proper TypeScript types

## Commit Messages

Follow Conventional Commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `refactor:` Code refactoring
- `test:` Tests
- `chore:` Maintenance

Example: `feat: add real-time alert notifications`

## Pull Request Process

1. Update documentation
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Request review from maintainers

## Testing

```bash
# Backend tests
cd services/api-gateway
pytest

# Frontend tests
cd frontend
npm test
```

## Questions?

Open an issue or reach out to maintainers.
