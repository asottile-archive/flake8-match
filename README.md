# ARHIVED

it is feature complete and I don't plan on updating it further

___

[![build status](https://github.com/asottile/flake8-match/actions/workflows/main.yml/badge.svg)](https://github.com/asottile/flake8-match/actions/workflows/main.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/flake8-match/main.svg)](https://results.pre-commit.ci/latest/github/asottile/flake8-match/main)

flake8-match
============

flake8 plugin which forbids match statements (PEP 634)

## installation

```bash
pip install flake8-match
```

## flake8 codes

| Code   | Description                 |
|--------|-----------------------------|
| MAT001 | do not use match statements |

## rationale

lol

## as a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/pycqa/flake8
    rev: 3.8.4
    hooks:
    -   id: flake8
        additional_dependencies: [flake8-match==1.0.0]
```
