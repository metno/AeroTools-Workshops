import pyaerocom as pya
import matplotlib.pyplot as plt

from pyaerocom.io.pyaro.pyaro_config import PyaroConfig

print(pya.const.CACHEDIR)
# breakpoint()

data_id = "nilupmfebas"
url = "/home/danielh/Downloads/EIMPs_winter2017-2018_data/EIMPs_winter_2017_2018_ECOC_Levo/"

config = PyaroConfig(
    name="pmf",
    data_id=data_id,
    filename_or_obj_or_url=url,
    filters={"variables": {"include": ["pm10#organic_carbon#ug C m-3"]}},
    name_map={"pm10#organic_carbon#ug C m-3": "concCec"},
)

rp = pya.io.ReadUngridded(configs=[config])

data = rp.read()

stations = data.to_station_data_all()
breakpoint()
