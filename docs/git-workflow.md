# Git Workflow Guidelines

## Branch Naming
- Use descriptive prefixes such as `feature/`, `bugfix/`, `hotfix/`, `docs/`, or `chore/`.
- Use kebab-case short summaries, e.g. `feature/add-login-endpoint`.
- Branch from the latest `main` and rebase frequently to stay up to date.
- Avoid pushing directly to `main`; always open a pull request.

## Commit Conventions
- Follow [Conventional Commits](https://www.conventionalcommits.org/) for
  clarity (e.g. `feat: add login endpoint`).
- Keep the subject line under 50 characters and wrap details at 72
  characters.
- Reference issue numbers when applicable (e.g. `fix: auth bug, closes #42`).
- Keep commits focused; separate unrelated changes into different commits.

## Code Review
- Open a pull request for every change and assign at least one reviewer.
- Run all tests and linters before requesting review.
- Address review feedback with follow‑up commits instead of force pushes when possible.

## Merge Policy
- Only merge changes through pull requests.
- Require at least one approved review before merging.
- All required status checks must pass.
- Prefer squash merging to keep history linear and easy to follow.
