from typing import List

from inim_prime import InimPrimeClient
from inim_prime.models import ZoneStatus, ZoneExclusionSetRequest


async def get_excluded_zones(client: InimPrimeClient) -> List[ZoneStatus]:
    zones = await client.get_zones_status()
    return [z for z in zones.values() if z.excluded]


async def include_all_zones(client: InimPrimeClient) -> List[ZoneStatus]:
    """
    Sets all currently excluded zones to included.

    Returns:
        List of zones that were changed.
    """
    excluded_zones = await get_excluded_zones(client)

    for zone in excluded_zones:
            request = ZoneExclusionSetRequest(zone_id=zone.id, exclude=False)
            await client.set_zone_exclusion(request)

    return excluded_zones