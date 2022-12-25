# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from umd_io.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    COURSES = "/courses"
    COURSES_LIST = "/courses/list"
    COURSES_SECTIONS = "/courses/sections"
    COURSES_SECTIONS_SECTION_IDS = "/courses/sections/{section_ids}"
    COURSES_COURSE_IDS = "/courses/{course_ids}"
    COURSES_COURSE_IDS_SECTIONS = "/courses/{course_ids}/sections"
    COURSES_COURSE_IDS_SECTIONS_SECTION_IDS = "/courses/{course_ids}/sections/{section_ids}"
    COURSES_SEMESTERS = "/courses/semesters"
    COURSES_DEPARTMENTS = "/courses/departments"
    PROFESSORS = "/professors"
    MAJORS_LIST = "/majors/list"
    MAP_BUILDINGS = "/map/buildings"
    MAP_BUILDINGS_BUILDING_ID = "/map/buildings/{building_id}"
    BUS_ROUTES = "/bus/routes"
    BUS_ROUTES_ROUTE_IDS = "/bus/routes/{route_ids}"
    BUS_STOPS = "/bus/stops"
    BUS_STOPS_STOP_IDS = "/bus/stops/{stop_ids}"
    BUS_ROUTES_ROUTE_ID_LOCATIONS = "/bus/routes/{route_id}/locations"
    BUS_ROUTES_ROUTE_ID_SCHEDULES = "/bus/routes/{route_id}/schedules"
    BUS_ROUTES_ROUTE_ID_ARRIVALS_STOP_ID = "/bus/routes/{route_id}/arrivals/{stop_id}"
