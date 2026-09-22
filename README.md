# RoCarp-CHM-AGB

**Canopy height and aboveground biomass of the Romanian Carpathian forests at 10 m**

> **Status — dataset in preparation.** The maps described on this page are being
> finalised. Public release is expected in **Q1 2027**, together with the
> accompanying peer-reviewed publication. This repository is the permanent entry
> point: the download links and the dataset DOI will appear here.
>
> **Landing page:** https://GITHUB-USER.github.io/rocarp-chm-agb/

---

## What this is

RoCarp-CHM-AGB is a wall-to-wall, 10 m resolution mapping of two forest structural
variables — **canopy height (CHM)** and **aboveground biomass (AGB)** — across the
forests of the Romanian Carpathian arc.

The maps are produced by machine-learning models calibrated against spaceborne LiDAR
from **NASA GEDI** (L2A relative height metrics for canopy height, L4A for aboveground
biomass density) and applied to a multi-source predictor stack combining optical,
C-band SAR, L-band SAR and terrain data.

Every map is distributed with an explicit uncertainty layer, so that users can
distinguish the reproducible signal from the component that depends on the training
procedure alone.

## Dataset specification

*Provisional — values marked (†) may still change before release.*

| | |
|---|---|
| **Variables** | Canopy height (m); aboveground biomass (Mg ha⁻¹) |
| **Spatial resolution** | 10 m |
| **Coordinate reference system** | EPSG:32635 — WGS 84 / UTM zone 35N |
| **Extent** | Forests of the Romanian Carpathian arc |
| **Format** | Cloud-Optimized GeoTIFF (COG) † |
| **No-data** | NaN |
| **Bands per product** | 1 — reference prediction · 2 — ensemble mean · 3 — ensemble standard deviation |
| **Reference period** | 2024–2025 † |
| **Forest definition** | Dynamic World derived forest mask |
| **Model families** | Random forest, XGBoost, CatBoost, convolutional neural network † |

The three-band structure is deliberate. Band 1 is the prediction of a single canonical
model; band 2 is the mean of ten models differing only in the random seed; band 3 is
the dispersion between them. Band 3 quantifies model-initialisation variance only — it
is not a prediction interval, and it is substantially smaller than the cross-validated
error of the same model.

## Method, in brief

1. **Reference data.** GEDI L2A and L4A footprints over the study area, filtered for
   quality and beam sensitivity, with footprint geolocation refined against a
   high-resolution digital terrain model.
2. **Predictors.** Seasonal Sentinel-2 surface reflectance composites and derived
   vegetation indices; Sentinel-1 C-band backscatter; JAXA ALOS-2 PALSAR-2 L-band
   annual mosaic (HH, HV and dual-polarisation indices); elevation, slope and aspect
   from a national 10 m digital terrain model.
3. **Feature selection.** Recursive feature elimination with cross-validation over the
   full multi-source stack.
4. **Model training.** Spatially blocked cross-validation on a 30 × 30 km block grid,
   with hyperparameters tuned by Optuna; ten seed replicates per final model.
5. **Prediction.** Block-wise application of the trained models to the full raster
   stack, restricted to the forest mask.

The full methodological description will accompany the publication.

## Data sources and attribution

Use of this dataset carries the attribution requirements of its inputs:

- **GEDI L2A / L4A** — NASA Global Ecosystem Dynamics Investigation, distributed by
  the LP DAAC and ORNL DAAC.
- **Sentinel-1 and Sentinel-2** — contains modified Copernicus Sentinel data
  (2024–2025), processed by the authors.
- **ALOS-2 PALSAR-2 yearly mosaic** — © JAXA/METI. Please cite Shimada et al. (2014),
  *Remote Sensing of Environment* 155, 13–31, as requested by the data provider.
- **Dynamic World** — Google / World Resources Institute, CC BY 4.0.
- **Digital terrain model** — national 10 m gap-filled DTM of Romania.

The predictor stack itself is **not** redistributed here. Only the derived canopy
height and biomass products are released, together with the code needed to reproduce
them from the original sources.

## Licence

- **Data products** — [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). See `LICENSE-DATA`.
- **Code in this repository** — MIT. See `LICENSE`.

## How to cite

The dataset DOI will be minted on release. Until then, please cite this repository.

```
Cățeanu, M. & Oniga, V.-E. (2027). RoCarp-CHM-AGB: canopy height and aboveground
biomass of the Romanian Carpathian forests at 10 m [Data set]. Zenodo.
https://doi.org/10.5281/zenodo.XXXXXXX
```

## Release plan

| Stage | Expected |
|---|---|
| Dataset description and specification published here | 2026 |
| Peer-reviewed publication | Q1 2027 |
| Full raster products on Zenodo, with DOI | Q1 2027, with the publication |
| Processing code released | With the publication |

Zenodo issues a version-independent *concept DOI* that always resolves to the most
recent version of the record. That DOI, once minted, is the one to bookmark or cite
when a specific version is not required.

## Authors

**Mihnea Cățeanu** <sup>1,3,\*</sup> · ORCID [0000-0002-3692-1050](https://orcid.org/0000-0002-3692-1050)
**Valeria-Ersilia Oniga** <sup>2,3,4</sup> · ORCID [0000-0001-5433-2201](https://orcid.org/0000-0001-5433-2201)

<sup>1</sup> Department of Forest Engineering, Faculty of Silviculture and Forest Engineering, Transilvania University of Brașov, Brașov, Romania
<sup>2</sup> Department of Land Surveying and Cadastre, Technical University „Gheorghe Asachi" of Iași, D. Mangeron Street, Iași, Romania
<sup>3</sup> Faculty of Geodesy, Technical University of Civil Engineering Bucharest, Bucharest, Romania
<sup>4</sup> Romanian Society of Photogrammetry and Remote Sensing, Lacul Tei Blvd. 124, 020396 Bucharest, Romania

<sup>\*</sup> Corresponding author: [cateanu.mihnea@unitbv.ro](mailto:cateanu.mihnea@unitbv.ro)

## Contact

Questions about the dataset, requests for early access for a specific application, or
proposals for collaboration: [cateanu.mihnea@unitbv.ro](mailto:cateanu.mihnea@unitbv.ro)

Watch this repository to be notified when the data are released.
