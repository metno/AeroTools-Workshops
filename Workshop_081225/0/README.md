# Preparations

Below is a list of simple preparations to complete before the workshop. Don’t worry if something doesn’t work, but if you manage to finish every step, you’ll be ready for the workshop.

If you encounter any issues, please contact me, Jan or IT.

## Accessing PPI

Everyone should be able to connect to PPI via SSH. If you cannot, please contact me or IT before the workshop.

To connect, use:

```
ssh ppi-r8login-b1.int.met.no
```

## Checking the Aerotools Module

This step will verify that you can run Pyaerocom. On PPI, enter:

```
module load /modules/MET/rhel8/user-modules/fou-kl/aerotools/aerotools
```

Then run:

```
pya --help
```

You should see options for Pyaerocom.

## Creating a Folder for Aeroval

On PPI, navigate to `/lustre/storeB/project/fou/kl/emep/Web/AeroVal/` and try to create a folder named after your username:

```
cd /lustre/storeB/project/fou/kl/emep/Web/AeroVal/
mkdir <your username>
```
