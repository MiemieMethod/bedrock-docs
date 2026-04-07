import neteaseLabelScript.labelConst as labelConst
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ScreenNode = clientApi.GetScreenNodeCls()
import neteaseLabelScript.apiUtil as apiUtil

class LabelPopScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print '==== %s ====' % 'init LabelPopScreen'

	def Create(self):
		self.AddTouchEventHandler("/mask/img_base_pop/btn_close", self.OnClose)
		self.AddTouchEventHandler("/mask/img_base_pop/btn_ensure", self.OnClose)

	def InitScreen(self):
		self.SetVisible("", False)

	def Show(self, title, detail):
		self.SetText('/mask/img_base_pop/lb_title', title)
		self.SetText('/mask/img_base_pop/lb_contents', detail)
		self.SetVisible("", True)

	@apiUtil.touch_filter("up")
	def OnClose(self, args):
		self.SetVisible("", False)