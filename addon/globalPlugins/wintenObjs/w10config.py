# Windows 10 add-on update and config facility
# Copyright 2017-2018 Joseph Lee, released under GPL.

# Add-on configuration and updates.
# Because the add-on employs continuous delivery model, it is beneficial to provide update facility.
# Base config section was inspired by Clip Contents Designer (Noelia Martinez).
# Overall update check routine comes from StationPlaylist Studio add-on (Joseph Lee).)

import os
import threading
# Python 3 calls for using urllib.request instead, which is functionally equivalent to urllib2.
try:
	from urllib.request import urlopen
except ImportError:
	from urllib import urlopen
import tempfile
import ctypes
import ssl
import time
import re
import config
import gui
import wx
# What if this is run from NVDA source?
try:
	import updateCheck
	canUpdate = True
except RuntimeError:
	canUpdate = False
from logHandler import log
import addonHandler
addonHandler.initTranslation()

# Add-on config database
confspec = {
	"autoUpdateCheck": "boolean(default=true)",
	"updateChannel": "string(default=dev)",
	"updateCheckTime": "integer(default=0)",
	"updateCheckTimeInterval": "integer(min=0, max=30, default=1)",
}
config.conf.spec["wintenApps"] = confspec

_addonDir = unicode(os.path.join(os.path.dirname(__file__), "..", ".."), "mbcs")
addonVersion = addonHandler.Addon(unicode(_addonDir)).manifest['version']
addonUpdateCheckInterval = 86400

channels={
	"stable":"https://addons.nvda-project.org/files/get.php?file=w10",
	"dev":"https://addons.nvda-project.org/files/get.php?file=w10-dev",
}


updateChecker = None
# To avoid freezes, a background thread will run after the global plugin constructor calls wx.CallAfter.
def autoUpdateCheck():
	currentTime = time.time()
	whenToCheck = config.conf["wintenApps"]["updateCheckTime"]
	if currentTime >= whenToCheck:
		t = threading.Thread(target=addonUpdateCheck, kwargs={"autoCheck":True})
		t.daemon = True
		t.start()
	else: startAutoUpdateCheck(interval=divmod((whenToCheck-currentTime), addonUpdateCheckInterval)[-1])

# Start or restart auto update checker.
def startAutoUpdateCheck(interval=None):
	# Don't do anything if told to check for update whenever NVDA starts.
	if not config.conf["wintenApps"]["updateCheckTimeInterval"]: return
	global updateChecker
	if updateChecker is not None:
		wx.CallAfter(updateChecker.Stop)
	updateChecker = wx.PyTimer(autoUpdateCheck)
	wx.CallAfter(updateChecker.Start, (addonUpdateCheckInterval if interval is None else interval) * 1000, True)

# Borrowed ideas from NVDA Core.
def checkForAddonUpdate():
	updateURL = channels[config.conf["wintenApps"]["updateChannel"]]
	# Commenting this out will effectively turn off pilot builds.
	# Check if pilot build is supported.
	def _pilotBuild():
		import versionInfo, winVersion
		return config.conf["wintenApps"]["updateChannel"] == "dev" and versionInfo.updateVersionType == "snapshot:next" and winVersion.winVersion.build >= 16299
	if _pilotBuild():
		updateURL = "http://www.josephsl.net/files/nvdaaddons/getupdate.php?file=w10-try"
	try:
		res = urlopen(updateURL)
		res.close()
	except IOError as e:
		# SSL issue (seen in NVDA Core earlier than 2014.1).
		if isinstance(e.strerror, ssl.SSLError) and e.strerror.reason == "CERTIFICATE_VERIFY_FAILED":
			_updateWindowsRootCertificates()
			res = urlopen(updateURL)
		else:
			raise
	if res.code != 200:
		raise RuntimeError("Checking for update failed with code %d" % res.code)
	# Build emulated add-on update dictionary if there is indeed a new verison.
	version = re.search("wintenApps-(?P<version>.*).nvda-addon", res.url).groupdict()["version"]
	if addonVersion != version:
		return {"curVersion": addonVersion, "newVersion": version, "path": res.url}
	return None

progressDialog = None
def addonUpdateCheck(autoCheck=False):
	global progressDialog
	config.conf["wintenApps"]["updateCheckTime"] = int(time.time()) + config.conf["wintenApps"]["updateCheckTimeInterval"] * addonUpdateCheckInterval
	try:
		info = checkForAddonUpdate()
	except:
		log.error("Error checking for update", exc_info=True)
		if not autoCheck:
			wx.CallAfter(progressDialog.done)
			progressDialog = None
			# Translators: Error text shown when add-on update check fails.
			wx.CallAfter(gui.messageBox, _("Error checking for update."),
				# Translators: Title of the dialog shown when add-on update check fails.
				_("Windows 10 App Essentials update"), wx.ICON_ERROR)
		else: startAutoUpdateCheck()
		return
	if not autoCheck:
		wx.CallAfter(progressDialog.done)
		progressDialog = None
	if info is None:
		if not autoCheck:
			# Translators: Presented when no add-on update is available.
			wx.CallAfter(gui.messageBox, _("No add-on update available."),
				# Translators: Title of the dialog presented when no add-on update is available.
				_("Windows 10 App Essentials update"))
			return
		else: startAutoUpdateCheck()
	else:
		if autoCheck: startAutoUpdateCheck()
		# Translators: Text shown if an add-on update is available.
		checkMessage = _("Windows 10 App Essentials {newVersion} is available. Would you like to update?").format(newVersion = info["newVersion"])
		# Translators: Title of the add-on update check dialog.
		wx.CallAfter(getUpdateResponse, checkMessage, _("Windows 10 App Essentials update"), info["path"])

def getUpdateResponse(message, caption, updateURL):
	if gui.messageBox(message, caption, wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION) == wx.YES:
		W10UpdateDownloader([updateURL]).start()

class WinTenAppsConfigDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: The title of a dialog to configure advanced WinTenApps add-on options such as update checking.
		super(WinTenAppsConfigDialog, self).__init__(parent, title=_("Windows 10 App Essentials settings"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		w10Helper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: A checkbox to toggle automatic add-on updates.
		self.autoUpdateCheckbox=w10Helper.addItem(wx.CheckBox(self,label=_("Automatically check for add-on &updates")))
		self.autoUpdateCheckbox.SetValue(config.conf["wintenApps"]["autoUpdateCheck"])
		# Translators: The label for a setting in WinTenApps add-on settings to select automatic update interval in days.
		self.updateInterval=w10Helper.addLabeledControl(_("Update &interval in days"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=30, initial=config.conf["wintenApps"]["updateCheckTimeInterval"])
		# Translators: The label for a combo box to select update channel.
		labelText = _("&Add-on update channel:")
		self.channels=w10Helper.addLabeledControl(labelText, wx.Choice, choices=["development", "stable"])
		self.updateChannels = ("dev", "stable")
		self.channels.SetSelection(self.updateChannels.index(config.conf["wintenApps"]["updateChannel"]))
		if canUpdate:
			# Translators: The label of a button to check for add-on updates.
			updateCheckButton = w10Helper.addItem(wx.Button(self, label=_("Check for add-on &update")))
			updateCheckButton.Bind(wx.EVT_BUTTON, self.onUpdateCheck)

		w10Helper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(w10Helper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.autoUpdateCheckbox.SetFocus()
		self.Center(wx.BOTH | (wx.CENTER_ON_SCREEN if hasattr(wx, "CENTER_ON_SCREEN") else 2))

	def onOk(self, evt):
		# #39: Prompt if switching from stable to development channel.
		currentUpdateChannel = config.conf["wintenApps"]["updateChannel"]
		newUpdateChannel = ("dev", "stable")[self.channels.GetSelection()]
		if currentUpdateChannel == "stable" and newUpdateChannel == "dev":
			if gui.messageBox(
				# Translators: The confirmation prompt displayed when changing to development channel (with risks involved).
				_("You are about to switch to development updates channel. Although updates from this channel brings exciting features, it also comes with updates that might be unstable at times and should be used for testing and sending feedback to the add-on developer. If you prefer to use stable releases, please answer no and switch to stable update channel. Are you sure you wish to switch to the development update channel?"),
				# Translators: The title of the channel switch confirmation dialog.
				_("Switching to unstable channel"),
				wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION, self
			) == wx.NO:
				return
		global updateChecker
		if updateChecker and updateChecker.IsRunning(): updateChecker.Stop()
		config.conf["wintenApps"]["autoUpdateCheck"] = self.autoUpdateCheckbox.Value
		config.conf["wintenApps"]["updateCheckTimeInterval"] = self.updateInterval.Value
		if not self.updateInterval.Value:
			config.conf["wintenApps"]["updateCheckTime"] = 0
			updateChecker = None
		else:
			updateChecker = wx.PyTimer(autoUpdateCheck)
			currentTime = time.time()
			whenToCheck = currentTime+(self.updateInterval.Value * addonUpdateCheckInterval)
			updateChecker.Start((whenToCheck-currentTime) * 1000, True)
		config.conf["wintenApps"]["updateChannel"] = ("dev", "stable")[self.channels.GetSelection()]
		self.Destroy()

	def onCancel(self, evt):
		self.Destroy()

	def onUpdateCheck(self, evt):
		self.onOk(None)
		global progressDialog
		progressDialog = gui.IndeterminateProgressDialog(gui.mainFrame,
		# Translators: The title of the dialog presented while checking for add-on updates.
		_("Add-on update check"),
		# Translators: The message displayed while checking for newer version of WinTenApps add-on.
		_("Checking for new version of Windows 10 App Essentials add-on..."))
		threading.Thread(target=addonUpdateCheck).start()

def onConfigDialog(evt):
	gui.mainFrame._popupSettingsDialog(WinTenAppsConfigDialog)


# Update downloader (credit: NV Access)
# Customized for WinTenApps add-on.
try:
	class W10UpdateDownloader(updateCheck.UpdateDownloader):
		"""Overrides NVDA Core's downloader.)
		No hash checking for now, and URL's and temp file paths are different.
		"""

		def __init__(self, urls, fileHash=None):
			"""Constructor.
			@param urls: URLs to try for the update file.
			@type urls: list of str
			@param fileHash: The SHA-1 hash of the file as a hex string.
			@type fileHash: basestring
			"""
			# In recent NVDA next snapshots (February 2018), update downloader was changed to take in update info dictionary.
			try:
				super(W10UpdateDownloader, self).__init__(urls, fileHash)
			except:
				pass
			self.urls = urls
			self.destPath = tempfile.mktemp(prefix="wintenApps_update-", suffix=".nvda-addon")
			self.fileHash = fileHash

		def start(self):
			"""Start the download.
			"""
			self._shouldCancel = False
			# Use a timer because timers aren't re-entrant.
			self._guiExecTimer = wx.PyTimer(self._guiExecNotify)
			gui.mainFrame.prePopup()
			# Translators: The title of the dialog displayed while downloading add-on update.
			self._progressDialog = wx.ProgressDialog(_("Downloading Add-on Update"),
				# Translators: The progress message indicating that a connection is being established.
				_("Connecting"),
				# PD_AUTO_HIDE is required because ProgressDialog.Update blocks at 100%
				# and waits for the user to press the Close button.
				style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME | wx.PD_AUTO_HIDE,
				parent=gui.mainFrame)
			self._progressDialog.Raise()
			t = threading.Thread(target=self._bg)
			t.daemon = True
			t.start()

		def _error(self):
			self._stopped()
			gui.messageBox(
				# Translators: A message indicating that an error occurred while downloading an update to NVDA.
				_("Error downloading add-on update."),
				# Translators: The title of a dialog indicating that an error occurred while downloading an update to NVDA.
				_("Error"),
				wx.OK | wx.ICON_ERROR)

		def _downloadSuccess(self):
			self._stopped()
			# Emulate add-on update (don't prompt to install).
			from gui import addonGui
			closeAfter = addonGui.AddonsDialog._instance is None
			try:
				try:
					bundle=addonHandler.AddonBundle(self.destPath.decode("mbcs"))
				except:
					log.error("Error opening addon bundle from %s"%self.destPath,exc_info=True)
					# Translators: The message displayed when an error occurs when opening an add-on package for adding. 
					gui.messageBox(_("Failed to open add-on package file at %s - missing file or invalid file format")%self.destPath,
						# Translators: The title of a dialog presented when an error occurs.
						_("Error"),
						wx.OK | wx.ICON_ERROR)
					return
				bundleName=bundle.manifest['name']
				for addon in addonHandler.getAvailableAddons():
					if not addon.isPendingRemove and bundleName==addon.manifest['name']:
						addon.requestRemove()
						break
				progressDialog = gui.IndeterminateProgressDialog(gui.mainFrame,
				# Translators: The title of the dialog presented while an Addon is being updated.
				_("Updating Add-on"),
				# Translators: The message displayed while an addon is being updated.
				_("Please wait while the add-on is being updated."))
				try:
					gui.ExecAndPump(addonHandler.installAddonBundle,bundle)
				except:
					log.error("Error installing  addon bundle from %s"%self.destPath,exc_info=True)
					if not closeAfter: addonGui.AddonsDialog(gui.mainFrame).refreshAddonsList()
					progressDialog.done()
					del progressDialog
					# Translators: The message displayed when an error occurs when installing an add-on package.
					gui.messageBox(_("Failed to update add-on  from %s")%self.destPath,
						# Translators: The title of a dialog presented when an error occurs.
						_("Error"),
						wx.OK | wx.ICON_ERROR)
					return
				else:
					if not closeAfter: addonGui.AddonsDialog(gui.mainFrame).refreshAddonsList(activeIndex=-1)
					progressDialog.done()
					del progressDialog
			finally:
				try:
					os.remove(self.destPath)
				except OSError:
					pass
				if closeAfter:
					wx.CallLater(1, addonGui.AddonsDialog(gui.mainFrame).Close)
except:
	log.debugWarning("Error downloading Windows 10 App Essentials update", exc_info=True)

# Borrowed from NVDA Core (the only difference is the URL and where structures are coming from).
def _updateWindowsRootCertificates():
	crypt = ctypes.windll.crypt32
	# Get the server certificate.
	sslCont = ssl._create_unverified_context()
	u = urlopen("https://addons.nvda-project.org", context=sslCont)
	cert = u.fp._sock.getpeercert(True)
	u.close()
	# Convert to a form usable by Windows.
	certCont = crypt.CertCreateCertificateContext(
		0x00000001, # X509_ASN_ENCODING
		cert,
		len(cert))
	# Ask Windows to build a certificate chain, thus triggering a root certificate update.
	chainCont = ctypes.c_void_p()
	crypt.CertGetCertificateChain(None, certCont, None, None,
		ctypes.byref(updateCheck.CERT_CHAIN_PARA(cbSize=ctypes.sizeof(updateCheck.CERT_CHAIN_PARA),
			RequestedUsage=updateCheck.CERT_USAGE_MATCH())),
		0, None,
		ctypes.byref(chainCont))
	crypt.CertFreeCertificateChain(chainCont)
	crypt.CertFreeCertificateContext(certCont)
