# Windows 11 Calculator
# Part of Windows App Essentials collection
# Copyright 2021-2022 Joseph Lee, released under GPL

# This is similar to older Calculator app but was redesigned from ground up.
# NVDA Core and Windows 10 Calculator from this add-on includes bulk of this app module.
# App module part of NVDA 2022.1.
from .calculator import AppModule, noCalculatorEntryAnnouncements
__all__ = ["AppModule", "noCalculatorEntryAnnouncements"]
