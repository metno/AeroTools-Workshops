from pyaerocom.io.pyaro.pyaro_config import PyaroConfig


############################
### Experiment Information. CHANGE THIS TO YOUR INFO!!!!!!
###########################
output_dir = "/home/danielh/Documents/pyaerocom/aeroval/data"
coldata_dir = "/home/danielh/Documents/pyaerocom/aeroval/coldata"
exp_pi = "Daniel Heinesen"
proj_id = "workshop"
exp_id = "noresmppi"


"""
Pyaro Setup
"""

data_name = "aeronettest"  # Unique name for this dataset. Can be set freely
data_id = "aeronetsunreader"  # ID for a specific reader.
url = "https://aeronet.gsfc.nasa.gov/data_push/V3/All_Sites_Times_Daily_Averages_AOD20.zip"  # Url or file location of the data


config = PyaroConfig(
    name=data_name,
    data_id=data_id,
    filename_or_obj_or_url=url,
    filters={  # Filters applied to the data before reading. Can reduce reading time significantly
        "variables": {
            "include": ["AOD_550nm"],
        }
    },
    name_map={  # Each reader can have its own names for variables, so here you should do the mapping to aerocom names
        "AOD_550nm": "od550aer",
    },
)


"""
Setup of config dict, with global options
"""

CFG = dict(
    # Output directories
    json_basedir=output_dir,
    coldata_basedir=coldata_dir,
    # Run options
    reanalyse_existing=True,  # if True, existing colocated data files will be deleted
    raise_exceptions=True,  # if True, the analysis will stop whenever an error occurs
    clear_existing_json=False,  # if True, deletes previous output before running
    # Map Options
    add_model_maps=False,  # Adds a plot of the whole map. Very slow!!!
    only_model_maps=False,  # Adds only plot above, without any other evaluation
    filter_name="ALL-wMOUNTAINS",  # Regional filter for analysis
    map_zoom="World",  # Zoom level. For EMEP, Europe is typically used
    # regions_how="country",        # Calculates statistics for different regions. Typically "country" is used, but that does not work for satellite data
    # Time and Frequency Options
    ts_type="monthly",  # Colocation frequency (no statistics in higher resolution can be computed)
    freqs=["monthly", "yearly"],  # Frequencies that are evaluated
    main_freq="monthly",  # Frequency that is displayed when opening webpage
    periods=[
        "2010"
    ],  # List of years or periods of years that are evaluated. E.g. "2005" or "2001-2020"
    # Statistical Options
    obs_remove_outliers=False,
    model_remove_outliers=False,
    colocate_time=True,
    zeros_to_nan=False,
    weighted_stats=True,
    annual_stats_constrained=True,
    harmonise_units=True,
    # resample_how={"vmro3max": {"daily": {"hourly": "max"}}}, # How to handle Ozone. Used all the time in EMEP
    # Experiment Metadata
    exp_pi=exp_pi,
    proj_id=proj_id,
    exp_id=exp_id,
    exp_name="Evaluation of NorESM data",
    exp_descr=("Evaluation of NorESM data"),
    public=True,
)


DEFAULT_RESAMPLE_CONSTRAINTS = dict(
    yearly=dict(monthly=9),
    monthly=dict(
        daily=7,
        weekly=3,
    ),
    daily=dict(hourly=18),
)

CFG["min_num_obs"] = DEFAULT_RESAMPLE_CONSTRAINTS


"""
Model Setup
"""

AEROCOM_MEAN = {
    "model_id": "AEROCOM-MEAN-2x3_AP3-CTRL",
}


NORESM = {
    "model_id": "noresm",
    "model_data_dir": "/lustre/storeB/project/fou/kl/emep/People/danielh/projects/pyaerocom/workshop/noresm/test_data/noresm",
}


MODELS = {"AEROCOM-MEAN": AEROCOM_MEAN, "NORESM": NORESM}

CFG["model_cfg"] = MODELS


"""
Observation Setup
"""
AERONET = dict(
    obs_id="AeronetSunV3Lev2.daily",  # Observation ID of know network
    web_interface_name="Aeronet-m",  # Name that is displayed on the webpage
    obs_vars=["od550aer"],  # List of variables that is to be evaluated
    obs_vert_type="Column",  # Observation level
    ts_type="monthly",  # Frequency of read observations. Evaluation can not be finer than this, for this network
    obs_filters={
        "latitude": [
            30,
            82,
        ],  # Observation filters. Each network can have own filters. Here I've uses lat, lon and alt as examples
        "longitude": [-30, 90],
        "altitude": [-200, 5000],
    },
)


MODIS = dict(
    obs_id="MODIS6.1terra.DT.DP.mean",  # Observation ID of know network
    web_interface_name="Modis",  # Name that is displayed on the webpage
    obs_vars=["od550aer"],  # List of variables that is to be evaluated
    obs_vert_type="Column",  # Observation level
    regrid_res_deg={  # Regridding of the data
        "lat_res_deg": 5,
        "lon_res_deg": 5,
    },
    ts_type="daily",  # Frequency of read observations. Evaluation can not be finer than this, for this network
)


PYARO = dict(
    obs_id=config.name,  # Must be set to the name found in the config
    obs_config=config,  # The pyaro config
    web_interface_name="Pyaro-d",  # Name that is displayed on the webpage
    obs_vars=["od550aer"],  # List of variables that is to be evaluated
    obs_vert_type="Column",  # Observation level
    ts_type="daily",  # Frequency of read observations. Evaluation can not be finer than this, for this network
)


OBS_CFG = {"Pyaro-d": PYARO, "Aeromet-m": AERONET, "MODIS": MODIS}

CFG["obs_cfg"] = OBS_CFG


if __name__ == "__main__":

    from pyaerocom.aeroval import EvalSetup, ExperimentProcessor
    from pyaerocom import const

    print(
        const.CACHEDIR
    )  # Prints where to find the caching folder. Not needed but this folder should be emptied now and then, so I like to see where it is

    stp = EvalSetup(**CFG)  # Makes a setup object from the dict, that PyAeroval can use
    ana = ExperimentProcessor(stp)  # Makes an experiment object
    res = ana.run()  # Runs the experiment

    # Example on how to run an experiment with only certain models, obs, and variables. Often used to run only parts of the experiment that has changed
    # res = ana.run(model_name=["NORESM"], obs_name=["Modis"], var_list=["od550aer"])
