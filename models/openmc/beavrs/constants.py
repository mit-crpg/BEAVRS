
import math

############## Material paramters ##############

h2oDens = 0.73986
nominalBoronPPM = 975

############## Geometry paramters ##############

## Steps withdrawn for each RCCA bank
rcca_bank_steps_withdrawn = {
    'A': 228,
    'B': 228,
    'C': 228,
    'D':   0, # bite position is bank D at 213 steps withdrawn
    'SA': 228,
    'SB': 228,
    'SC': 228,
    'SD': 228,
    'SE': 228,
}
rcca_banks = rcca_bank_steps_withdrawn.keys()

## pincell parameters
pelletOR        = 0.39218  #
cladIR          = 0.40005  #
cladOR          = 0.45720  #
rodGridSide_tb  = 1.22030  #
rodGridSide_i   = 1.22098  #
guideTubeIR     = 0.56134  #
guideTubeOR     = 0.60198  #
guideTubeDashIR = 0.50419  #
guideTubeDashOR = 0.54610  #
rcca_clad_OR    = 0.48387  # ML033530020 page 15
rcca_clad_IR    = 0.38608  # ML033530020 page 15
rcca_b4c_OR     = 0.37338  # ML033530020 page 15
rcca_aic_OR     = 0.38227  # ML033530020 page 15
rcca_spacer_OR  = 0.37845  # ML033530020 page 15
rcca_spring_OR  = 0.06459  # Assumed same as fuel
burnabs1        = 0.21400  #
burnabs2        = 0.23051  #
burnabs3        = 0.24130  #
burnabs4        = 0.42672  #
burnabs5        = 0.43688  #
burnabs6        = 0.48387  #
instrTubeIR     = 0.43688  # no source
instrTubeOR     = 0.48387  # no source
plenumSpringOR  = 0.06459  # frapcon source - see beavrs_spring.ods

## lattice parameters
pinPitch        =  1.25984 #
latticePitch    = 21.50364 #
gridstrapSide   = 21.49595 #

## <!--- axials copied straight from rod_axials.ods

# Core Structures
struct_LowestExtent             =      0.00000   #
struct_SupportPlate_bot         =      20.0000   # arbitrary amount of water below core
struct_SupportPlate_top         =      25.0000   # guessed
struct_LowerNozzle_bot          =      25.0000   # same as struct_SupportPlate_top
struct_LowerNozzle_top          =      35.0000   # approx from ** NDR of 4.088in for lower nozzle height
struct_LowestExtent_2d           =      220.000   # arbitrary lower slice for 2D problem
struct_HighestExtent_2d          =      230.000   # arbitrary upper slice for 2D problem
struct_UpperNozzle_bot          =      423.049   # fig 4.2-3 from Watts Bar Unit 2 safety analysis report
struct_UpperNozzle_top          =      431.876   # fig 4.2-3 from Watts Bar Unit 2 safety analysis report
struct_HighestExtent            =      460.000   # arbitrary amount of water above core

# Fuel Rod
fuel_Rod_bot                    =      35.0000   # same as struct_LowerNozzle_top
fuel_LowerFitting_bot           =      35.0000   # ML033530020 Fig 2-7
fuel_LowerFitting_top           =      36.7480   # ML033530020 Fig 2-7
fuel_ActiveFuel_bot             =      36.7480   # ML033530020 Fig 2-7
fuel_ActiveFuel_top             =      402.508   # ML033530020 Fig 2-7
fuel_Plenum_bot                 =      402.508   # ML033530020 Fig 2-7
fuel_Plenum_top                 =      417.164   # ML033530020 Fig 2-7
fuel_UpperFitting_bot           =      417.164   # ML033530020 Fig 2-7
fuel_UpperFitting_top           =      419.704   # ML033530020 Fig 2-7
fuel_Rod_top                    =      419.704   # ML033530020 Fig 2-7

# RCCAs (0 steps withdraw, i.e., fully inserted)
rcca_Rod_bot                    =      39.9580   # ML033530020 Fig 2-8
rcca_LowerFitting_bot           =      39.9580   # ML033530020 Fig 2-8
rcca_LowerFitting_top           =      41.8280   # ML033530020 Fig 2-8
rcca_AIC_bot                    =      41.8280   # ML033530020 Fig 2-8
rcca_AIC_top                    =      143.428   # ML033530020 Fig 2-8
rcca_B4C_bot                    =      143.428   # ML033530020 Fig 2-8
rcca_B4C_top                    =      402.508   # ML033530020 Fig 2-8
rcca_Spacer_bot                 =      402.508   # ML033530020 Fig 2-8
rcca_Spacer_top                 =      403.778   # ML033530020 Fig 2-8
rcca_Plenum_bot                 =      403.778   # ML033530020 Fig 2-8
rcca_Plenum_top                 =      415.558   # ML033530020 Fig 2-8
rcca_Rod_top                    =      460.000   # same as struct_HighestExtent
rcca_StepWidth                  =      1.58193   # Active height divided into 228 steps

# BPRAs
bpra_Rod_bot                    =      38.6600   # ML033530020 Fig 2-9
bpra_LowerFitting_bot           =      38.6600   # ML033530020 Fig 2-9
bpra_LowerFitting_top           =      40.5580   # ML033530020 Fig 2-9
bpra_Active_bot                 =      40.5580   # ML033530020 Fig 2-9
bpra_Active_top                 =      401.238   # ML033530020 Fig 2-9
bpra_Plenum_bot                 =      401.238   # ML033530020 Fig 2-9
bpra_Plenum_top                 =      421.532   # ML033530020 Fig 2-9
bpra_Rod_top                    =      431.876   # same as struct_UpperNozzle_top

# Guide Tube
gt_Rod_bot                      =      35.0000   # same as fuel_Rod_bot
gt_Dashpot_bot                  =      35.0000   #
gt_Dashpot_top                  =      39.9580   # same as rcca_Rod_bot for full insertion
gt_Upper_bot                    =      39.9580   #
gt_Upper_top                    =      423.049   # same as struct_UpperNozzle_bot
gt_Rod_top                      =      423.049   #

# Intrument Tube
instr_Rod_bot                   =      35.0000   # same as fuel_Rod_bot
instr_Rod_top                   =      423.049   # same as struct_UpperNozzle_bot

# Grid Spacers (centers provided by utiliy)  (heights 1.65 top/bottom, 2.25 intermediate)
grid1_bot                       =      37.1621   #
grid1_top                       =      40.5200   #
grid2_bot                       =      98.0250   #
grid2_top                       =      103.740   #
grid3_bot                       =      150.222   #
grid3_top                       =      155.937   #
grid4_bot                       =      202.419   #
grid4_top                       =      208.134   #
grid5_bot                       =      254.616   #
grid5_top                       =      260.331   #
grid6_bot                       =      306.813   #
grid6_top                       =      312.528   #
grid7_bot                       =      359.010   #
grid7_top                       =      364.725   #
grid8_bot                       =      411.806   #
grid8_top                       =      415.164   #

# data for nozzle and support plate region
n_nozzle_pins = 264            # number of pins
# volume fractions from ML033530020 (table 2-3)
nozzle_water_vol_frac = 0.8280 # water volume fraction
nozzle_ss_vol_frac    = 0.1720 # stainless steel volume fraction

## -- axials copied straight from rod_axials.ods -->

## radial paramters
coreBarrelIR       = 187.9600 # Fig 2.1 from NDR 2-8
coreBarrelOR       = 193.6750 # Fig 2.1 from NDR 2-8
baffleWidth        =   2.2225 # Fig 2.1 from NDR 2-8
baffleWaterGap     =   0.1627 # ML033530020
linerIR            =  219.150 # ML033530020
rpvIR              =  219.710 # ML033530020
rpvOR              =  241.300 # ML033530020

neutronShieldIR    = 194.840 # ML033530020
neutronShieldOR    = 201.630 # ML033530020
neutronShield_NWbot_SEtop = {'a': 1, 'b': math.tan(math.pi/3 + math.pi/180), 'c': 0, 'd': 0}
neutronShield_NWtop_SEbot = {'a': 1, 'b': math.tan(math.pi/6 - math.pi/180), 'c': 0, 'd': 0}
neutronShield_NEbot_SWtop = {'a': 1, 'b': math.tan(-math.pi/3 - math.pi/180), 'c': 0, 'd': 0}
neutronShield_NEtop_SWbot = {'a': 1, 'b': math.tan(-math.pi/6 + math.pi/180), 'c': 0, 'd': 0}
