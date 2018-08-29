"""plots.py

"""

import openmc

import beavrs.constants as c


class Plots(object):

  def __init__(self, mats):
    """ Creates BEAVRS plots"""

    self.mats = mats

    self.plots = []

    self._set_colors()
    self._add_plots()

  def _set_colors(self):

    self.colors_mat = {
      self.mats['Borated Water']:      [198, 226, 255],   # water:  light blue
      self.mats['Water SPN']:          [176, 196, 222],   # water spn: steel blue
      self.mats['Inconel 718']:        [101, 101, 101],   # inconel dim gray
      self.mats['Carbon Steel']:       [ 50,  50,  50],   # carbons light black
      self.mats['Zircaloy 4']:         [111, 111, 111],   # zirc:   dark gray
      self.mats['SS304']:              [  0,   0,   0],   # ss304:  black
      self.mats['SS304 SPN']:          [112, 128, 144],   # ss spn: slate gray
      self.mats['Air']:                [255, 255, 255],   # air:    white
      self.mats['Helium']:             [255, 218, 185],   # helium: light orange
      self.mats['Borosilicate Glass']: [  0, 255,   0],   # BR:     green
      self.mats['Ag-In-Cd']:           [255,   0,   0],   # AIC:    bright red
      self.mats['B4C']:                [200,  50,  50],   # B4C:    dark red
      self.mats['Fuel 1.6%']:          [142,  35,  35],   # 1.6:    light red
      self.mats['Fuel 2.4%']:          [255, 215,   0],   # 2.4:    gold
      self.mats['Fuel 3.1%']:          [  0,   0, 128],   # 3.1:    dark blue
    }

  def _add_plots(self):

    H = c.struct_HighestExtent-c.struct_LowestExtent
    res = 1000

    # BPRA positions
    plot = openmc.Plot()
    plot.filename = 'bpra_positions'
    plot.color_by = 'material'
    plot.basis = 'xy'
    plot.origin = [0, 0, H/2]
    plot.width = [c.rpvOR*2, c.rpvOR*2]
    plot.pixels = [res, res]
    plot.mask_components = [self.mats['Borosilicate Glass']]
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'radial_cells_midplane'
    plot.color_by = 'material'
    plot.basis = 'xy'
    plot.origin = [0, 0, H/2]
    plot.width = [c.rpvOR*2, c.rpvOR*2]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'radial_mats_midplane'
    plot.color_by = 'material'
    plot.basis = 'xy'
    plot.origin = [0, 0, H/2]
    plot.width = [c.rpvOR*2, c.rpvOR*2]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'radial_mats_grid1_center'
    plot.color_by = 'material'
    plot.basis = 'xy'
    plot.origin = [0, 0, c.grid1_bot+(c.grid1_top - c.grid1_bot)/2]
    plot.width = [c.rpvOR*2, c.rpvOR*2]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'radial_mats_grid4_center'
    plot.color_by = 'material'
    plot.basis = 'xy'
    plot.origin = [0, 0, c.grid4_bot+(c.grid4_top - c.grid4_bot)/2]
    plot.width = [c.rpvOR*2, c.rpvOR*2]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'axial_mats_row_8'
    plot.color_by = 'material'
    plot.basis = 'xz'
    plot.origin = [0, 0, H/2]
    plot.width = [H, H]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'axial_mats_row_8_topzoom'
    plot.color_by = 'material'
    plot.basis = 'xz'
    plot.origin = [0, 0, H/2 + H/4]
    plot.width = [H/2, H/2]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'axial_mats_row_8_topzoom2'
    plot.color_by = 'material'
    plot.basis = 'xz'
    plot.origin = [0, 0, H/2 + H/3]
    plot.width = [H/4, H/4]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'axial_mats_row_8_topzoom3'
    plot.color_by = 'material'
    plot.basis = 'xz'
    plot.origin = [0, 0, c.fuel_Rod_top]
    plot.width = [H/8, H/8]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'axial_mats_row_8_botzoom'
    plot.color_by = 'material'
    plot.basis = 'xz'
    plot.origin = [0, 0, H/2 - H/4]
    plot.width = [H/2, H/2]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'axial_mats_row_8_botzoom2'
    plot.color_by = 'material'
    plot.basis = 'xz'
    plot.origin = [0, 0, H/2 - H/3]
    plot.width = [H/4, H/4]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'axial_mats_row_8_botzoom3'
    plot.color_by = 'material'
    plot.basis = 'xz'
    plot.origin = [0, 0, c.fuel_Rod_bot]
    plot.width = [H/8, H/8]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'grid5_mats_H7'
    plot.color_by = 'material'
    plot.basis = 'xy'
    plot.origin = [0, c.latticePitch, c.grid5_bot+(c.grid5_top-c.grid5_bot)/2]
    plot.width = [c.latticePitch, c.latticePitch]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'grid8_mats_J14'
    plot.color_by = 'material'
    plot.basis = 'xy'
    plot.origin = [-c.latticePitch+c.latticePitch/3, \
                    -6*c.latticePitch+c.latticePitch/3, \
                    c.grid8_bot+(c.grid8_top-c.grid8_bot)/2]
    plot.width = [c.latticePitch, c.latticePitch]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'grid5_mats_J14'
    plot.color_by = 'material'
    plot.basis = 'xy'
    plot.origin = [-c.latticePitch+c.latticePitch/3, \
                    -6*c.latticePitch+c.latticePitch/3, \
                    c.grid5_bot+(c.grid5_top-c.grid5_bot)/2]
    plot.width = [c.latticePitch, c.latticePitch]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'midplane_mats_J14'
    plot.color_by = 'material'
    plot.basis = 'xy'
    plot.origin = [-c.latticePitch+c.latticePitch/3, \
                    -6*c.latticePitch+c.latticePitch/3, H/2]
    plot.width = [c.latticePitch, c.latticePitch]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    h = 4*(c.struct_LowerNozzle_top - c.struct_SupportPlate_bot)/c.latticePitch
    plot = openmc.Plot()
    plot.filename = 'J8_axial_bot'
    plot.color_by = 'material'
    plot.basis = 'xz'
    plot.origin = [0, c.latticePitch, c.struct_LowerNozzle_top]
    plot.width = [c.latticePitch, h]
    plot.pixels = [res, int(res*h)]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    h = 4*(c.struct_UpperNozzle_top - c.fuel_Rod_top)/c.latticePitch
    plot = openmc.Plot()
    plot.filename = 'J8_axial_top'
    plot.color_by = 'material'
    plot.basis = 'xz'
    plot.origin = [0, c.latticePitch, c.fuel_Rod_top]
    plot.width = [c.latticePitch, h]
    plot.pixels = [res, int(res*h)]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    plot = openmc.Plot()
    plot.filename = 'J8_nozzle'
    plot.color_by = 'material'
    plot.basis = 'xy'
    plot.origin = [0, c.latticePitch, c.struct_SupportPlate_bot + 2.0]
    plot.width = [c.latticePitch, c.latticePitch]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)

    h = 2*(c.struct_UpperNozzle_top - c.fuel_Rod_top)
    plot = openmc.Plot()
    plot.filename = 'H8_axial_top'
    plot.color_by = 'material'
    plot.basis = 'xz'
    plot.origin = [0, c.latticePitch, c.fuel_Rod_top]
    plot.width = [h, h]
    plot.pixels = [res, res]
    plot.colors = self.colors_mat
    self.plots.append(plot)
