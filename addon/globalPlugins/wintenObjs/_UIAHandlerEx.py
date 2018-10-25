#_UIAHandler.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2011-2018 NV Access Limited, Joseph Lee
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

# Extended to add additional events and such.

from UIAHandler import *

class UIAHandlerEx(UIAHandler):
	_com_interfaces_=[IUIAutomationEventHandler,IUIAutomationFocusChangedEventHandler,IUIAutomationPropertyChangedEventHandler,IUIAutomationNotificationEventHandler]

	def __init__(self):
		super(UIAHandlerEx,self).__init__()

	def MTAThreadFunc(self):
		try:
			oledll.ole32.CoInitializeEx(None,comtypes.COINIT_MULTITHREADED) 
			isUIA8=False
			try:
				self.clientObject=CoCreateInstance(CUIAutomation8._reg_clsid_,interface=IUIAutomation,clsctx=CLSCTX_INPROC_SERVER)
				isUIA8=True
			except (COMError,WindowsError,NameError):
				self.clientObject=CoCreateInstance(CUIAutomation._reg_clsid_,interface=IUIAutomation,clsctx=CLSCTX_INPROC_SERVER)
			# #7345: Instruct UIA to never map MSAA winEvents to UIA propertyChange events.
			# These events are not needed by NVDA, and they can cause the UI Automation client library to become unresponsive if an application firing winEvents has a slow message pump. 
			pfm=self.clientObject.proxyFactoryMapping
			for index in xrange(pfm.count):
				e=pfm.getEntry(index)
				for propertyID in UIAPropertyIdsToNVDAEventNames.keys():
					# Check if this proxy has mapped any winEvents to the UIA propertyChange event for this property ID 
					try:
						oldWinEvents=e.getWinEventsForAutomationEvent(UIA_AutomationPropertyChangedEventId,propertyID)
					except IndexError:
						# comtypes does not seem to correctly handle a returned empty SAFEARRAY, raising IndexError
						oldWinEvents=None
					if oldWinEvents:
						# As winEvents were mapped, replace them with an empty list
						e.setWinEventsForAutomationEvent(UIA_AutomationPropertyChangedEventId,propertyID,[])
						# Changes to an enty are not automatically picked up.
						# Therefore remove the entry and re-insert it.
						pfm.removeEntry(index)
						pfm.insertEntry(index,e)
			if isUIA8:
				# #8009: use appropriate interface based on highest supported interface.
				# #8338: made easier by traversing interfaces supported on Windows 8 and later in reverse.
				for interface in reversed(CUIAutomation8._com_interfaces_):
					try:
						self.clientObject=self.clientObject.QueryInterface(interface)
						break
					except COMError:
						pass
				# Windows 10 RS5 provides new performance features for UI Automation including event coalescing and connection recovery. 
				# Enable all of these where available.
				if isinstance(self.clientObject,IUIAutomation6):
					self.clientObject.CoalesceEvents=CoalesceEventsOptions_Enabled
					self.clientObject.ConnectionRecoveryBehavior=ConnectionRecoveryBehaviorOptions_Enabled
			log.info("UIAutomation: %s"%self.clientObject.__class__.__mro__[1].__name__)
			self.windowTreeWalker=self.clientObject.createTreeWalker(self.clientObject.CreateNotCondition(self.clientObject.CreatePropertyCondition(UIA_NativeWindowHandlePropertyId,0)))
			self.windowCacheRequest=self.clientObject.CreateCacheRequest()
			self.windowCacheRequest.AddProperty(UIA_NativeWindowHandlePropertyId)
			self.UIAWindowHandleCache={}
			self.baseTreeWalker=self.clientObject.RawViewWalker
			self.baseCacheRequest=self.windowCacheRequest.Clone()
			import UIAHandler
			self.ItemIndex_PropertyId=NVDAHelper.localLib.registerUIAProperty(byref(ItemIndex_Property_GUID),u"ItemIndex",1)
			self.ItemCount_PropertyId=NVDAHelper.localLib.registerUIAProperty(byref(ItemCount_Property_GUID),u"ItemCount",1)
			for propertyId in (UIA_FrameworkIdPropertyId,UIA_AutomationIdPropertyId,UIA_ClassNamePropertyId,UIA_ControlTypePropertyId,UIA_ProviderDescriptionPropertyId,UIA_ProcessIdPropertyId,UIA_IsTextPatternAvailablePropertyId,UIA_IsContentElementPropertyId,UIA_IsControlElementPropertyId):
				self.baseCacheRequest.addProperty(propertyId)
			self.baseCacheRequest.addPattern(UIA_TextPatternId)
			self.rootElement=self.clientObject.getRootElementBuildCache(self.baseCacheRequest)
			self.reservedNotSupportedValue=self.clientObject.ReservedNotSupportedValue
			self.ReservedMixedAttributeValue=self.clientObject.ReservedMixedAttributeValue
			self.clientObject.AddFocusChangedEventHandler(self.baseCacheRequest,self)
			self.clientObject.AddPropertyChangedEventHandler(self.rootElement,TreeScope_Subtree,self.baseCacheRequest,self,UIAPropertyIdsToNVDAEventNames.keys())
			for x in UIAEventIdsToNVDAEventNames.iterkeys():  
				self.clientObject.addAutomationEventHandler(x,self.rootElement,TreeScope_Subtree,self.baseCacheRequest,self)
			# #7984: add support for notification event (IUIAutomation5, part of Windows 10 build 16299 and later).
			if isinstance(self.clientObject, IUIAutomation5):
				self.clientObject.AddNotificationEventHandler(self.rootElement,TreeScope_Subtree,self.baseCacheRequest,self)
		except Exception as e:
			self.MTAThreadInitException=e
		finally:
			self.MTAThreadInitEvent.set()
		self.MTAThreadStopEvent.wait()
		self.clientObject.RemoveAllEventHandlers()

