import typing_extensions

from umd_io.apis.tags import TagValues
from umd_io.apis.tags.courses_api import CoursesApi
from umd_io.apis.tags.professors_api import ProfessorsApi
from umd_io.apis.tags.bus_api import BusApi
from umd_io.apis.tags.map_api import MapApi
from umd_io.apis.tags.majors_api import MajorsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.COURSES: CoursesApi,
        TagValues.PROFESSORS: ProfessorsApi,
        TagValues.BUS: BusApi,
        TagValues.MAP: MapApi,
        TagValues.MAJORS: MajorsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.COURSES: CoursesApi,
        TagValues.PROFESSORS: ProfessorsApi,
        TagValues.BUS: BusApi,
        TagValues.MAP: MapApi,
        TagValues.MAJORS: MajorsApi,
    }
)
