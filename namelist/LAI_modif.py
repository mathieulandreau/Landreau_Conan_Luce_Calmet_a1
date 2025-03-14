from py_wrf_arps import Proj
sim = Proj("../../", "14_20200515/", ["01","02","03","04","05"], "WRFinput", tab_test="30")
print("sim created")
#modify LAI
params = []
for dom in sim.tab_dom:
    print("LAI : dom =", dom.i_str)
    LAI_new = dom.modify_LAI("/LAB-DATA/GLiCID/projects/MesoScaleABL/DATADIR/WRF/Static_Geography_Data/LAI_VEGFRA/c_gls_LAI300_202005200000_GLOBE_PROBAV_V1.0.1.nc",\
                             modify_file = True)
#modify VEGFRA
params = []
for dom in sim.tab_dom:
    print("VEGFRA : dom =", dom.i_str)
    
    VEGFRA_new = dom.modify_VEGFRA("/LAB-DATA/GLiCID/projects/MesoScaleABL/DATADIR/WRF/Static_Geography_Data/LAI_VEGFRA/c_gls_FCOVER300_202005200000_GLOBE_PROBAV_V1.0.1.nc",\
                                   modify_file = True)
    params.append({
        "typ" : "2DH",
        "Z" : VEGFRA_new,
        "Zname" : "VEGFRA",
        "kwargs_plt" : {
            "cmap" : "Spectral_r",
        },
        "clim" : [0, 100],
        "dom" : dom.i_str,
        "savepath" : "new_VEGFRA",
    })
fig = sim.plot_fig(params)

