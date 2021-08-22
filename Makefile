all: ui

ui:
	@pyuic5 src/ui/patheditor.ui -o src/ui/patheditor_ui.py
	@pyrcc5 src/ui/images.qrc -o src/images_rc.py