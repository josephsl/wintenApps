# Contributing to Windows App Essentials NVDA add-on

Thank you for your interest in contributing to Windows App Essentials NVDA add-on. The purpose of this document is to outline the overall add-on contribution requirements, development process, and offer tips when contributing.

## Important notes

Before reading further, please read this section to better understand specifics about this add-on:

1. This add-on is optimized for recent releases of Windows 10 and later. As such, safeguards are in place to prevent installation on older Windows releases such as 8.1. Put it the other way, in order to contribute, you must be running Windows 10 and later (collectively called "modern Windows" in some places), specifically supported Windows releases (see Windows Release Information page offered by Microsoft for a list of supported Windows releases).
2. This add-on is optimized for recent NVDA releases and is sensitive to it. From time to time the add-on drops support for older NVDA releases in order to take advantage of changes introduced in newer NVDA releases. For effective contributions, you should use latest stable version of NVDA and/or latest alpha/beta/release candidate builds.
3. Occasionally you may need to use other add-ons and/or tools in addition to the add-on. When debugging event handling, you must use either Event Tracker add-on or AccEvent from Windows Software Development Kit (SDK).
4. This add-on does not replace the need to contact app developers. Although the add-on can cover accessibility issues with apps (or you can contribute fixes for apps in regards to accessibility issues such as incorrect labels), ideal fixes should come from vendors themselves.

## Ways to contribute

You can contribute to Windows App Essentials in a number of ways:

1. Testing: provided that you are using supported Windows releases (including latest Windows Insider Preview build) with latest NVDA and the add-on installed, you can help improve the add-on by testing and reporting feedback.
2. Localization: you can translate add-on documentation and messages via NVDA translations workflow. The author (Joseph Lee) does not take pull requests involving localization data.
3. Issues and pull requests: the author welcomes issues and pull requests submitted via GitHub (see the section on issues and pull requests for more information).

## Contribution requirements

You must:

1. Be running the latest supported version of Windows 10 and later (as of August 2021, this means Windows 10 May 2021 Update (Version 21H1), Windows 11 preview, and latest Insider Preview build).
2. Be running the latest stable version of NVDA or later (as of August 2021, this means NVDA 2021.1 or latest alpha release).
3. If you wish to offer pull requests, you must be running latest NVDA stable version or later.

## Contribution process

### Testing the add-on

You can contribute by testing the add-on. To facilitate this, a development snapshot of this add-on is released from time to time so people can test latest changes.

To test the add-on, you must be running the latest stable or development build of Windows App Essentials, latest stable or development build of NVDA, and Add-on Updater (Add-on Updater is needed to download Windows App Essentials add-on updates). For effective testing, you must also be running latest Windows release (public release or latest Insider Preview build).

Before testing the add-on:

1. Install Add-on Updater add-on from community add-ons website (https://addons.nvda-project.org).
2. Open NVDA menu/Preferences/Settings, then select Add-on Updater.
3. Select Windows App Essentials from "Prefer development releases" list and click OK.
4. Restart NvDA, and Add-on Updater will offer the latest Windows App Essentials development snapshot (typically the version will be of the form "YYYYMMDD-dev").
5. Install the offered development snapshot and restart NVDA.

Testing the add-on simply involves using NVDA as usual. If you do encounter issues:

1. Restart NVDA with add-ons disabled.
2. Enable one add-on at a time to make sure the issue is not related to add-ons other than Windows App Essentials.
3. If the issue occurs after enabling Windows App Essentials, note steps to reproduce the issue.
4. Use GitHub and submit a new issue (https://github.com/josephsl/wintenapps/issues/new). Be sure to include NVDA version, add-on version, Windows version, and steps to reproduce the problem.
5. Sometimes the author will ask for a debug log. If so, restart NvDA with debug logging enabled, try reproducing the issue, then either attach the debug log as part of the GitHub issue or copy and paste the relevant log fragment from the log viewer (NVDA+F1).

### Localizing add-on documentation and messages

You must do this through NVDA translations workflow, not through pull requests.

### Offering pull requests

#### Coding style

Windows App Essentials follows NVDA's own coding style (tabs for indentation, camel case, etc.). Although you don't have to, please align closely to NVDA's own coding style.

#### Pull request process

1. If you want, create a new issue on GitHub proposing specific changes. This is so that more people can discuss changes.
2. Create an accompanying pull request via GitHub (be sure to fork the add-on source code before doing so). Unless otherwise noted, pull request base branch should be "main".
3. In the pull request comment, describe the pull request, including applicable Windows releases (if any) such as whether the pull request addresses issues with a specific build range.
4. It can take up to 24 hours for the pull request to be reviewed and a decision is made. Depending on the severity of the issue, it can be included in the next version of the add-on or delayed for the next milestone release.

## Additional notes

### Support duration

A given Windows App Essentials release is supported until the next version is released. For development snapshots, only the latest build is supported. A stable version is supported until the next stable version is released. Both major (milestone) and minor (backports and localizations) are grouped under stable versions.

For NVDA releases, Windows App Essentials supports latest NVDA releases, including development builds. Unless noted otherwise, the immediate past stable NVDA release is also supported. As of August 2021, Windows App Essentials supports NVDA 2020.4, 2021.1, and alpha snapshots.

For Windows releases, a stable Windows release (typically a feature update) is supported for at least 12 months (18 months for Windows 11 releases). Although the add-on will indicate support for a Windows release (or a feature update) months in advance, official support begins the moment a given release is made available to the general public. For example, although Windows 10 May 2021 Update was marked as supported since February 2021, official support duration is from May 2021 to at least June 2022. For Windows Insiders, only the latest Insider Preview build is supported, particularly if using dev channel builds.

### Development process and milestone releases

Windows App Essentials uses continuous, iterative development process. This means a given feature or a change can take up to several weeks to months to be implemented and refined based on user feedback (this can take several milestones), along with being sensitive to changes to NVDA, Windows, and apps. To facilitate this, development snapshots are released whenever changes are made to the add-on source code and data, including when localizations are updated.

For project management, the add-on uses "development semesters" lasting about six months. These semesters, named after a chemical element to align with Windows development cycle, are further divided into "development quarters" lasting about three months each. These quarterly releases are termed "milestone" or major releases dedicated to a specific theme or activity such as adding or dropping support for Windows and/or NVDA releases. One or more minor releases, consisting of backports from the next development quarter and responding to changes in Windows and apps, can be released between milestone releases, typically on a monthly basis. Localization updates can also trigger minor releases.

The main development branch is named "main". This branch holds code for the upcoming milestone release. Although quality may vary, the aim is to house code that can ship as a stable version at anytime and can be backported to maintenance branches easily.

At least two weeks prior to end of a milestone, code from the main branch is merged into a release branch (currently named "stable"). This is so localization data exchange can take place (to help people localize new messages if any) and to prepare the add-on for a stable release through additional testing. For minor releases, the release branch (named after the development quarter) includes latest stable branch changes and backports from upcoming milestone that does not involve major code rewrites (major rewrites are reserved for milestone releases), along with localization updates if any.

#### Upcoming development semesters and quarters

* Nickel:
	* Nickel 1: June 2021 to September 2021, dedicated to refining Windows 11 support and introduction of control types refactor from NVDA 2021.2
	* Nickel 2: September 2021 to December 2021 at the earliest
* Copper:
	* Copper 1: December 2021 to early 2022
	* Copper 2: TBD