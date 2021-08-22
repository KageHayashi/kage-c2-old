from multiprocessing.context import Process
from kage.core.common import *

import threading, sys, logging
import flask

SENTINELS = {}
PORTS_IN_USE = []

def killAllSentinels():
    for sentinel in SENTINELS.values():
        sentinel.kill()

class Sentinel():
    def __init__(self, name, port):
        self._name = name
        self._port = port
        self._status = "Inactive"

        self.app = flask.Flask(name)

        SENTINELS[name] = self
        PORTS_IN_USE.append(port)
        
        @self.app.route("/")
        def index():
            return "hi"

        @self.app.route("/register", methods=["POST"])
        def registerShadow():
            '''Register a Shadow (agent) with name'''
            if flask.request.method == 'POST':
                data = flask.request.get_json()
                # Create Shadow object and store in database
                # db.storeShadow(shadow)
                return "OK."
            else:
                return "Error. Only POST requests are allowed!"
            
        @self.app.route("/tasks/<name>", methods=["GET"])
        def viewTasks():
            '''The endpoint for Shadows to view their assigned tasks'''
            pass
            
        @self.app.route("/results/<name>", methods=["POST"])
        def sendResults():
            '''The endpoint for Shadows to send the results of their tasks'''
            pass
    
    def _update_status(self, status: str) -> None:
        self._status = status

    def start(self) -> None:
        '''
        Creates a new process and thread to run the server daemon. 
        '''
        self.server_process = Process(target=self.app.run, args=("127.0.0.1", str(self._port)))
        
        # Disable cli logging
        cli = sys.modules['flask.cli']
        cli.show_server_banner = lambda *x: None
        log = logging.getLogger('werkzeug')
        log.disabled = True

        self.daemon_thread = threading.Thread(name = self._name,
                                              target = self.server_process.start,
                                              args=[])
        
        self.daemon_thread.start()
        self._update_status("Active")

    def kill(self) -> None:
        '''
        Kills ther server by terminating the server process and daemon thread
        '''
        printInfo(f"Killing Sentinel '{self._name}'")
        self.server_process.terminate()
        self.server_process = None
        self.daemon_thread = None