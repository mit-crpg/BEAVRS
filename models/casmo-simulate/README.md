# CASMO/Simulate Inputs for BEAVRS

Input files for CASMO-5/Simulate-3 at HZP and HFP for Cycle 1 and Cycle 2 used to generate radial reaction rates

## Running
```bash
# Run CASMO on assemblies
for f in `ls c5*inp`
do
  cas5 $f
done

# Run cmslink to create library file
cmslink cms1.inp

# Run Simulate on full-core HZP/HFP
simulate3 simulate_full_hzp.inp
simulate3 simulate_hzp_noIT_ft.inp
simulate3 simulate_hfp_noIT_ft.inp
simulate3 simulate_hzp_noIT_cyc2_ft.inp
simulate3 simulate_hfp_noIT_cyc2_ft.inp
```
