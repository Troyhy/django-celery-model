#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "djcelery_model.tests.settings"
    )
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
