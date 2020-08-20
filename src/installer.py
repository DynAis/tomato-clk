import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['mainp.py','-F','-w','--icon=image/tomato.ico']
    run(opts)