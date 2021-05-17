# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['tradutor_runas_osnf.py'],
             pathex=['C:\\Users\\denad\\Google Drive\\Desenvolvimento\\Programas Python\\Conversor Runas 1.0\\Conversor Runas 1.0\\Tradutor de Runas OSNF'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='tradutor_runas_osnf',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
