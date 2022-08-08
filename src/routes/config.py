"""
Runtime Arguments Example

A simple GET the global runtime args.

Copyright: Oblivious Software Ltd, 2022.
"""

import settings.settings as settings
from fastapi import APIRouter

router = APIRouter(
    tags=["service_settings"]
    )

@router.get("")
def config():
    runtime_config = settings.get_settings()
    return runtime_config