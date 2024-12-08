# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['tomogatchiGUI.py'],
    pathex=[],
    binaries=[],
    datas=[('Sprite_Stuff/SpriteFolder', 'Sprite_Stuff/SpriteFolder'), ('fonts', 'fonts'), ('images', 'images'), ('Color_game', 'Color_game'), ('.env', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='tomogatchiGUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
