from objc_util import *
import random

#Made By: OMZ Admin
#Edit By: Russian Otter

load_framework('ReplayKit')
RPScreenRecorder = ObjCClass('RPScreenRecorder')

def previewControllerDidFinish_(_self, _cmd, _vc):
	ObjCInstance(_vc).dismissViewControllerAnimated_completion_(True, None)

PreviewDelegate = create_objc_class('PreviewDelegate', methods=[previewControllerDidFinish_])

def stop_callback(_cmd, _vc):
	vc = ObjCInstance(_vc)
	delegate = PreviewDelegate.new().autorelease()
	vc.setPreviewControllerDelegate_(delegate)
	rootvc = UIApplication.sharedApplication().keyWindow().rootViewController()
	rootvc.presentViewController_animated_completion_(vc, True, None)
	
stop_handler = ObjCBlock(stop_callback, restype=None, argtypes=[c_void_p, c_void_p])
recorder = RPScreenRecorder.sharedRecorder()

@on_main_thread
def start_recording():
	recorder.startRecordingWithMicrophoneEnabled_handler_(False, None)

@on_main_thread
def stop_recording():
	recorder.stopRecordingWithHandler_(stop_handler)
