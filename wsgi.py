
"""Application entry point."""
from warehouseServer import init_app as warehouseServerApp
from FTP import init_app as FTPApp

#app1 = warehouseServerApp()
app2 = FTPApp()

if __name__ == "__main__":
    app2.run(host="0.0.0.0")