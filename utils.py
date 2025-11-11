#!/usr/bin/env python3
"""Shared utility functions for mcp-oauth-gateway project."""

from pathlib import Path
from typing import Optional


def get_project_root() -> Path:
    """Get the project root directory (where this utils.py is located)."""
    return Path(__file__).parent


def save_env_var(
    key: str,
    value: str,
    env_file: Optional[Path] = None
) -> None:
    """
    Save or update an environment variable in .env file.

    Args:
        key: Environment variable name
        value: Environment variable value
        env_file: Optional path to .env file. If not provided, uses project root/.env
    """
    if env_file is None:
        env_file = get_project_root() / ".env"

    lines = []
    found = False

    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                if line.strip().startswith(f"{key}="):
                    lines.append(f"{key}={value}\n")
                    found = True
                else:
                    lines.append(line)

    if not found:
        lines.append(f"\n{key}={value}\n")

    with open(env_file, "w") as f:
        f.writelines(lines)
