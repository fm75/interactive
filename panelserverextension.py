_efrom subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the panel_exp.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "panel_exp.ipynb", "--allow-websocket-origin=*"])
