# Contributing to Windows App Essentials NVDA add-on

IMPORTANT: Windows App Essentials add-on is end of life. This document remains in the add-on code repository to provide historical information on the add-on contribution process.

Thank you for your interest in contributing to Windows App Essentials NVDA add-on. The purpose of this document is to outline the overall add-on contribution requirements, development process, and offer tips when contributing.

## Important notes

Before reading further, please read this section to better understand specifics about this add-on:

1. This add-on is optimized for recent releases of Windows 11. As such, safeguards are in place to prevent installation on older Windows releases such as 8.1. Put it the other way, in order to contribute, you must be running Windows 11, specifically supported Windows releases (see Windows Release Information page offered by Microsoft for a list of supported Windows releases).
2. This add-on is optimized for recent NVDA releases and is sensitive to it. From time to time the add-on drops support for older NVDA releases in order to take advantage of changes introduced in newer NVDA releases. For effective contributions, you should use latest stable version of NVDA and/or latest alpha/beta/release candidate builds.
3. Occasionally you may need to use other add-ons and/or tools in addition to the add-on. When debugging event handling, you must use either Event Tracker add-on or AccEvent from Windows Software Development Kit (SDK).
4. This add-on does not replace the need to contact app developers. Although the add-on can cover accessibility issues with apps (or you can contribute fixes for apps in regards to accessibility issues such as incorrect labels), ideal fixes should come from vendors themselves.

## Ways to contribute

You can contribute to Windows App Essentials in a number of ways:

1. Testing: provided that you are using supported Windows releases (including latest Windows Insider Preview build) with latest NVDA and the add-on installed, you can help improve the add-on by testing and providing feedback.
2. Localization: you can translate add-on documentation and messages via NVDA translations workflow (Subversion or Crowdin). The author (Joseph Lee) does not take pull requests involving localization data.
3. Issues and pull requests: the author welcomes issues and pull requests submitted via GitHub (see the section on issues and pull requests for more information).

## Contribution requirements

You must:

1. Be running the latest supported version of Windows 11 (as of September 2025, this means Windows 11 2024 Update (Version 24H2) and latest Insider Preview (canary/dev/beta/release preview) build).
2. Be running the latest stable version of NVDA or later (as of September 2025, this means NVDA 2025.3 or latest alpha release).
3. If you wish to offer code/pull requests, you must be running latest stable NVDA (2025.3) and Windows 11 (24H2) release or later.
4. To package your modifications into an add-on build, you must be using Python 3.13 or later.

## Contribution process

### Testing the add-on

You can contribute by testing the add-on. To facilitate this, a development snapshot of this add-on is released from time to time so people can test latest changes.

To test the add-on, you must be running the latest stable or development build of NVDA and latest stable or development build of Windows App Essentials. You can obtain latest Windows App Essentials via NV Access add-on store (NVDA menu/Tools/add-on store, available or updatable add-ons tab). For effective testing, you must also be running latest Windows release (public release or latest Insider Preview build).

Before testing the add-on:

1. Install the latest availible NVDA release.
2. Visit NV Access add-on store (NVDA menu/tools/add-on store).
3. Check Windows App Essentials add-on version from installed add-ons tab. If the version is of the form yyyymmdd.x.y, you do not have to perform dev channel installation step but do try updating to the latest version (see below).
4. To switch to dev channel, from add-on store, press Control+Tab to go to either updatable or available add-ons tabs.
5. Select "all" or "dev" from channel list.
6. Press Tab several times until arriving at updatable/available add-ons list, then select Windows App Essentials add-on version of the form yyyymmdd.x.y e.g. 20230905.0.0.
7. Press Enter, then from the context menu, select "update" or "install" depending on if Windows Ap Essentials is installed or not.
8. Close add-on store, and installation will begin, then restart NVDA when prompted.

Testing the add-on simply involves using NVDA as usual. If you do encounter issues:

1. Restart NVDA with add-ons disabled.
2. Enable one add-on at a time to make sure the issue is not related to add-ons other than Windows App Essentials.
3. If the issue occurs after enabling Windows App Essentials, note the steps to reproduce the issue.
4. Use GitHub and submit a new issue (https://github.com/josephsl/wintenapps/issues/new). Be sure to include NVDA version, add-on version, Windows version, and steps to reproduce the problem.
5. Sometimes the author will ask for a debug log. If so, restart NvDA with debug logging enabled, try reproducing the issue, then either attach the debug log as part of the GitHub issue or copy and paste the relevant log fragment from the log viewer (NVDA+F1).

### Localizing add-on documentation and messages

You must do this through NVDA translations workflow (Crowdin), not through pull requests.

### Offering code and pull requests

#### Windows release requirement

To contribute code and pull requests, you must use latest stable Windows 11 (24H2) release or Windows Insider build.

#### Coding style

Windows App Essentials follows NVDA's own coding style (tabs for indentation, camel case, etc.). Although you don't have to, please align closely to NVDA's own coding style.

#### Pull request process

1. If you want, create a new issue on GitHub proposing specific changes. This is so that more people can discuss changes.
2. Create an accompanying pull request via GitHub (be sure to fork the add-on source code before doing so). Unless otherwise noted, pull request base branch should be "main" and each pull request must be done from a different branch.
3. In the pull request comment, describe the pull request, including applicable Windows releases (if any) such as whether the pull request addresses issues with a specific build range.
4. It can take up to 48 hours for the pull request to be reviewed and a decision made. Depending on the severity of the issue, it can be included in the next version of the add-on or delayed for the next milestone release.

## Additional notes

### Support duration

A given Windows App Essentials release is supported until the next version is released. For development snapshots, only the latest build is supported. A stable version is supported until the next stable version is released. Both major (milestone) and minor (backports and localizations) are grouped under stable versions.

For NVDA releases, Windows App Essentials supports latest NVDA releases, including development builds. Unless noted otherwise, the immediate past stable NVDA release is also supported. As of September 2025, Windows App Essentials supports NVDA 2025.3 (latest stable) and alpha snapshots.

For Windows releases, a stable Windows release (typically a feature update) is supported for at least 12 months and no more than consumer support duration (typically two years). Although the add-on will indicate support for a Windows release (or a feature update) months in advance, official support begins the moment a given release is made available to the general public. For example, although Windows 10 November 2021 Update was marked as supported since August 2021, official support duration is from November 2021 to at least December 2022 and no later than June 2023. For Windows 11 2023 Update, preview (and experimental) support began in July 2023, and official support duration is from October 2023 to at least April 2025 and no later than November 2025. As a rule of thumb, Windows App Essentials uses consumer (Home, Pro, Pro for Workstations) support duration for a feature update to determine support duration. See release information page from Microsoft for details on support duration for Windows releases, and see below for support duration for Windows releases across add-on releases.

Regarding end of support for a Windows release from the add-on, for stable Windows releases, support duration is tied to consumer support. Prior to end of support, a grace period (at least 30 days) will be given to let users upgrade to newer releases (for Windows 11 original release, support from the add-on ended in August 2023, and the grace period was from June 2023 to August 2023). For Windows Insiders, only the latest Insider Preview build is supported, particularly if using canary and dev channel builds. Consequently, there is no concept of grace period from the add-on for Windows Insider Preview builds.

Note: until July 2025, the only exception to support duration policy was the very last Windows 10 feature update (2022 Update/Version 22H2), which was supported until October 2025 (official support until August 2025 followed by 60-day grace period; no support for extended security updates). Subsequently, Windows 11 24H2 and 25H2 were added as support for these releases depend on overall add-on maintenance duration (24H2 support did meet the minimum support duration requirement).

#### Supported Windows releases

For each Windows release, Windows App Essentials provides support for at least twelve months (18 months for Windows 11) and up to end of consumer support (18 months for Windows 10, two years for Windows 11) except Windows Insider Preview where the add-on supports latest build. Windows Server support duration is tied to client releases (for example, Windows Server 2025 support duration is tied to Windows 11 Version 24H2) whether or not client and server releases have the same build. Windows Enterprise LTSC (long-term servicing channel), as well as Windows Server Core and semi-annual and annual container channel server releases are not supported.

Note: support duration also depends on add-on maintenance - duration can be shortened if the add-on becomes unsupported prior to end of consumer support for a Windows release.

##### Windows 10

* Version 1507 (build 10240): September 2015-November 2016
* Version 1511 (build 10586): December 2015-June 2017
* Version 1607 and Windows Server 2016 (build 14393): July 2016-December 2017
* Version 1703 (build 15063): March 2017-June 2018
* Version 1709 (build 16299): August 2017-January 2019
* Version 1803 (build 17134): March 2018-July 2019
* Version 1809 and Windows Server 2019 (build 17763): September 2018-January 2020
* Version 1903 (build 18362): March 2019-June 2020
* Version 1909 (build 18363): August 2019-January 2021
* Version 2004 (build 19041): February 2020-July 2021
* Version 20H2 (build 19042): August 2020-January 2022
* Version 21H1 (build 19043): March 2021-August 2022
* Version 21H2 and Windows Server 2022 (build 19044/Windows 10, 20348/Server 2022): August 2021-May 2023
* Version 22H2/final (build 19045): August 2022-October 2025

##### Windows 11

* Version 21H2 (build 22000): October 2021-July 2023
* Version 22H2 (build 22621): July 2022-August 2024
* Version 23H2 (build 22631): July 2023-July 2025
* Version 24H2 and Windows Server 2025 (build 26100): April 2024-October 2025
* Version 25H2 (build 26200): July 2025-October 2025

### Development process and milestone releases

Windows App Essentials uses continuous, iterative development process. This means a given feature or a change can take up to several weeks to months to be implemented and refined based on user feedback (this can take several milestones), along with being sensitive to changes to NVDA, Windows, and apps. To facilitate this, development snapshots are released whenever changes are made to the add-on source code and data, including when localizations are updated.

For project management, the add-on uses "development milestones" lasting between six months to a year. These milestones, named after a chemical element to align with Windows development cycle, are further divided into "development quarters" lasting about three months each. These quarterly releases are termed "milestone" or major releases dedicated to a specific theme or activity such as adding or dropping support for Windows and/or NVDA releases. One or more minor releases, consisting of backports from the next development quarter and responding to changes in Windows and apps, can be released between milestone releases, typically on a monthly basis. Localization updates can also trigger minor releases.

The main development branch is named "main". This branch holds code for the upcoming milestone release. Although quality may vary, the aim is to house code that can ship as a stable version at anytime and can be backported to maintenance branches easily.

At least two weeks prior to end of a milestone, code from the main branch is merged into a release branch (currently named "stable"). This is so localization data exchange can take place (to help people localize new messages if any) and to prepare the add-on for a stable release through additional testing. For minor releases, the release branch (named after the development quarter) includes latest stable branch changes and backports from upcoming milestone that does not involve major code rewrites (major rewrites are reserved for milestone releases), along with localization updates if any.

#### Recent and upcoming development milestones and quarters

Originally development semesters in 2021 but changed to annual milestones in 2022, then reverted to semesters in 2024.

* Nickel (2021):
	* Nickel 1: June 2021 to September 2021, dedicated to refining Windows 11 support and introduction of control types refactor from NVDA 2021.2
	* Nickel 2: September 2021 to January 2022, refinements to Windows 11 support and end of support for Windows 10 October 2020 Update (Version 20H2)
* Copper (2022):
	* Copper 1: December 2021 to March 2022, NVDA 2021.3 and 2022.1 support, removing deprecated features, and changes from Insider Preview builds
	* Copper 2: March 2022 to June 2022, Windows 11 Version 22H2 preview, Windows 10 installation message preview, Voice Access, Windows 11 UI navigation
	* Copper 3: May 2022 to September 2022, official support for Windows 10 and 11 Version 22H2, end of support for Windows 10 May 2021 Update (Version 21H1), changes to installation mechanics and support message for Windows 11 releases, NVDA 2022.2 requirement, drag and dropt target announcement
	* Copper 4: August 2022 to January 2023, Windows 11 Search Highlights, Suggested Actions, installation message changes, removing detection for old Windows releases, NVDA 2022.4 requirement
* Zinc (2023):
	* Zinc 1: December 2022 to March 2023, Windows apps optimizations, removed 'no more weather data' message from Weather app, type information
	* Zinc 2: February 2023 to June 2023, end of support for Windows 10 November 2021 Update and Server 2022 (Version 21H2), reimagined virtual desktops announcement internals, Weather app changes, NVDA 2023.1 requirement, some Windows 10 workarounds removed
	* Zinc 3: May 2023 to October 2023, end of support for Windows 11 original release (Version 21H2), NVDA 2023.2 requirement, removed Cortana support
	* Zinc 4: September 2023 to January 2024, restructuring Settings app support in preparation for freezing Windows 10 support code, NVDA 2023.3 requirement, removed Voice Access support, initial support for NVDA 2024.1
* Gallium/Germanium/Arsenic (2024):
	* Gallium 1: December 2023 to April 2024, official support for Windows 11 Version 24H2, revert to older installation error message, no more dictation/voice typing detection in modern keyboard, restructured install tasks, refactored modern keyboard window open event handler
	* Gallium 2: March 2024 to June 2024, NVDA 2024.1 requirement, deprecate 32-bit Windows 10 support, Windows 11 Windows Update status update announcement removed, reorganized modern keyboard support and added dedicated overlay class for navigation menu items
	* Germanium: May 2024 to September 2024, NVDA 2024.2 requirement, end of support for Windows 11 2022 Update (Version 22H2) and 32-bit Windows 10, restructured install tasks, WinApps global plugin no longer included in add-on installation package (remains in source code repo), Ruff replaces Flake8 as linter, minimal readme with removal of app support notes, resolve live region change event handling in modern keyboard
	* Arsenic: August 2024 to January 2025, NVDA 2024.3.1 and 2024.4.1 requirements, initial support for NVDA 2025.1, minimum Windows version detection routine rewrite to emphasize Windows 11, reformatted add-on module contents using Ruff, transferred wiki docs to main repo, support for Copilot WebView2 app
* Selenium (2025):
	* Selenium 1: December 2024 to April 2025, Windows 11 is required to contribute to add-on development, removed Settings app module with the removal of Windows 10 Windows Update live region change workaround, restore WinApps global plugin to handle WinUI 3 top-level window UIA reclassification across apps to enable mouse and touch navigation
	* Selenium 2: March 2025 to August 2025, NVDA 2025.1 requirement, end of support for Windows 11 2023 Update (Version 23H2), UIA notification event handling for elements without native window handle set, reintroduced Voice Access support, go to line control reclassification in Notepad, removed Copilot WebView2 and modern keyboard app modules, removed WinUI 3 app mouse and touch navigation workaround
	* Selenium 3 (final ad-on development milestone): June 2025 to October 2025, NVDA 2025.2/2025.3 requirement, end of support for Windows 10 series (Version 22H2), brief support for Windows 11 25H2, freezing localization data, add-on contents (most of global plugin content and app modules) removed as NVDA 2025.2 includes them
