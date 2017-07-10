import appModuleHandler
import tones
import ui

class AppModule(appModuleHandler.AppModule):

	def event_nameChange(self, obj, nextHandler):
		ui.message(obj.name)
		nextHandler()
