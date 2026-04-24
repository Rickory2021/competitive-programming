# ──────────────────────────────────────────────
# competitive-programming — Makefile
# ──────────────────────────────────────────────
PYTHON   := python3
VENV     := .venv
BIN      := $(VENV)/bin
PIP      := $(BIN)/pip
PY       := $(BIN)/python

# ── Setup ────────────────────────────────────

.PHONY: setup
setup: $(VENV) ## Create venv and install dev deps
	@echo "✓ venv ready — run 'source $(VENV)/bin/activate'"

$(VENV):
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]" 2>/dev/null || $(PIP) install ruff pytest ipython

.PHONY: clean
clean: ## Nuke the venv
	rm -rf $(VENV)

# ── Utilities ────────────────────────────────
# Running / testing / scaffolding handled by CPH extension (Ctrl+Alt+B)

.PHONY: tidy
tidy: ## Move solution .py files from root → contests/ (updates .cph metadata)
	@$(PY) tidy.py

.PHONY: lint
lint: ## Lint all .py files
	$(BIN)/ruff check .

.PHONY: fmt
fmt: ## Format all .py files
	$(BIN)/ruff format .

.PHONY: stress
stress: ## Run pytest (stress tests, generators)
	$(BIN)/pytest -v

.PHONY: help
help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
