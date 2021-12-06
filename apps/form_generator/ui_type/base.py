from abc import ABC
from dataclasses import dataclass, asdict, field
from typing import Optional, Dict, Any, List


class FormUnit(ABC):
    def get_schema(self):
        return asdict(self)


@dataclass
class BaseFormUnit(FormUnit):
    widget: Any
    name: Optional[str] = None
    label: Optional[str] = None
    value: Optional[str] = None
    choices: List[Any] = field(default_factory=list)
    extra_options: Dict[str, str] = field(default_factory=dict)

