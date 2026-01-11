from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class GSMSStatus:
    supply_voltage: Optional[float]   # "vcc"
    firmware_version: Optional[str]   # "fwv"
    operator: Optional[str]           # "gop"
    signal_strength: Optional[int]    # gpw (CSQ / RSSI index)
    credit: Optional[str]             # "cre"

    def __str__(self) -> str:
        parts = ["GSM Status:"]

        if self.supply_voltage is not None:
            parts.append(f"  Supply voltage: {self.supply_voltage} V")

        if self.firmware_version:
            parts.append(f"  Firmware version: {self.firmware_version}")

        if self.operator:
            parts.append(f"  Operator: {self.operator}")

        if self.signal_strength is not None:
            parts.append(f"  Signal strength (CSQ): {self.signal_strength}")

        if self.credit:
            parts.append(f"  Credit: {self.credit}")

        return "\n".join(parts)

    @property
    def signal_strength_dbm(self) -> Optional[int]:
        """Convert CSQ to dBm (-113 + 2*CSQ). Returns None if unknown."""
        if self.signal_strength is None or self.signal_strength == 99:
            return None
        return -113 + 2 * self.signal_strength