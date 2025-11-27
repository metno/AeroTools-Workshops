# AeroTools workshop

Here you can find the files associated with the AeroTools workshop, first held 08.12.2025. The lectures assume that you have access to Lustre/PPI

Each folder holds a separate lecture, in the form of a jupyter notebook. Most of the notebooks can be used to run the tutorial code directly, while some notebooks have command line code, which has to be run in the terminal. 

0. [Preparations](0/README.md)
1. [What is AeroTools?](1/what_is_aerotools.ipynb)
2. [Using PyAeroval](2/pyaeroval.ipynb)
3. [Using PyAeroval 2](3/advanced.ipynb)
4. [Uploading and viewing on Aeroval](4/Aeroval.ipynb)


## Running the notebooks from Lustre
We will be running all the code in this workshop on lustre. While it is possible to read the notebooks locally and copy the code to PPI, you can also host the notebooks on PPI

Log onto PPI (`ssh ppi-r8login-b1.int.met.no`), then activate AeroTools


```
module load /modules/MET/rhel8/user-modules/fou-kl/aerotools/aerotools
```
Clone this repository:
```
git clone git@github.com:metno/AeroTools-Workshops.git
cd AeroTools-Workshops
```
Then run 
```
pya_jupyter notebook --no-browser --ip=$(hostname -f)
```

In the output, you should see two urls. Copy the url starting with `ppi-r8login-b1.int.met.no` into your browser. You should now see the notebooks in your browser. Open the first tutorial by locating `Workshop_081225/1/what_is_aerotools.ipynb`.
