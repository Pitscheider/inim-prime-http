from dataclasses import dataclass
from enum import IntEnum
from typing import Optional, FrozenSet

class SystemFault(IntEnum):
    # Byte 0
    AVAILABLE_1 = 0
    AVAILABLE_2 = 1
    LOW_BATTERY = 2
    NETWORK_FAULT = 3
    NO_TELEPHONE_LINE = 4
    RADIO_JAMMING = 5
    LOW_BATTERY_WIRELESS = 6
    WIRELESS_DEVICE_DISAPPEARANCE = 7

    # Byte 1
    GSM_FAULT = 8
    SENSOR_DIRTY = 9
    ZONE_FAULT = 10
    SIRENS_FAULT = 11
    POWER_SUPPLY_FAULT = 12
    RADIO_KEYBOARDS_FAULT = 13
    SABOTAGE_FAULT = 14
    INTERNET_FAULT = 15

@dataclass(frozen=True)
class SystemFaultsStatus:
    supply_voltage: Optional[float]
    faults: FrozenSet[SystemFault]

    def __str__(self) -> str:
        lines = ["System Faults Status:"]

        if self.supply_voltage is not None:
            lines.append(f"  Supply voltage: {self.supply_voltage} V")

        if self.faults:
            lines.append("  Active faults:")
            for fault in sorted(self.faults, key=lambda f: f.value):
                lines.append(f"    - {fault.name}")
        else:
            lines.append("  No active faults")

        return "\n".join(lines)

    @property
    def has_any_fault(self) -> bool:
        return bool(self.faults)

    def has_fault(self, fault: SystemFault) -> bool:
        return fault in self.faults
