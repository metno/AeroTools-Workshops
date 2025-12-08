output_dir = <your desired output directory>"/data"
coldata_dir = <your desired output directory>"/coldata"
exp_pi = <your name>
proj_id = <your project ID>
exp_id = <your experiment ID>


# Main configuration dictionary
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
    map_zoom="Europe",  # Zoom level. For EMEP, Europe is typically used
    regions_how="country",  # Calculates statistics for different regions. Typically "country" is used, but that does not work for satellite data
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
    colocate_time=False,
    zeros_to_nan=False,
    weighted_stats=True,
    annual_stats_constrained=True,
    harmonise_units=True,
    resample_how={
        "vmro3max": {"daily": {"hourly": "max"}}
    },  # How to handle Ozone. Used all the time in EMEP
    # Experiment Metadata
    exp_pi=exp_pi,
    proj_id=proj_id,
    exp_id=exp_id,
    exp_name="Evaluation of model data",
    exp_descr=("Evaluation of model data"),
    public=True,
)


DEFAULT_RESAMPLE_CONSTRAINTS = dict(
    yearly=dict(monthly=9),
    monthly=dict(
        daily=1,
        weekly=1,
    ),
    daily=dict(hourly=1),
)

CFG["min_num_obs"] = DEFAULT_RESAMPLE_CONSTRAINTS


# Model definitions

AEROCOM_MEAN = {
    "model_id": "AEROCOM-MEAN-2x3_AP3-CTRL",
}

NORESM = {
    "model_id": "noresm",
    "model_data_dir": "/lustre/storeB/project/fou/kl/emep/People/danielh/projects/pyaerocom/workshop/noresm/test_data/noresm",
}

MODELS = {"AEROCOM-MEAN": AEROCOM_MEAN, "NORESM": NORESM}

CFG["model_cfg"] = MODELS

# Observation definitions

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


OBS_CFG = {
    "Aeronet-m": AERONET,
}

CFG["obs_cfg"] = OBS_CFG

# Running the analysis
from pyaerocom.aeroval import EvalSetup, ExperimentProcessor
from pyaerocom import const

print(
    const.CACHEDIR
)  # Prints where to find the caching folder. Not needed but this folder should be emptied now and then, so I like to see where it is


stp = EvalSetup(**CFG)  # Makes a setup object from the dict, that PyAeroval can use
ana = ExperimentProcessor(stp)  # Makes an experiment object
res = ana.run()
