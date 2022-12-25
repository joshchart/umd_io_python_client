# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from umd_io.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from umd_io.model.building import Building
from umd_io.model.bus_schedule import BusSchedule
from umd_io.model.course import Course
from umd_io.model.error import Error
from umd_io.model.major import Major
from umd_io.model.meeting import Meeting
from umd_io.model.professor import Professor
from umd_io.model.route import Route
from umd_io.model.section import Section
from umd_io.model.stop import Stop
