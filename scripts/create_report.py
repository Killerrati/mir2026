"""Создаёт файл-артефакт без внешних зависимостей."""
from datetime import datetime, timezone
from pathlib import Path
import platform

out = Path("dist/report.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(
    "CI demo report\n"
    f"Python: {platform.python_version()}\n"
    f"OS: {platform.system()}\n"
    f"Generated (UTC): {datetime.now(timezone.utc).isoformat()}\n",
    encoding="utf-8",
)
print(f"Created {out}:")
print(out.read_text(encoding="utf-8"))
