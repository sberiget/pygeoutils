"""Top-level package for PyGeoUtils."""
from importlib.metadata import PackageNotFoundError, version

from pygeoutils._utils import get_gtiff_attrs, get_transform, transform2tuple, xd_write_crs
from pygeoutils.exceptions import (
    EmptyResponseError,
    InputRangeError,
    InputTypeError,
    InputValueError,
    MatchingCRSError,
    MissingAttributeError,
    MissingColumnError,
    MissingCRSError,
)
from pygeoutils.geotools import (
    Coordinates,
    GeoSpline,
    break_lines,
    coords_list,
    geo2polygon,
    geometry_list,
    geometry_reproject,
    line_curvature,
    make_spline,
    multi2poly,
    nested_polygons,
    query_indices,
    smooth_linestring,
    snap2nearest,
    spline_curvature,
    spline_linestring,
)
from pygeoutils.print_versions import show_versions
from pygeoutils.pygeoutils import (
    arcgis2geojson,
    geodf2xarray,
    gtiff2vrt,
    gtiff2xarray,
    json2geodf,
    xarray2geodf,
    xarray_geomask,
)

try:
    __version__ = version("pygeoutils")
except PackageNotFoundError:
    __version__ = "999"

__all__ = [
    "arcgis2geojson",
    "break_lines",
    "geo2polygon",
    "geometry_list",
    "get_gtiff_attrs",
    "get_transform",
    "gtiff2xarray",
    "gtiff2vrt",
    "snap2nearest",
    "xarray2geodf",
    "multi2poly",
    "geodf2xarray",
    "json2geodf",
    "transform2tuple",
    "xd_write_crs",
    "xarray_geomask",
    "coords_list",
    "Coordinates",
    "query_indices",
    "nested_polygons",
    "geometry_reproject",
    "GeoSpline",
    "make_spline",
    "spline_linestring",
    "smooth_linestring",
    "line_curvature",
    "spline_curvature",
    "InputTypeError",
    "InputValueError",
    "InputRangeError",
    "MissingAttributeError",
    "MissingColumnError",
    "MissingCRSError",
    "MatchingCRSError",
    "UnprojectedCRSError",
    "EmptyResponseError",
    "show_versions",
]
