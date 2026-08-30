## Brain Games

[![Actions Status](https://github.com/mikitasazan/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mikitasazan/devops-engineer-from-scratch-project-49/actions)

Учебный Python-проект с единым игровым движком и пятью консольными играми:
`brain-even`, `brain-calc`, `brain-gcd`, `brain-progression` и `brain-prime`.
Каждая игра задаёт три вопроса, проверяет ответы и показывает правильное
решение при ошибке.

## Требования

- Python 3.10+;
- `uv`.

## Установка и запуск

```bash
make install
uv run brain-games
uv run brain-prime
```

## Проверки

```bash
make lint
make build
```

Точка входа каждой игры объявлена в `pyproject.toml`, а общая логика диалога
находится в `brain_games/engine.py`.
