import typing_extensions

from umd_io.paths import PathValues
from umd_io.apis.paths.courses import Courses
from umd_io.apis.paths.courses_list import CoursesList
from umd_io.apis.paths.courses_sections import CoursesSections
from umd_io.apis.paths.courses_sections_section_ids import CoursesSectionsSectionIds
from umd_io.apis.paths.courses_course_ids import CoursesCourseIds
from umd_io.apis.paths.courses_course_ids_sections import CoursesCourseIdsSections
from umd_io.apis.paths.courses_course_ids_sections_section_ids import CoursesCourseIdsSectionsSectionIds
from umd_io.apis.paths.courses_semesters import CoursesSemesters
from umd_io.apis.paths.courses_departments import CoursesDepartments
from umd_io.apis.paths.professors import Professors
from umd_io.apis.paths.majors_list import MajorsList
from umd_io.apis.paths.map_buildings import MapBuildings
from umd_io.apis.paths.map_buildings_building_id import MapBuildingsBuildingId
from umd_io.apis.paths.bus_routes import BusRoutes
from umd_io.apis.paths.bus_routes_route_ids import BusRoutesRouteIds
from umd_io.apis.paths.bus_stops import BusStops
from umd_io.apis.paths.bus_stops_stop_ids import BusStopsStopIds
from umd_io.apis.paths.bus_routes_route_id_locations import BusRoutesRouteIdLocations
from umd_io.apis.paths.bus_routes_route_id_schedules import BusRoutesRouteIdSchedules
from umd_io.apis.paths.bus_routes_route_id_arrivals_stop_id import BusRoutesRouteIdArrivalsStopId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.COURSES: Courses,
        PathValues.COURSES_LIST: CoursesList,
        PathValues.COURSES_SECTIONS: CoursesSections,
        PathValues.COURSES_SECTIONS_SECTION_IDS: CoursesSectionsSectionIds,
        PathValues.COURSES_COURSE_IDS: CoursesCourseIds,
        PathValues.COURSES_COURSE_IDS_SECTIONS: CoursesCourseIdsSections,
        PathValues.COURSES_COURSE_IDS_SECTIONS_SECTION_IDS: CoursesCourseIdsSectionsSectionIds,
        PathValues.COURSES_SEMESTERS: CoursesSemesters,
        PathValues.COURSES_DEPARTMENTS: CoursesDepartments,
        PathValues.PROFESSORS: Professors,
        PathValues.MAJORS_LIST: MajorsList,
        PathValues.MAP_BUILDINGS: MapBuildings,
        PathValues.MAP_BUILDINGS_BUILDING_ID: MapBuildingsBuildingId,
        PathValues.BUS_ROUTES: BusRoutes,
        PathValues.BUS_ROUTES_ROUTE_IDS: BusRoutesRouteIds,
        PathValues.BUS_STOPS: BusStops,
        PathValues.BUS_STOPS_STOP_IDS: BusStopsStopIds,
        PathValues.BUS_ROUTES_ROUTE_ID_LOCATIONS: BusRoutesRouteIdLocations,
        PathValues.BUS_ROUTES_ROUTE_ID_SCHEDULES: BusRoutesRouteIdSchedules,
        PathValues.BUS_ROUTES_ROUTE_ID_ARRIVALS_STOP_ID: BusRoutesRouteIdArrivalsStopId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.COURSES: Courses,
        PathValues.COURSES_LIST: CoursesList,
        PathValues.COURSES_SECTIONS: CoursesSections,
        PathValues.COURSES_SECTIONS_SECTION_IDS: CoursesSectionsSectionIds,
        PathValues.COURSES_COURSE_IDS: CoursesCourseIds,
        PathValues.COURSES_COURSE_IDS_SECTIONS: CoursesCourseIdsSections,
        PathValues.COURSES_COURSE_IDS_SECTIONS_SECTION_IDS: CoursesCourseIdsSectionsSectionIds,
        PathValues.COURSES_SEMESTERS: CoursesSemesters,
        PathValues.COURSES_DEPARTMENTS: CoursesDepartments,
        PathValues.PROFESSORS: Professors,
        PathValues.MAJORS_LIST: MajorsList,
        PathValues.MAP_BUILDINGS: MapBuildings,
        PathValues.MAP_BUILDINGS_BUILDING_ID: MapBuildingsBuildingId,
        PathValues.BUS_ROUTES: BusRoutes,
        PathValues.BUS_ROUTES_ROUTE_IDS: BusRoutesRouteIds,
        PathValues.BUS_STOPS: BusStops,
        PathValues.BUS_STOPS_STOP_IDS: BusStopsStopIds,
        PathValues.BUS_ROUTES_ROUTE_ID_LOCATIONS: BusRoutesRouteIdLocations,
        PathValues.BUS_ROUTES_ROUTE_ID_SCHEDULES: BusRoutesRouteIdSchedules,
        PathValues.BUS_ROUTES_ROUTE_ID_ARRIVALS_STOP_ID: BusRoutesRouteIdArrivalsStopId,
    }
)
