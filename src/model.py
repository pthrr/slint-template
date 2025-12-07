from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class AppModel:
    counter: int = field(default=0)

    def increment(self) -> int:
        self.counter += 1
        return self.counter

    def reset(self) -> int:
        self.counter = 0
        return self.counter
