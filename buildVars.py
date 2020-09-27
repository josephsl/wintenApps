# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext
def _(arg):
	return arg


# Add-on information variables
addon_info = {
	# add-on Name/identifier, internal for NVDA
	"addon_name": "wintenApps",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on
	# to be shown on installation and add-on information.
	"addon_summary": _("Windows 10 App Essentials"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description": _("""A collection of app modules for various Windows 10 apps"""),
	# version
	"addon_version": "20.10",
	# Author(s)
	"addon_author": "Joseph Lee <joseph.lee22590@gmail.com>, Derek Riemer <driemer.riemer@gmail.com> and others",
	# URL for the add-on documentation support
	"addon_url": "https://addons.nvda-project.org/",
	# Documentation file name
	"addon_docFileName": "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3.0", minor version is optional)
	"addon_minimumNVDAVersion": "2020.2",
	# Last NVDA version supported/tested (e.g. "2018.4.0", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion": "2020.4",
	# Minimum Windows version supported
	"addon_minimumWindowsVersion": "10.0.18363",
	# Add-on update channel (default is None, denoting stable releases,
	# and for development releases, use "dev".)
	# Do not change unless you know what you are doing!
	"addon_updateChannel": None,
}


import os.path  # NOQA

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [
	os.path.join("addon", "*.py"),
	os.path.join("addon", "appModules", "*.py"),
	os.path.join("addon", "globalPlugins", "wintenObjs.py")
]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
