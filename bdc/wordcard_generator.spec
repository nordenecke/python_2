# -*- mode: python -*-

block_cipher = None


a = Analysis(['wordcard_generator.py'],
             pathex=['E:\\workspace\\python\\bdc'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='wordcard_generator',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='wordcard.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='wordcard_generator')
