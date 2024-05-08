# EMEP AeroTools workshop

Here you can find the files associated with the EMEP AeroTools workshop, first held 22.03.2024. The lectures assume that you have access to Lustre/PPI

Each folder holds a separate lecture, in the form of a jupyter notebook. Most of the notebooks can be used to run the tutorial code directly, while some notebooks have command line code, which has to be run in the terminal. 

1. [What is AeroTools?](1/what_is_aerotools.ipynb)
2. [Readying the EMEP data](2/emep_data.ipynb)
3. [Using PyAeroval](3/pyaeroval.ipynb)
4. [Adding Custom Variables](4/custom_vars.ipynb)
5. [Uploading and viewing on Aeroval](5/Aeroval.ipynb)


## Running the notebooks from Lustre
We will be running all the code in this workshop on lustre. While it is possible to read the notebooks locally and copy the code to PPI, you can also host the notebooks on PPI

Log onto PPI (`ssh ppi-r8login-b1.int.met.no`), then activate AeroTools

```
module load /modules/MET/rhel8/user-modules/fou-kl/aerotools/pya-v2024.03.NorESM.conda
```
After easter it should be enough with

```
module load /modules/MET/rhel8/user-modules/fou-kl/aerotools/aerotools
```
Clone this repository:
```
git clone https://github.com/metno/AeroTools-Workshops.git
cd AeroTools-Workshops
```
Then run 
```
jupyter notebook --no-browser --ip=$(hostname -f)
```

In the output, you should see two urls. Copy the url starting with `ppi-r8login-b1.int.met.no` into your browser. You should now see the notebooks in your browser. Open the first tutorial by locating `EMEP/1/what_is_aerotools.ipynb`.

## NOTE on AeroTools module

During this workshop we have run everything though a custom module. After easter, NAC will be included in the AeroTools module, meaning you can run 

```
module load /modules/MET/rhel8/user-modules/fou-kl/aerotools/aerotools
```

instead. The main difference is that on the AeroTools module, all commands start with `pya_`, i.e.

```
# For jupyter notebook
pya_jupyter notebook --no-browser --ip=$(hostname -f)

# For NAC
pya_nac --help
```

So just keep that in mind...
