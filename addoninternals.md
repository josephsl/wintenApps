# NVDA Add-on internals: Windows App Essentials

Author: Joseph Lee

Revision: March 2025

Note: originally called Windows 10 App Essentials, the add-on was renamed to Windows App Essentials in 2021 with the introduction of Windows 11. Parts of this document will refer to the original add-on name or Windows 10.

## Preface

If one add-on can define my passion for NVDA, it would be Windows App Essentials, a soon to be discontinued add-on. What started out as a small app module for Insider Hub became one of the most recognizable add-ons in NVDA community, offering needed fixes and features to make Windows 10 and 11 more accessible and usable for NVDA users along with communicating accessibility needs to app developers.

When I started development of Windows App Essentials in 2015, I knew that the lifetime of the add-on was limited. While I promised to support the add-on as long as Windows Insider Program was a thing, deep down I knew that the lifetime of the add-on depended on add-on features and bug fixes being integrated into NVDA. Throughout 2024 and 2025, the last pieces of this add-on became part of NVDA, with the final parts being a bug fix for modern keyboard included in NVDA 2025.1 and global support for mouse and touch navigation in WinUI 3 apps.

Originally, I planned to support Windows 10 series until October 2025 but a fix from Microsoft in February 2025 changed this. Prior to February 2025, NVDA would be verbose when announcing update installation status in Settings app, therefore the add-on resolved it by silencing some update announcements. However, in February 2025, the live region change event responsible for announcing update status changes is no longer raised, making the workaround unnecessary. With this change, the last remaining anchor to Windows 10 (Settings app module) was removed in February 2025, but to fulfill the promise to support it until its end of life, Windows 10 support will be kept in install tasks module (checking minimum supported Windows version) until late 2025.

The upcoming Windows 10 end of life and my current status as an up and coming researcher led to the decision to discontinue the add-on in late 2025. I felt bittersweet when announcing my decision in 2024, knowing that there was no other add-on like it where I can pour out my advocacy skills through programming. However, I knew that add-on development can become a distraction as I learn to practice research, so I decided to take the necessary step to wind down this activity. Although the add-on is fading into history in 2025, I still dream of accessible apps and opportunities to advocate for it in different forms.

As a software engineer and a communication studies researcher, I take documentation seriously, more so now that I'm documenting a project that defined my engineering and scholarly identity. When reading add-on source code and browse Git commit log, one may notice tons of comments sprinkled throughout the code base and detailed collection of commit messages narrating a story filled with wide range of emotions and thoughts. The below add-on internals document is an extension of my thought process - I wrote the documentation below not only for myself, but also to serve as an artifact for future coders and researchers wishing to know the history of Windows 10/11 accessibility and advocacy that went into it. Although the add-on itself is being phased out, its code and documentation lives on, with the former being part of a project and a community that champions equal access to technology: NonVisual Desktop Access.

## Introduction

Supporting new technologies can be fun and challenging, especially a new operating system version that changes how people perform certain tasks and introduces new ways of keeping up with changes. This is more so when it comes to letting screen readers support new operating systems such as Windows 10 and 11, which brings new ways of interacting with a computer, new set of apps and technologies, and accessibility improvements and challenges. NVDA includes solid support for Windows 10 (support may vary on newer releases), including Microsoft Edge, the new Start menu, navigation in universal apps, emoji panel and so on, all made possible thanks to collaboration between users, Microsoft, NV Access and others, part of which involves the add-on we will meet in this article.

In NVDA Add-on Internals: Windows App Essentials, we'll look at how this add-on came about, how it works, its development, and go over recommendations from the add-on author (me) regarding accessibility practices. You'll also glimpse how UI Automation works at a high level, how features start out as an add-on component and end up as an NVDA feature and so on.

To download the add-on, visit NV Access add-on store. The source code for this add-on can be found at https://github.com/josephsl/wintenApps. As Windows (10 and later, more so for Windows 11) and universal apps are UI Automation universes, it is essential that you know some things about UIA, which are covered later.

Disclaimer: Despite the article text and knowledge that's contained within, I (Joseph Lee, the add-on author) do not work for NV Access nor Microsoft.

Note: some of the features described may change as Windows and NVDA development progresses. As of April 2025 revision, features from NVDA 2025.1 preview and recent Windows Insider Preview builds are documented for reference purposes. Also, when refering to Windows releases (in particularly, Windows 10 feature updates), release Id (YYMM/YYHn) is used instead of using marketing label unless specified (for example, 1709 instead of Fall Creators Update, or 20H2 instead of 2009). To account for Windows 11, releases will be denoted as "Windows release YYMM/YYHn" e.g. Windows 10 21H1 for Windows 10 May 2021 Update or Windows 11 24H2 for Windows 11 2024 Update.

Copyright: Microsoft Windows, Windows API, UI Automation, Microsoft Edge, Universal Windows Platform (UWP) and related technologies are copyright Microsoft Corporation. NVDA is copyright NV Access. Windows App Essentials add-on is copyright 2015-2025 Joseph Lee and contributors, released under GPL 2.

## Windows releases and Windows App Essentials

The first version of Windows was 1.01, released in 1985. Over time, Microsoft released familiar Windows releases such as 95, 2000, XP, Vista, 7, 8, 10, 11, and so on. Each release took years to develop - five years for Windows Vista, three years for Windows 7, and almost two years for initial Windows 11 version (21H2).

What I would call the modern Windows began with Windows 10 with the introduction of Windows as a Service (WaaS) where major updates are developed months at a time in collaboration with Windows Insiders. For example, it took Microsoft about five months (June to October 2015) to develop Windows 10 1511 (November Update). Internally, a given Windows release takes more time to develop (up to a year or more), with quality checks done by Microsoft and feedback from Windows Insiders deciding which features will appear for the general public. This practice continues in Windows 11, and so does my work on championing accessibility, especially when it comes to making sure third-party universal apps are usable by many, supporting features such as modern input facility and so on.

Originally, Windows App Essentials supported Windows 10 only, hence the original name (Windows 10 App Essentials). This became an issue in June 2021 when Microsoft introduced Windows 11. Despite being called Windows 11, it is still powered by Windows 10 technologies, as evidenced by the system version being 10.0, the same as Windows 10 releases. As a result, the need to expand the add-on to support Windows 11 and future Windows releases became a high priority, and as part of this change, "10" was dropped from add-on name in June 2021. To acknowledge its origins and since Windows system version is 10.0 across Windows releases from 10 onwards (unless this changes), parts of the add-on and this internal article will refer to Windows 10 App Essentials (WinTenApps for short) where context matters.

### Windows 10

Windows 10 is the "last major" version of Windows... or was promoted as such until Windows 11 debuted in 2021. It introduced a completely new way of keeping track of changes through Windows Insider Program and Windows as a Service (WaaS, a fancy term for continuous delivery), new application development framework, unification strategy in terms of user experience across devices and a new web browser. In addition, it featured the return of an older style of Start menu, virtual desktops, Action Center to centralize notifications, a way to run command-line Linux utilities, and refinements to Narrator, the built-in screen reader. Microsoft announced in April 2023 that Windows 10 will have its own last version, 22H2, to be supported until October 2025.

Windows 10 made its maiden flight in October 2014. Back then, it was called Windows Technical Preview, and after several weeks, it was renamed to Windows Insider Preview. Between October 2014 and July 2015 when Windows 10 Version 1507 (build 10240) shipped, more than five million users became Windows Insiders, testing new builds and apps, submitting feedback and so on.

I call the October 2014 preview (build 9841) a maiden flight for several reasons. First, this is the first time where Microsoft did show interest in user-level feedback. Although betas existed for earlier versions such as Windows 7 and 8.1, Windows 10 is the first attempt from Microsoft at connecting with users and taking comments seriously. Second, build 9841 (the first Insider Preview build) hailed the start of Windows as a Service, a completely different approach to upgrading Windows where Microsoft wanted to provide two things: continuous delivery and feedback loop, and a unified configuration that works well with most devices. There were setbacks such as privacy concerns due to telemetry and data losses in October 2018 Update, but for the most part, Windows 10 was received positively.

There is another, more personal reason for calling October 2014 release a maiden flight: I became one of the first Windows Insiders, and due to my work on NVDA, I have decided to make sure screen reader users were treated with respect. This included sending accessibility-related feedback, getting other screen reader users onboard as Insiders, and releasing NVDA try builds that resolved important issues for Windows Insiders. This culminated in the release of Windows 10 App Essentials add-on in November 2015 (in time for Windows 10 Version 1511/build 10586 release) that provided basic support for Insider Hub (now Feedback Hub) and other workarounds, which translated to superb user experience for NVDA users when it comes to using Windows 10 and various universal apps.

### Windows 11

Windows 11 is described as the next generation of Windows. It introduced user interface tweaks, combined input experience panel where users can select from emojis and clipboard history, a revamped Store, support for Android apps distributed through Amazon Appstore (deprecated), File Explorer tabs, Windows Recall to show snapshots of user's activities with help from hardware features (if allowed), and other under the hood system tweaks. Despite its name, Windows 11's internal system version is 10.0.

Windows 11 development could be best described as a reaction to changes to Windows ecosystem around 2020. First, Microsoft announced in December 2019 that Windows Insiders on fast ring (now dev channel) wil receive builds that are not tied to upcoming Windows releases. Six months later, Windows Insiders were notified that the "Insider ring" model was being replaced by "Insider channels" that clarified the quality of a Windows build. For example, people subscribed to slow ring were redirected to beta channel where the next feature update build was released for testing in advance.

At the same tine, Microsoft was working on Windows 10 X, an operating system designed for dual screen devices. Windows 10 X was designed to be "secure by default", meaning that it will let go of legacy components that could compromise operating system security such as running classic desktop apps locally. Because Windows 10 X downplayed classic desktop apps, I and others were wondering as to how would desktop apps (in my case, screen readers) would work in this environment, with Microsoft noting that an app container will be used to run classic apps securely. But by 2021, it was clear that Windows 10 X was not ready for the world (originally designed for dual screen devices, later becoming a single screen environment), and the world was a different place than 2019 when Windows 10 X was first announced.

Most significantly, the COVID-19 (Coronavirus Disease 2019) pandemic brought changes to lives of billions. Schools shifted to remote learning, and businesses accelerated adoption of hybrid and remote work. Responding to the pandemic and its impact, coupled with the state of Windows 10 X, Microsoft suspended Windows 10 X development in early 2021 and refined it as Sun Valley, a project to improve the user interface and related tweaks. This culminated in Sun Valley being revealed as Windows 11.

The first Windows 11 Insider Preview build (22000.51) was released on June 28, 2021. The biggest difference from Windows 10 era was how the user interface was presented and coded. For example, Settings app was reorganized, and many File Explorer controls and Shell elements such as buttons on the taskbar are UIA controls. Just like old Windows 10 Insider Preview builds, accessibility regressions were found, the most significant being inability to activate items with shortcut keys in quick menu (Windows+X), resolved a few weeks later.

Just like first Windows 10 Insider Preview build (9841), build 22000 is personal. Although I was disappointed that the main add-on development machine at that time wasn't compatible with Windows 11, Windows 11 preview ran well as a virtual machine. At least this gave me a head start on bringing experimental support for Windows 11 user interface through Windows App Essentials, made easier as I have learned a lot during Windows 10 era. Many add-on snapshots were released days following the availability of the first preview build, and as of time of this writing (March 2025), Windows 11 provides a solid experience for NVDA users.

## Purposes of Windows App Essentials

Windows App Essentials add-on is built on top of four pillars:

* New features support: part of making sure screen reader users were treated with respect was showcasing new Windows features early through this NVDA add-on. These include support for really old versions of Feedback Hub app, emoji panel in Windows 10 Fall Creators Update, Settings app support in Windows 11 and so on.
* Essential features and announcements: Until early 2017, NVDA did not announce important information such as status of Windows Update installations in Settings app. This has changed significantly in 2017 (see notes on live region change event for details).
* UI Automation and accessibility workarounds: every day, new features and bug fixes are added to various universal apps or Windows itself. At the same time, there is at least one app where accessibility, particularly UI Automation, gets broken, especially during development of new Windows releases. Some of the add-on code is devoted to providing workarounds for odd UIA implementations.
* Demonstrating commitment to accessibility advocacy: some accessibility champions, including I, have recently stressed that accessibility is important in app designs, and that developers should take accessibility feedback seriously. Through workarounds and features, the add-on provides a way to demonstrate this commitment and advocacy.

There is a fifth pillar that has emerged in recent years: providing a testing ground for potential NVDA features dealing with Windows and apps. Recently, parts of this add-on have made their way to NVDA screen reader, including emoji panel support, suggestion sounds and announcements, UIA-based drag and drop announcements, reporting virtual desktop changes and others.

## Add-on contents

The Windows App Essentials add-on consists of a global plugin and app modules for various universal apps included with Windows 10 and later. The Windows App Objects (shortened to WinAppObjs), the global plugin portion of this add-on, provides foundations such as overlay classes for frequently encountered controls in Windows an universal apps. Until 2022, UIA event tracking and logger facility was also part of the add-on, replaced by Event Tracker add-on. Until 2018, the global plugin was also responsible for add-on update feature, documented here for sake of completeness. With the integration of updated dialog detection in NVDA 2024.1, the global plugin became empty until March 2025 when a global yet hacky mechanism to enable mouse and touchscreen navigation in WinUI 3 apps such as Copilot and parts of Windows 11 File Explorer was introduced.

In regards to app modules, these were included to either provide workarounds or enhance the user experience. For example, the app module for Settings app (systemsettings) allows NVDA to announce Windows Update download and installation progress, and app module for modern keyboard (windowsinternal_composableshell_experiences_textinput_inputapp) provides support for more modern input facilities such as enhanced dictation and suggested actions. We'll meet some of these app modules in subsequent sections.

### A note on feature parity with NVDA screen reader

As noted above, some features discussed in this article (such as UIA notification event handler and UIA-based drag and drop announcements) were integrated into recent NVDA releases. I will point out some of these, as well as provide how these were integrated, including planning involved and some tips on modifying add-on features to fit into NVDA's code base.

### Information on add-on update feature

This article will sometimes reference add-on update feature, which is gone in 2019. Information about it is kept here for reference purposes. An add-on appropriately named "Add-on Updater" is used to update windows App Essentials and other add-ons, and with the opening of the NV Access add-on store in 2023, NVDA itself can update add-ons includin Windows App Essentials.

### Special note on feature updates support on Windows 10 and later

Windows App Essentials add-on supports a given Windows feature update (release) for at least one year and no more than end of consumer level support (Home, Pro, Pro Education, Pro for Workstations); the exception is Windows 10 22H2, the final Windows 10 feature update which will be supported until October 2025. In addition, it comes with support for features found in Windows Insider Preview (WIP) builds, including features that may not appear in subsequent feature updates.

## Fun with UI Automation

Before we dive into how the add-on works, it is helpful to understand what UIA is and wy it is important. Only then the rest of the article makes sense, as Windows (10 and later) and universal apps are UIA universes (exceptions exist, including desktop apps submitted (either converted (Windows 10) or installer (Windows 11) for distribution in Microsoft Store).

UI Automation (UIA), released in 2007, is an accessibility API based on Component Object Model (COM) that allows assistive technologies and other programs to communicate with each other regarding accessibility information about a control. In some respects, this API is a replacement for Microsoft Active Accessibility (MSAA), sometimes called IAccessible that was released in the 1990's. Being a COM-based API set, it allows programs and objects to expose essential information regardless of programming language in use as long as an object exposes documented routines that other programs can use.

In UIA world, an object on screen is termed an "element". Just like any accessibility API's, UIA exposes various elements to assistive technologies, which are termed "clients", with programs with the set elements termed "servers". These elements are organized into a UI tree, with the Windows Shell (desktop) object being the root, with tree being pruned and new leafs springing constantly whenever apps are started and closed, elements are created and destroyed, controls are shown and hidden on screen and so on.

Although UIA is meant to replace MSAA due to modernized accessibility information that can be gathered, screen reader vendors such as NV Access publishes workarounds for poor or odd UIA implementations. One such case is UIA issues in older versions of Microsoft Office, such as label problem in various combo boxes. Certain areas in Windows and universal apps still have UIA issues, such as odd or badly applied control labels, generic XAML (eXtensible Application Markup Language)/UI labels, expected events not being fired and so on. This is one of the reasons for creating Windows App Essentials add-on: to provide workarounds for issues like these.

### Automation Id and other interfaces and properties

A key piece of information UIA exposes (or attempts to gather) is Automation Identifier (Id), a string that uniquely identifies an element. For example, some search fields expose "SearchEditBox" as Automation Id, which allows screen readers such as NVDA to detect these controls. Although most controls do expose unique Automation Id's, some uses generic or auto-generated identifiers (such as update history in Settings app).

Other useful information exposed by UIA elements are:

* Class name: the class name for this control, a string that denotes the class of this element (not to be confused with Automation Id that uniquely identifies an element).
* Framework: the underlying framework used to create a given control such as XAML, Direct UI and others.
* Localized control type: a role type text that should be spoken by screen readers in different languages.
* Controller for: a list (array) of controls that this element manipulates when performing actions such as search suggestions (explained below).
* ARIA properties: a map of ARIA properties such as role description, mostly encountered in Microsoft Edge elements.
* Pattern: one or more actions the element supports or can be manipulated by users. These can include selection, drag, legacy MSAA (IAccessible) patterns and so on.

### UIA events

In addition to standard events expected from accessibility API's such as focus manipulation and object property (such as name and state) changes, UIA comes with some interesting events, including controller for, live region changed, notification and many others. Due to performance reasons, NVDA ignores certain events such as structure change and others. How NVDA and Windows App Essentials add-on deals with certain UIA events is covered later in this article.

### UIA-related additions, fixes and workarounds

The Windows App Essentials add-on includes the following additions, fixes and workarounds for UIA issues and control problems:

* Search suggestions: NVDA now plays a sound to indicate appearance of search suggestions, incorporated into NVDA 2017.3 and later expanded in 2021.3 to include suggestion count announcement. More on this below.
* Live region change announcements in various apps. In the global plugin portion, a way to define and track this event is included. As of 2022, live region change event is fully tracked by NVDA itself.
* Floating suggestions such as Emoji panel in Windows 10 1709 (Fall Creators Update) and hardware keyboard suggestions in 1803 (April 2018 Update). This has been incorporated into NVDA 2018.3 with refinements since then.
* Support for UIA notification event introduced in Windows 10 1709. This became part of NVDA in 2018.2, and refined in 2019.2 to interupt users when important notifications are pending.
* Providing more meaningful labels for certain controls such as update history in Settings/Update and Security/Windows Update, sensitive to changes in Insider Preview builds.
* Announcing tooltips from universal apps, incorporated into NVDA 2019.3.
* Recognizing dialogs powered by XAML and various frameworks. Since NVDA 2018.3, NVDA itself takes care of this in most situations, with an updated procedure introduced in NVDA 2024.1.
* Announcements on accessible (keyboard based) drag and drop if the element supports it. These include rearranging tiles in Windows 10 Start menu, reordering virtual desktops in Windows 11 task view, and other places where drag and drop operations are possible. NVDA 2022.4 and later includes drag and drop announcements powered entirely by code from this add-on.
* Reclassifying some top-level window elements as UIA to allow mouse and touch navigation in recent app releases and parts of Windows interface.

We'll meet various UIA controls and workarounds (including notable changes introduced and then removed in past releases) throughout this article.

## Windows App Objects

Windows App Essentials add-on comes with Windows App Objects (WinAppObjs; formerly Windows 10 Objects or WinTenObjs for short), a global plugin that contains definitions of common controls encountered in Windows and various universal apps. In its infancy, this global plugin was home to a variety of event handlers, overlay classes, and workarounds, but its scale has gone down significantly in 2023 when virtual desktops announcement became part of NVDA 2023.2. The scale has gone down even more in 2024 with updated dialog detection transferred to NVDA, and remained an empty module until March 2025 when a global mechanism to support mouse and touch navigation in WinUI 3 apps was introduced.

Historically, Windows App Objects global plugin included handlers for some UIA events such as virtual desktop switch announcements, search suggestions, among other things. In older add-on releases, the global plugin was also home for add-on update checks (removed in 2019) and handled more modern controls (most were transferred to NVDA in recent years).

### Source code layout

The main global plugin is housed inside winappObjs.py and is laid out thus:

1. Usual add-on header such as copyright information.
2. UIA constants not included in NVDA, including property ID's such as controller for event. Most are now part of NVDA itself.
3. Classes defining various Windows and universal app controls, including search suggestions, looping selectors and so on. As of 2023, there are no classes defined in the global plugin.
4. The actual global plugin class, consisting of overlay class finder and tracking routines for various UIA events (only available if NVDA is restarted with debug logging enabled). UIA events definition and tracking became part of Event Tracker in 2022. Prior to 2024, the class included overlay class finder for detecting UIA dialogs.

### Startup and shutdown

At startup, the add-on would determine if it must patch NVDA internals. This is used to introduce new features and changes to NVDA's behavior, most notably announcing virtual desktop switches or reclassifying some top-level windows as UIA elements. One or more functions responsible for an NVDA behavior is defined and add-on specific code is added, followed by replacing (assigning) the functions defined in NVDA with those included in the add-on. For example, event handling code from NVDA is replaced with ones defined in the add-on if running on NVDA 2023.1 as NVDA 2023.2 includes event handler changes to support virtual desktop switch announcements. This is skipped if NVDA ships with features represented by patched functions.

In the past, the startup routine did more than just patch NVDA internals if needed. Until 2019, the add-on was also responsible for extending the UIA interface, adding settings dialogs, and checking for updates. These took the bulk of startup and shutdown routines which were removed with the removal of add-on update check facility.

A crutial step performed while extending the UIA interface until 2022 is enabling missing UIA events tracking. For example, until May 2017, controller for event (an event fired by a control that depends on another control such as an edit field with search suggestions) wasn't available in NVDA screen reader, but search suggestion announcement was made possible as this add-on added this event. Similarly, UIA-based drag and drop announcements became possible after adding these events to NVDA's UIA support code via startup patching.

### Notable Windows app objects and features

Note: most features described below are part of NVDA and are documented for historical reasons.

#### Sounds to indicate appearance of search suggestions

In some edit fields such as search box in Start menu, a list of suggestions will appear while entering text. for newer implementations, UIA controller for event is raised if this happens, with different screen readers reacting differently. For example, when typing something into Start search box while using Narrator, Narrator will play a sound to indicate appearance of suggestions, while old NVDA releases will announce top suggestion.

Because I felt it would be best to let users be notified when suggestions appear and disappear (and in some respects, follow Narrator's footsteps), I have implemented code to handle search suggestions. This is divided into four components:

* One or more classes used to identify edit fields that does raise UIA controller for event and ways to identify them. The reason for using several classes for the same object is due to compatibility reasons, as older NVDA releases does not come with a search field class. These classes include two events related to controller for event:
	* `event_suggestionsOpened`: called when suggestions appear. Some controls, notably embedded Cortana search box when opening a new Sets tab, does not fire this event properly.
	* `event_suggestionsClosed`: called when suggestions disappear. There are controls that does not raise this, including Edge's address omnibar.
* A class representing the suggestion items themselves.
* A set of sounds to indicate appearance/disappearance of suggestions.
* A compatibility layer for old and upcoming NVDA releases as noted above.

In addition, in some cases, it is helpful to announce how many suggestions have appeared, thus a routine has been added to announce this. With this added, the complete picture is as follows:

1. User types text into a search field.
2. NVDA will notice controller for event and will look for suggestions list. If such a list is found, NVDA will play the suggestion sound by raising suggestions opened event.
3. If suggestions are found, it'll announce the top suggestion or suggestion count. The former is for Start menu, while the latter is for other edit fields. The latter is done through UIA layout invalidated event.
4. One can then use up or down arrow keys to move through suggestions, then press Enter to select or Escape to close suggestions list. When closing suggestions list, NVDA will play suggestions close sound.

Since NVDA 2017.3, suggestion announcement is part of the screen reader, with suggestion count announcement becoming part of NVDA in 2021.3.

Note that the routines described above was done at a time when it was desirable to detect all possible search fields. However, it was found that some workarounds were app specific, thus in June 2019, it was decided to transfer some search field handling to app modules. This is especially the case with address omnibar in legacy Microsoft Edge (EdgeHTML version) where the global plugin’s suggestions closed event handler did not apply if Edge is in use. Along the way, handling rarely used search fields that appeared in one or two apps (such as People app search field in old app releases) were dropped.

#### Announcing notifications

Windows 10 1709 (Fall Creators Update) introduces a new event to let apps send text to be announced by UIA clients such as NVDA. One of the jobs of Windows App Objects is to catch this and announce notifications for NVDA releases which does not support this natively.

Because old NVDA releases do not support the new notification event natively, a trick is included with the add-on to allow NVDA to detect and handle notifications. This is done by extending UIA support subsystem through an internal module that takes over the NVDA's own routines. Among other things, this extended subsystem includes definitions for UIA notification event handler, and this subsystem takes over if NVDA 2018.1.x is running on Windows 10 1709 and later.

The notification event handler takes five keyword arguments:

* Sender: the UIA element that raised the event.
* Notification kind: the kind of notification.
* Notification processing: how NVDA should process incoming notification.
* Display string: notification text.
* Activity Id: the unique identifier for the notification.

As of October 2018, NVDA itself announces notifications for all apps (especially for the currently active app) except one or two apps where this would cause issues, thus the add-on is no longer involved in announcing many notifications except those that could cause issues.

#### Tracking UIA events for controls

Until 2022, Windows App Objects global plugin had ability to track UIA events for controls and log info about them, executed via `uiaDebugLogging` function that takes an object and the event name. This function recorded the following if NVDA is started with debug logging enabled or told to monitor specific events and/or events from specific apps:

* What the object actually is.
* Object name.
* Name of the event being logged.
* App where the control can be found (specifically, the app module).
* Automation Id if possible.
* UIA class name.
* For controller for event, the list of objects the given control depends on.
* For tooltip open event, the GUI framework that powers the element.
* For item status event, new item status text.
* For state change event, current element state.

For notification events, NVDA records event parameters from the event handler method itself. The bulk of event tracking routine was split into an appropriately named Event Tracker add-on in 2021, with the add-on level event logging removed in 2022 in favor of letting individual events record debugging information. The latter change, too became part of Event Tracker in late 2022.

#### Looping selectors

A looping selector is a combo box-like control where the selection loops around. This is employed in places such as Alarms and Clock, Settings/Update and Security/Windows Update/active hours and so on.

In older Windows 10 and universal app releases, when changing selector values, item selected UIA event wasn't fired. To get around this, the add-on will examine states for each item and announce if an item has selected state. This isn't the case for newer implementations, but for backward compatibility, the old routines are kept. This has been enhanced in NVDA 2019.1, and since June 2019, the add-on is no longer involved in keeping an eye on this control as NVDA supports it natively.

#### Live region change events

Some controls are live regions - that is, a control whose content denotes live text, such as progress of something, alerts and so on. Because of odd live region change event implementations, older NVDA releases does not support this event natively, but NVDA 2017.3 and later includes a trivial implementation where NVDA will announce the live region text i.e. object name.

The Windows App Objects goes one step further by recording instances of this event and providing workarounds for specific cases. These include announcing correct text for Edge alerts (see below), preventing repeat announcements in some apps and so on.

As of 2022, no live region change event workaround exists in the add-on at the global plugin level (still exists at the app module level). The last remaining workaround (preventing NVDA from announcing live region from Start menu when changing screen resolution) is no longer needed in newer Windows 10 and 11 releases.

#### Recognizing various dialogs

Despite not being identified as such, some windows are actually dialogs. These include pop-up dialog for uninstaling apps, various dialogs found in Settings app and so on.

In old add-on releases, NVDA would consult a list of known dialog class names in hopes of catching a dialog. In newer releases, especially if run on Windows 10 1809 and later, UIA IsDialog property is used to catch dialog elements. Once dialogs are recognized, NVDA will read contents of these dialogs automatically when they appear. This has been simplified in NVDA 2018.3 as NVDA itself will try its best to recognize more dialogs, including those marked as a dialog via UIA in Windows 10 1809. However, there are windows that are actually dialogs, so the add-on still ships with a list of known dialog classes to be consulted by NVDA.

As of 2024, the updated dialog detection routine was the only task of the global plugin. This became part of NVDA 2024.1, making the global plugin redundant until top-level reclassification mechanism arrived in 2025 (documented below).

#### Drag and drop events

Some controls allow dragging and dropping items using keyboard commands. This is used when rearranging Start menu tiles, moving Action Center items around, and reordering virtual desktops and taskbar items in Windows 11. This is done by pressing Alt+Shift+left or right arrow keys.

Except for taskbar item reordering, the controls listed above raise UIA drag and drop events, equivalent to mouse drag/drop events. Up to six UIA events and six properties are defined to notify UIA clients such as NVDA when drag or drop operation starts, is happening, or items were dragged or dropped, as well as announcing drag and drop effects. Of these, NVDA listens to the following events to announce new location of the just dragged item:

* Drag start: raised by the item itself when it is about to be dragged somewhere.
* Drag cancel: raised by the item itself when drag operation is somehow canceled.
* Drag complete: raised by the item itself when it is dragged somewhere.

The drag start/cancel/complete events are mapped to state change events as these cause the item to be dragged to set "is grabbed" property flag (set to True while the item is being dragged). An additional property, "grabbed items", is used if dragging and dropping multiple items at once. While items are being dragged, drag drop effect(s) property (effect and effects properties, that is) is used to record effect(s) of dragging the current item to somewhere.

In addition, UIA defines the following events not tracked by NVDA:

* Drop target enter: a container such as a list notifies UIA clients if the item about to be dragged enters a target area.
* Drop target leave: a container such as a list notifies UIA clients if the dragged item leaves the target area.
* Drop target dropped: a container such as a list notifies UIA clients if an item inside it is dragged to the target position.

But NVDA does track drop target effect(s) property (effect and effects properties, that is) as the effect(s) text describes where the dragged item is going while being dragged. Unlike drag drop effect(s) property, drop target effect(s) text comes from the drop target (element that allows an item to be dragged), not by the dragged item itself.

The keyboard based drag and drop announcements became part of NVDA 2022.4.

#### Reporting virtual desktop names

One of Windows 10's highlights is virtual desktops. This is used to group various application windows into "virtual desktops" so one can "switch" between them by switching virtual desktops. Newer Windows 10 and 11 releases added improvements such as renaming virtual desktops and reordering them.

While older Windows 10 releases do provide a way to query currently active virtual desktop, it wasn't until Windows 10 1703 (Creators Update) that virtual desktop name reporting became more efficient for screen readers other than Narrator. This is done through CSRSS (client/server runtime subsystem), sometimes known as Windows subsystem process in Microsoft documentation, with it raising a name change event whenever virtual desktops are created, changed, and closed. Newer Windows 10 and 11 releases brought visible and internal changes, the most significant being internal changes for Windows desktop representation introduced in Windows 10 1903, and Windows Insider builds in 2023 brought a different approach to virtual desktop reporting as explained below.

Depending on Windows release, the following happens when virtual desktops are created (Control+Windows+D), switched to (Control+Windows+left/right arrows, and closed (Control+Windows+F4):

* Windows 10 1703 to 11 22H2: as soon as virtual desktop commands are pressed, CSRSS sends a name change event.
* Windows Insider preview: UIA notification event is raised by File Explorer to report virtual desktop name as display string.

Windows App Essentials added support for properly announcing virtual desktop names in 2018. Initially it began as a name change event handler defined in the global plugin because it wasn't known until later that virtual desktop name changes are raised only by CSRSS. Once this fact became clear, the name change event handler in question became basis for CSRSS app module, responsible for announcing virtual desktop names after a short delay.

Meanwhile, announcing virtual desktop names without using an add-on became a top priority for me and other NVDA developers. At least two pull requests were submitted, designed to bring this add-on feature to NVDA itself. In 2023, one such pull request was merged: one of my pull requests, incorporating ideas from an earlier work by Jamie Teh (Mozilla). The idea is to handle virtual desktop change event just prior to announcing focus changes whenever virtual desktops are created, changed, and removed, requiring edits to event handler's focus change handling routine in NVDA. With this change, whenever CSRSS raises name change event, the new virtual desktop name is stored in a private variable inside event handler, which is then announced between foreground and focus changes. Because virtual desktops can be created while focused on the desktop, a timer is provided to announce virtual desktop names after a short delay if not handled as part of focus change event handler. To align the add-on with NVDA changes, I made changes in early 2023 to move CSRSS name change event handler back to the global plugin in order to let the event be handled prior to focus events, similar to Jamie's pull request. The new routine is now part of NVDA 2023.2, and with that, a major feature of Windows App Essentials became part of NVDA.

#### Mouse and touch navigation in recent apps through top-level window reclassification

NVDA supports navigation via keyboard, braille hardware, mouse, and touch. While NVDA started out as a keyboard-focused screen reader, recent releases has improved support for mouse users, and since 2012, touchscreen access. In particular, touchscreen access has gained momentum through smartphones in early 2010's, and since the release of Windows 8 in 2012, Microsoft and app vendors are taking touch features more seriously.

When the first version of Windows App Essentials was released in 2015, mouse and touch interaction was not considered as NVDA users can access Windows 10 apps with mouse and touch without problems. However, Windows 11 brought changes to the user interface that broke mouse and touch navigation, and this change is affecting Windows 10 users with recent app releases such as Copilot powered by WinUI 3 framework. To resolve this, Windows App Essentials implemented top-level window reclassification strategy since 2022, with initial work done in app modules and then brought to the global plugin in 2025.

In recent apps, especially apps written with WinUI 3 framework including parts of Windows 11 interface, top-level windows are seen as Microsoft Active Accessibility (MSAA)/IAccessible elements whereas the rest of the app is a collection of UIA elements. This arrangement poses no issues for keyboard access but breaks mouse and touch interaction. This was resolved by reclassifying top-level windows as UIA elements, allowing the entierty of the affected app to become a UIA element collection, allowing mouse and touch interaction to work.

Initially, this strategy was implemented in app modules via isGoodUIAWindow app module method, taking a window handle, comparing the window class name to a known top-level class name, then forcing NVDA to accept the affected window as a UIA element (returning true). This approach was used to resolve mouse and touch navigation in parts of Windows 11 interface including Windows 11 24H2 quick settings, but not across apps powered by WinUI 3 framework such as Copilot. Therefore, a more global strategy was implemented in 2025 by adding a known WinUI 3 top-level window class name to NVDA's good UIA window class names tuple, performed as part of the global plugin startup. With this strategy, any WinUI 3 app can be navigated with keyboard, mouse, and touch.

The global plugin strategy described above is a hack - it requires changing the internal representation of good UIA window class names collection. However, a proposal was submitted to NVDA project to allow NVDA to record the WinUI 3 framework class name as a good UIA window class name from the beginning, thereby allowing the hack strategy to be removed from the add-on. A more app centric approach is proposed in an add-on named Mouse Enhancement (not my add-on) that will force app modules for WinUI 3 and WinUI 2 apps to admit top-level window as good UIA window without resorting to patching NVDA, and the mentioned NVDA project proposal plans to combine best of both approaches.

The restoration of mouse and touch navigation in Windows 11 is one of several global plugin features that involved close collaboration with app modules, or outright transferrred to and from app modules (other notable features include virtual desktop announcements and handling live regions). As a reminder, the biggest distinction with the global plugin and app modules (discussed next) is module and feature scope - app modules are designed to work with an app or two, whereas the global plugin portion includes workarounds across apps.

## App modules for universal apps

In addition to Windows App Objects global plugin, the add-on comes with app modules designed to provide extra support for various universal apps included in Windows 10 and later. These modules include enhancers and/or fixers, broadly divided into five categories:

1. Adding extra features.
2. Supporting new technologies.
3. Announcing (or, more recently, suppressing extraneous announcement of) information in various situations.
4. Workarounds for UIA issues.
5. Respond to changes in apps, and in at least five occasions, adding aliases due to renamed executable names.

Historically, the following modules and enhancers/fixers were included in the add-on:

* Calculator: selectively announce calculator display.
* Calendar: suppress read-only state announcement in various controls.
* Cortana/Start menu/Windows Search (classic Cortana): suppress double announcement of suggestion result item in some cases, staying silent when user is dictating to Cortana, handling bad UIA implementations.
* Cortana/conversations (new Cortana) and Copilot (web app based): announcing text responses from Cortana or Copilot.
* Mail: table navigation commands in message list, suppress read-only announcement in email content, app alias for hxmail.exe and hxoutlook.exe (the latter for updates released in May 2017).
* Maps: play location coordinates for map items, suppress repeated live region announcements, aliases to support old and new Maps releases (the old alias, maps_windows, is gone).
* Microsoft Store: announce needed information when live region changed event is fired by some controls, aliases to support old and new Store versions (the old alias, winstore_mobile, is no more).
* Modern keyboard/text input host: support for emoji panel, dictation, hardware input suggestions, pasting clipboard items (Version 1809), Suggested Actions (Windows 11 22H2), and modern IME's, part of NVDA since 2018.3.
* MSN Weather: use up or down arrow keys to read forecast information.
* Notepad: announcing status bar content in Windows 11 Notepad.
* People: announcing first suggestion when looking for a contact.
* Settings: selectively announce various status information, provide correct labels for certain controls.
* Shell Experience Host (action center/quick settings): suppress extraneous status announcements, enable touch and mouse interaction in Windows 11 24H2 (2024 Update) quick settings.

As of March 2025, only Copilot and modern keyboard with their enhancers and fixers remain. Settings ap module was removed in February 2025 with live region change bug fix from Microsoft, and with NVDA 2025.1 (under development), contents from modern keyboard app module are part of NVDA, making the app module redundant. Therefore, the following sections describe what the add-on did in the past for the most part.

### Adding useful features in apps

The following app modules add functionality unique to NVDA and/or commands that are used to improve user experience when using apps:

* Maps (maps.py): when using object navigation to examine a map, a tone will be played to indicate where things are located on the map. This is achieved by defining a custom handler for `event_becomeNavigatorObject` that'll take the coordinates of the object (in pixels) and play a tone, essentially emulating mouse coordinate beeps in NVDA. The app module also allows users to hear new locations when using street view to navigate the map, and this is done through handlers for live region changed event.
* Mail (hxoutlook.py): when focused on messages list, one can use table navigation commands (Control+Alt+arrow keys) to review message headers. This is possible thanks to two things: headers are child objects of the message item, and because of this, `NVDAObjects.behaviors.RowWithFakeNavigation` class can be employed to add this functionality.
* MSN Weather (microsoft_msn_weather.py): this app module, contributed by Derek Riemer, allows users to use up and down arrow keys to read forecast information, achieved by calling corresponding review cursor movement commands to move by line.

#### A note about modern keyboard

Modern keyboard, sometimes called Composable Shell (windowsinternal_composableshell_experiences_textinput_inputapp.py) and nowadays called Text Input Host, is the name of the app that provides various features, including emoji panel, dictation, hardware input suggestions, listing items to be pasted from cloud clipboard and many other input related features. This is not exactly an app, but more towards a floating overlay, much akin to touch keyboard on touchscreen devices. Powering these is a redesigned touch keyboard where XAML-based touch panel (with its own process) is used.

In Windows 10 Insider Preview build 16215 and later, it is possible for users to browse and select emojis to insert in an edit field. This is done by pressing Windows+period (.) or Windows+semicolon (;). A floating panel of emoji categories and emojis will appear. One can then use arrow keys to move through emojis or Tab and Shift+Tab to cycle through categories. In build 16226, one can type emoji descriptions to narrow the emoji field.

In build 17666 and later, this panel has been redesigned. Instead of using Tab key to move between categories, one would press Tab to move between emoji grid and categories. In case of People category, pressing Tab will let you move to skin tones list where you can use arrow keys to select a skin tone, then press Tab to move to emoji grid.

Build 18305 and later brought another design change to this panel. In addition to selecting emojis, it also hosts two new grand categories named kaomoji ("face characters" in Japanese) and symbols. When one presses Tab, one will eventually reach category list with three items: emoji, kaomoji, and symbols. Just like selecting emoji categories, pressing Enter will switch the panel among these modes.

Build 18963 renamed Modern Keyboard to Text Input Host, along with bringing refined version of Input Method Editor (IME) for certain languages. For languages such as Japanese, the modern IME hosted by Text Input Host is used.

Build 20206 brought redesigned modern keyboard. Emoji panel and clipboard history were combined, along with searching for GIF's (animated images). Instead of element selected event, notification event is used to announce selected emoji and clipboard history item. It will not be until build 21296 that the redesigned emoji panel became usable, and this change is present in Windows 11 releases.

When this panel opens, a menu open event is fired by the emoji panel (File Explorer in build 18305 and later), an event NVDA does not detect for performance reasons. As items are selected, an item selected event (notification event in build 21296 and later) is fired, to which NVDA responds by walking the panel in a tree-like fashion in order to locate the item selected. The actual announcement of emoji characters depends on synthesizers; currently, recent SAPI5 and OneCore (aka SAPI Mobile) voices and Espeak nG ships with definitions of emoji characters, expanded to cover other synthesizers in NVDA 2018.4

Similar to emoji panel (or expanded input panel in build 18305 and later), in build 17025 and later, modern keyboard can also provide input suggestions. This is done by checking a new option in Settings/Devices/Typing, and activated when one presses up arrow while typing (only United States English keyboard layout is supported). Just like emoji panel, a floating window appears, and in this case, one can press left or right arrow to navigate between suggestions and press Enter to accept the offered item.

The above mechanism for selecting input suggestions is also employed when pasting items from cloud clipboard. In build 17666 and later, one can copy text and small images to the clipboard to be pasted later, and Windows will keep a history of items copied to the clipboard. When Windows+V is pressed, a list of clipboard items will be displayed, and one can use left or right arrows to select the desired item.

In NVDA 2018.3, support for all of these (modern keyboard features) plus dictation window (also part of modern keyboard) have become part of NVDA, with modern IME support coming with NVDA 2020.4. Subsequent NVDA releases brought changes from the add-on such as dictation notification and suggested actions handling. As of NVDA 2025.1, all changes from the add-on can be found in NVDA itself and the modern keyboard app module will be removed from the add-on in 2025.

### What to announce, what not to announce

It is sometimes helpful to let users know what's going on by announcing various status information, while at other times it is equally important to not announce extraneous messages. The former was the case for majority of app modules below in the past, but since mid-2017, reverse is happening more frequently.

The app modules (and for one in particular, more than an app module) in question are:

* Calculator (calculator.py): while entering calculations, entered expression will be announced via name change and notification event handlers. Because this may interfere with typed character announcement in NVDA, the calculator display will be announced only when actual results appear or when the display is cleared.
* People (peopleapp.py): NVDA will announce first suggestion when looking for a contact. Unlike other search fields, there is no controller for event. However, the suggestion raises item selected event.
* Cortana (searchui.py)/new Start menu and Windows Search experience (searchapp.py in Windows 10, searchhost.py in Windows 11): classic Cortana uses name change events and specific Automation Id's to convey text messages. Name change event is also employed when Cortana tries to understand the text a user is dictating, which in old releases of the add-on meant NVDA would announce gibberish, subsequently resolved in later add-on releases. In recent Windows 10 releases, due to Windows Search redesign (which also involve changing executable for Windows Search to searchapp), search box content instead of result details is announced, or if results are announced, they are announced twice.
* Cortana conversations (cortana.py): similar to classic Cortana, Cortana's responses are announced.
* Copilot (copilotnative.py): a WebView2 implementation of Microsoft Copilot, live region based textual responses are reported. Unlike other aps, an IAccessible (MSAA) event is handled.
* Settings (systemsettings.py): NVDA will announce messages such as Windows Update notifications, and this is done through live region changed event (name change event in older add-on releases).
* Microsoft Store (winstore_app.py): just like Settings app, status messages are announced, this time dealing with product downloads such as apps and multimedia content. This is applicable in Store version 1 (old Windows 10 releases) ae version 2 (Windows 11 and newer Windows 10 releases) does a better job of letting NVDA announce download progress.
* Notepad (notepad.py): in Windows 11, Notepad is updated through Microsoft Store, thus changes can happen more frequently. This is more so with Notepad adopting Windows 11 look and feel, with a problem being inability to announce certain screen content, notably status bar content. A specific method is defined inside the app module to let NVDA retrieve status bar content in Windows 11 Notepad.

### Hunting for UIA implementation issues

As noted above, some controls ship with odd or bad UIA implementations, and universal apps are no exception (at least for app modules included with the add-on). Because of this, the following app modules (and in case of two, taken care of by Windows App Objects global plugin itself) include workarounds for various UIA problems:

* Calendar (hxcalendarappimm.py) and Mail (hxoutlook.py): some edit fields, such as appointment title and others are shown as read-only when they are not, and removing this state from states set for these controls resolved this problem. As of 2022, this workaround is no longer present in the add-on.
* Cortana: some search suggestions expose same text for name and description, which results in repeats for suggestion result text. This was corrected by comparing name and description and nullifying the description (obj.description = None). This workaround is no longer applicable due to Windows Search redesign in Version 1903. Also, when opening Sets version of Cortana search box (builds 17666 and 17692), wrong controller for event is fired, which prevents NVDA from announcing suggestions, and this has been corrected.
* Maps: despite no changes to the app, live region changed event is fired by map title control, so NVDA includes a way to suppress repetitions. AS of 2022, this workaround is gone from the add-on.
* Settings and Store: for some controls (such as when downloading content from Store), a specific status control fires live region changed event. Unfortunately, the text for them are generic (for example, "downloading some percent" as opposed to announcing the product one is downloading), thus NVDA will locate information such as product names when this happens to make this easier to follow. Also, in Settings app, some controls in older versions of this app have no label, thus NVDA is told to look for labels to traversing sibling (next/previous) objects, and in case of certain Windows 10 1809 installations, the correct label is the name of the first child.

### A tale on app module and executable names

One of the side-effects of continuous delivery is appearance of unanticipated changes. This is more so when a workaround for an app broke simply because the name of the executable or the app has changed. In addition, some apps shipped with an executable whose name broke Python's module name and import routines.

The specific issues encountered were:

* Calculator, Mail and Calendar, Maps, Modern Keyboard, Shell Experience Host (shellexperiencehost.py, action center/quick settings), Start menu, Windows Search and Store: executable names have changed throughout development of Windows 10 and later. For example, in May 2017, workarounds in place for Mail app broke when Microsoft renamed hxmail to hxoutlook, and in July 2019, Modern Keyboard was renamed to textinputhost. Windows 11 is no exception, bringing with it renamed Windows Search executable (searchhost) and 24H2 separating quick settings from Shell Experience Host and renaming it to shellhost.exe. Due to this, aliasing (a new app module importing everything from an old version) is common.
* MSN Weather, Store, modern keyboard and others: some executable names have a dot (.) in the middle, which breaks app module import routines. This is countered by replacing dots with underscores (_). For example, for Store, the actual executable name is winstore.app.exe, while the app module for this app is named winstore_app.py. This fix is now part of recent NVDA releases.

## Few remarks

### UIA performance

Numerous issues were filed on NVDA's GitHub page regarding UIA performnace issues. These include issues in early days of Edge support where navigating the document was slow (resolved in NVDA 2017.2), list view issues in File Explorer while using a program with high CPU usage (GoldWave, for example, resolved in NVDA 2018.4) and so on. While some are specific to NVDA, others are reproducible while using Narrator, hence NV Access and Microsoft are actively collaborating on identifying and writing fixes for performance and control implementation problems (such as some of the ones listed above).

### Narrator is the new reference in screen reading in Windows 10 (and later) and universal apps

Until a few years ago, any screen reader wishing to support an app or add features would look up to JAWS for Windows for guidance. This is no longer the case with Windows 10 (and later) and universal apps, as Narrator provides a useful yardstick (at least a base implementation other screen reader vendors should respond to) when it comes to reading text on screen, feature set for supporting universal apps, and investigate UIA issues. Some of the features discussed above, such as search suggestion notification, were inspired by Narrator's handling of various UIA events, and because Narrator reads what is told to read, NVDA ships with workarounds for odd UIA implementations to get around some problems.

### Add-on development and testing

The add-on employs iterative development cycle where features are continuously refined. Refinements can be driven by user feedback, changes in Windows Insider Preview builds and apps, or changes were made to NVDA that requires the add-on to support old and new code paths. Because the add-on employs continuous delivery model (stable versions can be released at any time), a stable version may contain features in various stages of development.

As part of add-on development and testing, one activity I perform is keep up with changes in Insider Preview builds, specifically changes in dev and canary channels (formerly Windows Insider fast ring; became dev channel in 2020 and split into dev and canary in 2023). Whenever new builds are released, I analyze new features described in release notes and see if user-visible changes are present. If so, I test new features and see how usable the feature is while using Narrator and NVDA. If I notice things are not working with NVDA, I perform debugging procedures such as analyzing UIA events to figure out how NVDA can better support a feature. This is done repeatedly until I'm satisfied that NVDA supports a given feature well. Examples of features that followed this route include emoji panel support, changes to Settings app interface, and reporting virtual desktop reordering operation. Note that even if a build does not come with spectacular changes, I still use it to look for small changes and fixes.

Because Windows ships with apps that can change without notice, apps can become another source of feature development. To support app changes, I note down differences between app releases and come up with a plan to support old and new releases. This becomes important if executables were renamed, in which case app aliasing is used to support old and new app releases. Examples include Mail and Calendar, modern keyboard, and Cortana.

Besides Windows and app changes, changes to NVDA such as incorporating support for a new Windows feature (scenario 1) or changes to apps (scenario 2) can contribute to feature changes. As described below, some add-on features became part of NVDA. If NV Access and contributors plan to incorporate features from this add-on, I assume it has been integrated and I edit the add-on source code to support old (not integrated) and new (integrated) code paths. These rely on presence of specific module attributes and do my best to let the add-on emulate features being reviewed. Once a version of NVDA with new features is released, the add-on is told to drop support for old NVDA versions with just integrated features not present. This route was taken to incorporate features such as emoji panel, search suggestions, Calculator support, and handling notification event.

From time to time, these changes are released as development snapshots. This is so that I can gather feedback from testers in hopes of refining changes. At least once a month, changes in development snapshots are sent to a branch used to prepare stable add-on releases, and a stable version is tagged a few days later once final changes such as latest localizations are integrated. The cycle then repeats.

#### Changes in 2021 and refinements in 2022 and 2023

One big change in 2021 is milestone-based development. It is still an iterative development process, but I decided to use a quarterly development cycle to isolate long-running features and to focus on other priorities. This is a result of life changes that will reduce add-on development commitments - to reduce focus on add-on maintenance in favor of early planning and initial development, focus on other priorities, and refine the add-on when I have time.

The quarterly milestone process derives from Windows development milestones. As part of Windows development, Microsoft divides development phases into milestones - semesters until 2021, development year in 2022, returned to semesters in 2023. Each development milestone is named according to a chemical element, specifically named after elements in the periodic table. This is done for Microsoft Azure, but also was adopted for Windows development recently and is designed to set milestones for long-running features. Near the end of a milestone, Microsoft chooses features that will be part of the next release (either a full build or an enablement package) and creates a maintenance branch from these features, with others pushed to the next development milestone for further refinements.

The quarterly development cycle for Windows App Essentials (adopted in June 2021) is named after Windows development milestones, divided into quarters. This was based on semesters in 2021 (two quarters or halves for each semester) and year-based milestones in 2022 (up to four quarters). For example, as of March 2025, the latest development cycle inside Microsoft is "Selenium", and the internal development cycle for Windows App Essentials is "selenium2" running from March 2025 to July 2025. Each milestone is dedicated to one or more long-running features or themes - for example, "nickel1" (June to September 2021), named after "nickel" development year (formerly a development semester but became a year-long milestone inside Microsoft in 2022), was dedicated to refining Windows 11 support and preparing the add-on for control types refactor from NVDA 2021.2. I tend to do a code sprint early and refine code as time goes on - as of March 2025, "selenium1" milestone development was just completed and switched to refining code changes, mostly introducing significant changes and responding to NVDA 2025.1 features such as inclusion of parts of this add-on. This is just one of the activities I perform as I go on in life (the priority at the moment is graduate school).

In between milestone releases, a dedicated branch is used to backport key changes from the upcoming quarter. These are initially named after a chemical compound or an alloy involving the base element which is the base for the backport branch. For example, a branch named "alnico" (an alloy of aluminum, nickel, and cobalt) is used to backport key changes from "nickel2" to "nickel1" branch. These serve not only as maintenance branches, but also introduce features that will be part of the next milestone release provided that they do not involve massive rewrites such as requiring newer NVDA or Windows releases. Eventually the "alloy" branches are merged into milestone branches such as "nickel1".

The whole point of development milestone/quarter process is to remind me of life priorities. In the past, I was able to dedicate more time to add-on development and maintenance. As time went on, it became important to think about my immediate life concerns such as focusing more on advanced education. Besides, I have been looking for a way to reimagine add-on development cycles, so in June 2021, I decided to switch stable version development from more of a continuous delivery to quarterly releases with periodic backports, similar how recent features such as News and Interests (part of widgets in Windows 11) were developed (continuous development, followed by backports to stable releases). This change should have minimal impact on development snapshots, which are released continuously as add-on code changes. Overall, milestone development is still an iterative process just like previous releases.

### Integrating features from this add-on to NVDA screen reader

As noted above, some add-on features are being (or have been) integrated into NVDA. These include search suggestion notification, modern keyboard support, live region changed event tracking and announcement and so on. As described above, these changes can come from Windows, apps, and other sources such as internal NVDA changes.

Typically, when a feature from an add-on is integrated into NVDA, it goes through an issue-prototype-review-test-documentation cycle. To illustrate this, let us go through steps involved in getting search suggestions into NVDA:

1. Issue: an issue regarding search suggestions was filed in 2016.
2. Prototype: support for search suggestions was included in the add-on.
3. Review: while transforming the prototype into an NVDA pull request, I and NV Access went through a review phase where implementation detail were discussed and test cases written.
4. Test: in 2017, search suggestion feature made its debut in an NVDA next snapshod. This resulted in feedback from users regarding braille support, sounds and others. After several weeks, this feature was made available to master snapshot users, thus ready for NVDA 2017.3.
5. Documentation: the search suggestion feature was documented in the user guide. Discussion of this feature in this article is a special case of documentation step.

After search suggestions support became part of NVDA, I edited the add-on to assume this feature was always available, mostly involving removing the integrated code from the add-on.

Due to changes to release process in 2018, testing occurs via pull requests.

In addition, when a feature from an add-on is under consideration for inclusion in NVDA, I modify the add-on source code to make it compliant with NVDA source code guidelines, such as commenting style, copyright header and so on.

### Giving feedback to app developers

Feedback drives Windows and universal apps. one of the reasons for instituting Windows Insider Program, as noted by Microsoft and others, is to gather feedback from millions of users in hopes of making Windows better in the long run. As such, sending feedback regarding Windows and preinstalled universal apps, as well as third-party apps is crucial at the age of feedback-driven development.

Here are some tips regarding sending feedback to app writers:

1. Embrace: have willingness to embrace (use and test) the app in question.
2. Document: if something happens, document what happened, steps to reproduce, and possible workarounds.
3. Send: send feedback to developers (Feedback Hub, contacting developers of third-party universal apps, screen reader vendors and so on).
4. Follow-up: follow-up with developers if they have questions for you or you want to know what's going on with your feedback.

### Accessibility best practices for universal apps

As a Windows Insider, a screen reader contributor and the author of a screen reader add-on for Windows 10 and later and universal apps, I came across numerous examples where apps were inaccessible at first, or usability was overshadowed by issues when working with controls, navigation and so on.

Here are some tips in hopes of making universal apps truly universally accessible and usable:

* Listen to feedback, especially feedback coming from users with disabilities such as screen reader users.
* Do not put accessibility as an afterthought, nor something you want to work in the future (say, version 3). Proactive accessibility and investigations into issues is something app developers should learn as they develop apps.
* Test with screen readers and other assistive technologies: one way to validate accessibility issues raised by users with disabilities is using assistive technologies in real life. Use facilities offered by screen readers such as Python console in NVDA, developer mode in Narator and so on in hopes of locating where the root of the issue lies.
* Try using keyboards and other input methods offered by various assistive technologies: touchscreen isn't the only input method used in universal apps. Many screen reader users use a keyboard to interact with apps, and some use touchscreen gestures offered by screen readers to navigate an app and respond to changes. Try using them to make sure app features are working as advertised when using keyboards and other input methods.
* Use useful labels: in case the control has no label as reported by screen readers, be sure to provide labels. A good historical case is Windows Defender Security Center where there was no label for various buttons in 2016, which was fixed in 2017 with Creators Update. Also, avoid generic XAML labels such as someclass.someotherclass.such (especialy lists and list items), as it does not provide an accurate picture as to where one is located. A classic case is Feedback Hub app where generic labels for lists were presnet in older versions, subsequently fixed in recent updates.
* Raise appropriate UIA events: screen readers listen to UIA events to detect what's happening with apps. For example, if there's a need to anounce suggestions, controller for event should be fired. An example is Store where old releases did not raise controller for event when content suggestions appeared, with recent versions raising this event.

## Conclusion

With the introduction of Windows 10 and Universal Windows Platform, a new way of connecting users and developers has emerged: feedback-driven development. This allows users to send feedback regarding features and bugs, including that of accessibility feedback. Although accessibility of Windows and universal apps were spotty at first, this situation is improving, driven by Microsoft's commitment to accessibility, continued feedback, and collaboration between Microsoft and assistive technology vendors. This trend continues in Windows 11.

In terms of NVDA, what made usability of Windows 10 and later better was not only changes made from within Windows and universal apps, but also proactive investigations into making sure NVDA users have a great time with Windows. Windows App Essentials add-on is part of that work, as discussed throughout this article when talking about UIA workarounds, improving support for apps and controls and others. But there are limits as to what the add-on can do, as the other puzzle pieces are willingness from developers (especially third-party UWP developers) to embrace accessibility as a pillar in their apps, and willingness from users to send accessibility feedback. Although some add-on features are being integrated into NVDA, there are some areas where the add-on is needed (especially when supporting features introduced in Windows Insider Preview builds), and until the day accessibility is everywhere in modern Windows ecosystem and universal apps, the add-on will still be here.

## References

* Windows 10 (Wikipedia): https://en.wikipedia.org/wiki/Windows_10
* Windows 11 (Wikipedia): https://en.wikipedia.org/wiki/Windows_11
* Windows Insider Program (Microsoft): https://insider.windows.com/
* Windows as a Service Overview (Microsoft Docs): https://docs.microsoft.com/en-us/windows/deployment/update/waas-overview
* What's a Universal Windows Platform (UWP) App (Microsoft UWP App Developer): https://docs.microsoft.com/en-us/windows/uwp/get-started/whats-a-uwp
* UI Automation Overview (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee684076(v=vs.85).aspx
* MSAA overview (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/dd373592(v=vs.85).aspx
* UI Automation and Active Accessibility (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671585(v=vs.85).aspx
* Component Object Model Overview (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ms680573(v=vs.85).aspx
* IUIAutomationElement interface (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671425(v=vs.85).aspx
* cachedAutomationId (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671434(v=vs.85).aspx
* UI Automation Properties Overview (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671594(v=vs.85).aspx
* UI Automation Events Overview (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671221(v=vs.85).aspx
* UI Automation Event Identifiers (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/ee671223(v=vs.85).aspx
* Auto-suggest accessibility, part of Accessible Text Requirements (Microsoft Docs): https://docs.microsoft.com/en-us/windows/uwp/accessibility/accessible-text-requirements
* IUIAutomationNotificationEventHandler::HandleNotificationEvent (MSDN): https://msdn.microsoft.com/en-us/library/windows/desktop/mt814955(v=vs.85).aspx
