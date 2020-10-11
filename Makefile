build:
	poetry build

reinstall: build
	pipx uninstall eyebreak
	pipx install dist/eyebreak-0.1.0-py3-none-any.whl
