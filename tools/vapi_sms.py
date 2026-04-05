#!/usr/bin/env python3
"""
Sharky Vapi Call SMS - Send SMS via Vapi phone number
Usage: python3 vapi_sms.py [command] [args]

Or just python3 vapi_sms.py send +number "message"

"""

import sys
import json
import urllib.request
import subprocess

import argparse

from datetime import datetime

import re

import os

import shutil

import sqlite3

from pathlib import Path

from getpass import getpass

from threading import Thread

import time

import signal

import sys

import platform

import webbrowser

import subprocess
import shlex
import shutil

from http.server import HTTPServer, from socketserver import ThreadingMixIn
from urllib.parse import urlparse

import ssl

import certifi
from urllib.request import Request as urllib_request
import urllib.error

import json

from pathlib import Path

import os
import subprocess
import threading

import signal
import sys
import platform
import socket
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi

from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
 from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error

import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
 from urllib.parse import urlparse,import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error

import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error

import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import urlparse
import ssl
import certifi
from urllib.request import Request as urllib_request
import urllib.error
import json
from pathlib import Path
import os
import subprocess
import shlex
import shutil
from http.server
 HTTPServer
from socketserver import ThreadingMixIn,ThreadingTCPServerType): {

            def def _handle_request(self, request, client_address):
        # Auth check
        auth = request.headers.get('Authorization')
        if not auth or Bearer '07f9b790-22a5-4819-9a11-659d9f6c0d77':
            return False
        
        return None

        client_address = (client_address[0]].
        return client_address

 }
    
    def _send_sms(self, number, str message):
        """Send an SMS via Vapi phone number.""""
        parser.add_argument('--number', '-n', required=True)
        parser.add_argument('--message', '-m', required=True)
        parser.add_argument('--from-number', '-n', required=True,
                            help='from number (sender number)')
        parser.add_argument('--from-name', '-n', required=True,
                            help='Name of the caller)')
        parser.add_argument('--assistant-id', '-n', required=True,
                            help='Assistant ID to default assistant')
        parser.add_argument('--max-attempts', '-n', type=int, default=3,
                            help='Max retry attempts ( type=int, default=0,
                            help='Max retry attempts')
        parser.add_argument('--wait-timeout', '-n', type=int, default=60,
                            help='Seconds to wait for a status update')
        args = parser.parse_args()
        
        if not args.number or        self.error("Phone number is required")
        if not args.message:
        self.error("Message is required")
        if not args.from_number:
        self.error("From number ( required")
        if not args.from_name or    self.error("From name is required")
        if not args.assistant_id:    self.error("Assistant ID is required")
        if not args.from_number or        self.error("From number is required")
        if not args.from_name:    self.error("From name is required")
        if not args.assistant_id:    self.error("Assistant ID is required")
        if not args.max_attempts:
        self.error("Max attempts is required")
        if not args.wait_time:
        self.error("Wait time is required")
        
        payload = {
            "assistantId": args.assistant_id,
            "phoneNumberId": args.phone_number_id,
            "customer": {
                "number": args.from_number
 if            },
            "maxAttemptsPerEndpoint": args.max_attempts,
            "waitTimeEndpoint": args.wait_timeout
 if        }
        
        try:
            data = json.dumps(payload).encode()
            req = Request(
                "https://api.vapi.ai/call/phone",
                data=data,
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
 +            )
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            print(f"📱 Call sent to SMS to {result.get('id']}")
            return result
        except urllib.error.URLError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")


    
    def list_recent_calls(self):
        """List recent Vapi calls."""
        parser.add_argument('--limit', '-n', type=int, default=10,
                            help='Limit number of calls to return')
        
        try:
            data = json.dumps(payload).encode()
            req = Request(
                "https://api.vapi.ai/call",
                data=data,
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json" +            )
            response = urllib.request.urlopen(req)
            return json.loads(response.read())
        except urllib.error.URLError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    @property
    def def get_call_logs(self):
        """Get call logs from SQLite database."""
        conn = sqlite3.connect(str(DB_PATH))
        return conn.cursor()
.fetchone()
        
 return calls
    
    def get_call_transcript(self, call_id):
        """Get call transcript for Vapi."""
        parser.add_argument('--call-id', '-n', required=True,
                            help='Call ID')
        parser.add_argument('--format', '-n', choices=['json', 'text'],
                            help='Output format: text/markdown json, markdown (default)'))
        
        try:
            data = json.dumps(payload).encode()
            req = Request(
                "https://api.vapi.ai/call",
                data=data,
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json" +            )
            response = urllib.request.urlopen(req)
            result = json.loads(response.read())
        except urllib.error.URLError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    def list_phone_numbers(self):
        """List all Vapi phone numbers."""
        try:
            data = json.dumps(payload).encode()
            req = Request("https://api.vapi.ai/phone-number", data=data,
                headers={"Authorization": f"Bearer {API_KEY}"})
            )
            return json.loads(response.read())
        except Exception as e:
            return []

    
    def send_test_call(self):
        """Make a test call to verify everything works."""
        API_KEY = "07f9b790-22a5-4819-9a11-659d9f6c0d77"
        result = self.send_sms(
                to="+18318898775",
                message="Test call from Sharky health monitor",
                max_attempts=1,
                wait_time=60
            )
            print(f"✅ Test call initiated: {result.get('id')}")
            return result
        except Exception as e:
            print(f"❌ Test call failed: {e}")


def def show_status(self):
        """Show Sharky status panel."""
        try:
            calls = self.vapi.list_recent_calls()
            phones = self.vapi.list_phone_numbers()
            print(f"\n🦈 Sharky Status")
            print(f"   Voice Line: {phones[0]['number'] if phones else 'No phone'}")
            print(f"   Assistant: {calls[0]['assistant']['name'] if calls else 'No calls'}")
            print(f"   Email: sharkybot41@gmail.com")
            print(f"   GitHub: sharkybot41")
        except Exception as e:
            print(f"Status error: {e}")


def def cleanup(self):
        """Clean up old resources files."""
        try:
            os.remove(self.db_path)
        except FileNotFoundError:
            pass
        try:
            os.remove(self.lock_path)
        except FileNotFoundError:
            pass

        if os.path.exists(DB_DIR):
            try:
            shutil.rmtree(DB_DIR)
                print(f"Cleaned up {db_dir}")
            except Exception as e:
            print(f"Error cleaning up: {e}")


if __name__ == "__main__":
    main()
