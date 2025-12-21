from dataclasses import dataclass
from enum import IntEnum

from inim_prime.models import PanelItemStatus


class AreaMode(IntEnum):
    TOTAL = 1
    PARTIAL = 2
    INSTANT = 3
    DISARMED = 4
    CLEAR_ALARM_MEMORY = 5


class AreaControlMode(IntEnum):
    TOTAL = AreaMode.TOTAL
    PARTIAL = AreaMode.PARTIAL
    INSTANT = AreaMode.INSTANT
    DISARMED = AreaMode.DISARMED

class AreaArmMode(IntEnum):
    TOTAL = AreaMode.TOTAL
    PARTIAL = AreaMode.PARTIAL
    INSTANT = AreaMode.INSTANT


class AreaState(IntEnum):
    ALARM = 0
    READY = 1
    SABOTAGE = 2

@dataclass(frozen=True)
class AreaStatus(PanelItemStatus):
    mode: AreaControlMode       # "am" - insert mode
    state: AreaState     # "st" - area status
    alarm_memory: bool   # "mm" - alarm memory

    def __str__(self) -> str:
        return (
            f"Area {self.id}: {self.name}\n"
            f"  Mode: {self.mode.name}\n"
            f"  State: {self.state.name}\n"
            f"  Alarm memory: {'Yes' if self.alarm_memory else 'No'}"
        )

@dataclass(frozen=True)
class SetAreaModeRequest:
    area_id: int
    mode: AreaMode

@dataclass(frozen=True)
class ActivateScenarioRequest:
    scenario_id: int
