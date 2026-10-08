"""Shared Jobs_2026 dataset discovery for course notebooks and scripts."""

import os
import platform
from pathlib import Path


def resolve_jobs_data_dir() -> Path:
    """Choose the local dataset folder; JOBS_DATA_DIR overrides detection."""
    override = os.getenv("JOBS_DATA_DIR", "").strip()
    if override:
        return Path(override).expanduser().resolve()

    if platform.system() == "Windows":
        hostname = platform.node().upper().split(".")[0]
        office = Path("D:/Boston/AD688/Data/Jobs_2026_US")
        home = Path("E:/Data/Jobs_2026")
        if hostname == "DESKTOP-95RT96I":
            return office.resolve()
        if hostname == "DESKTOP-BSQIUTN":
            return home.resolve()
        for candidate in (office, home):
            if candidate.is_dir():
                return candidate.resolve()

    # EC2 downloads live beside the repository. Search ancestors so module
    # folders, repo-root renders, and standalone student notebooks all work.
    cwd = Path.cwd().resolve()
    for directory in (cwd, *cwd.parents):
        candidate = directory / "Jobs_2026"
        if candidate.is_dir():
            return candidate.resolve()
        if (directory / ".git").exists() or (directory / "_quarto.yml").is_file():
            return (directory.parent / "Jobs_2026").resolve()
    return (cwd.parent / "Jobs_2026").resolve()
