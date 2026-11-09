#!/usr/bin/env python3
"""
Append Batch 10 (Q121 - Q150) data to data/geology_2019.json
"""

import json
import os

BASE_DIR = "/home/tapaswi/Mines_Geology/Orrisa_geology"
DATA_PATH = os.path.join(BASE_DIR, "data", "geology_2019.json")

batch10_items = [
  {
    "q": 121,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Marine Optics & Oceanography",
    "topic": "Refractive Index of Ocean Seawater as Function of Salinity & Temperature",
    "question": "The refractive index of the ocean water:",
    "options": {
      "A": "Increases with salinity",
      "B": "Increases with temperature",
      "C": "Decreases with salinity",
      "D": "Decreases with temperature"
    },
    "correct_option": "A",
    "correct_text": "Increases with salinity (Lorentz-Lorenz equation & Millard-Seaver 1990 seawater formulation: dn/dS ≈ +0.00019 / PSU)",
    "textbook_ref": "R.C. Millard & G. Seaver (1990); R.W. Austin & G. Halikas (1976); K.M. Bangar (p. 208)",
    "file_html": "solutions/geology_2019/Q121_Refractive_Index_Ocean_Water_Increases_With_Salinity_Complete_Guide.html",
    "icon": "🌊"
  },
  {
    "q": 122,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Satellite Remote Sensing & Geometric Correction",
    "topic": "Systematic vs. Random Geometric Distortions in Satellite Sensors",
    "question": "Which one of the following geometric errors of satellite sensors is random ?",
    "options": {
      "A": "Scan skew",
      "B": "Panoramic distortion",
      "C": "Earth rotation",
      "D": "Altitude variation"
    },
    "correct_option": "D",
    "correct_text": "Altitude variation (Orbital height perturbations & attitude jitter are non-systematic/random errors requiring GCP polynomial correction)",
    "textbook_ref": "T.M. Lillesand, R.W. Kiefer, & J.W. Chipman (Remote Sensing and Image Interpretation, 7th Ed., Ch. 7); K.M. Bangar (p. 210)",
    "file_html": "solutions/geology_2019/Q122_Geometric_Errors_Satellite_Sensors_Random_Altitude_Variation_Complete_Guide.html",
    "icon": "🛰️"
  },
  {
    "q": 123,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Remote Sensing Instrumentation & Sensor Physics",
    "topic": "Active vs. Passive Remote Sensing Sensor Systems",
    "question": "The instruments which provide electromagnetic radiation of specified wave length or a band of wave lengths to illuminate the earth surface, are called :",
    "options": {
      "A": "Microwave sensors",
      "B": "Passive sensors",
      "C": "Active sensors",
      "D": "Optical sensors"
    },
    "correct_option": "C",
    "correct_text": "Active sensors (Self-illuminating systems like Radar, LiDAR, and scatterometers that emit their own EMR pulse)",
    "textbook_ref": "T.M. Lillesand et al. (Ch. 1 & 8); Floyd F. Sabins (Ch. 1); K.M. Bangar (p. 209)",
    "file_html": "solutions/geology_2019/Q123_Instruments_Providing_EMR_To_Illuminate_Earth_Active_Sensors_Complete_Guide.html",
    "icon": "📡"
  },
  {
    "q": 124,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Wave Optics & Radar Remote Sensing",
    "topic": "Coherence Length and Spectral Bandwidth Relationship",
    "question": "The coherence length over which there is a strong relationship between amplitudes is:",
    "options": {
      "A": "Directly proportional to the bandwidth",
      "B": "Inversely proportional to the bandwidth",
      "C": "The square of the bandwidth",
      "D": "The inverse of square of bandwidth"
    },
    "correct_option": "B",
    "correct_text": "Inversely proportional to the bandwidth (Lc = c / Δν = λ₀² / Δλ; Fourier transform uncertainty relation)",
    "textbook_ref": "Eugene Hecht (Optics, 5th Ed., Ch. 7 & 12); Max Born & Emil Wolf (Principles of Optics); T.M. Lillesand et al. (Ch. 8)",
    "file_html": "solutions/geology_2019/Q124_Coherence_Length_Inversely_Proportional_Bandwidth_Complete_Guide.html",
    "icon": "〰️"
  },
  {
    "q": 125,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Atmospheric Physics & Radiation Transfer",
    "topic": "Atmospheric Windows and Atmospheric Transmission in Remote Sensing",
    "question": "The spectral region of the electromagnetic radiation which passes through the atmosphere without much attenuation in known as:",
    "options": {
      "A": "Ozone hole",
      "B": "Atmospheric window",
      "C": "Ozone window",
      "D": "Black hole"
    },
    "correct_option": "B",
    "correct_text": "Atmospheric window (Wavelength bands where atmospheric gas absorption is minimal, allowing EMR to transmit to Earth's surface)",
    "textbook_ref": "T.M. Lillesand et al. (Ch. 1); Floyd F. Sabins (Ch. 2); K.M. Bangar (p. 208)",
    "file_html": "solutions/geology_2019/Q125_Spectral_Region_Passes_Through_Atmosphere_Atmospheric_Window_Complete_Guide.html",
    "icon": "🪟"
  },
  {
    "q": 126,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Radiation Physics & Quantum Mechanics",
    "topic": "Planck's Quantum Law and Energy-Frequency Relationship",
    "question": "The value of energy quantum for radiation of any frequency is proportional to :",
    "options": {
      "A": "The frequency",
      "B": "The reciprocal of the energy",
      "C": "The square of the frequency",
      "D": "The square root of the frequency"
    },
    "correct_option": "A",
    "correct_text": "The frequency (Planck's law: E = h·ν; photon energy quantum is directly proportional to radiation frequency)",
    "textbook_ref": "Max Planck (1900); Arthur Beiser (Concepts of Modern Physics); T.M. Lillesand et al. (Ch. 1); K.M. Bangar (p. 208)",
    "file_html": "solutions/geology_2019/Q126_Energy_Quantum_Radiation_Proportional_To_Frequency_Complete_Guide.html",
    "icon": "⚛️"
  },
  {
    "q": 127,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Aerial Photogrammetry & Relief Displacement",
    "topic": "Relief Displacement Calculation for Vertical Objects",
    "question": "A and B are two towers of equal height diametrically opposite on either side of the nadir point at 3 km and 5 km distances. Then, which one of the following statements is correct ?",
    "options": {
      "A": "Height displacement of A will be less than that of B",
      "B": "Height displacement of B will be less than that of A",
      "C": "Height displacement of A and B is equal",
      "D": "Height displacement of A and B will be towards each other"
    },
    "correct_option": "A",
    "correct_text": "Height displacement of A will be less than that of B (Relief displacement formula d = r·h/H; since r_A = 3 km < r_B = 5 km, d_A < d_B)",
    "textbook_ref": "P.R. Wolf & B.A. Dewitt (Elements of Photogrammetry, 4th Ed.); T.M. Lillesand et al. (Ch. 3); K.M. Bangar (p. 211)",
    "file_html": "solutions/geology_2019/Q127_Aerial_Photogrammetry_Relief_Height_Displacement_Towers_Complete_Guide.html",
    "icon": "🗼"
  },
  {
    "q": 128,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Satellite Geodesy & GPS Technology",
    "topic": "Antenna Architecture for Global Positioning System (GPS)",
    "question": "The most widely used antenna in GPS is:",
    "options": {
      "A": "Parabolic antenna",
      "B": "Microstrip antenna",
      "C": "Horn antenna",
      "D": "Slotted antenna"
    },
    "correct_option": "B",
    "correct_text": "Microstrip antenna (Compact ceramic patch antenna; provides low profile, RHCP polarization, and hemispherical coverage)",
    "textbook_ref": "B. Hofmann-Wellenhof et al. (GNSS: GPS, GLONASS, Galileo); C.A. Balanis (Antenna Theory); K.M. Bangar (p. 212)",
    "file_html": "solutions/geology_2019/Q128_Most_Widely_Used_Antenna_In_GPS_Microstrip_Antenna_Complete_Guide.html",
    "icon": "🛰️"
  },
  {
    "q": 129,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Electromagnetic Wave Propagation & Optics",
    "topic": "Fresnel Reflection and Transmission at Dielectric Interfaces",
    "question": "“An Electromagnetic wave falls on to a boundary between two less homogeneous media with different refractive indices and a part of the wave is reflected back to the incident medium and the rest is transmitted on to the second media.” This phenomenon is known as :",
    "options": {
      "A": "Fresnel reflection",
      "B": "Fresnel refraction",
      "C": "Snell’s law",
      "D": "Spectral reflectance"
    },
    "correct_option": "A",
    "correct_text": "Fresnel reflection (Verbatim textbook definition of reflection and transmission wave splitting at dielectric boundaries governed by Fresnel equations)",
    "textbook_ref": "Eugene Hecht (Optics, 5th Ed., Ch. 4); Max Born & Emil Wolf (Principles of Optics); T.M. Lillesand et al. (Ch. 1)",
    "file_html": "solutions/geology_2019/Q129_Electromagnetic_Wave_Boundary_Reflection_Fresnel_Reflection_Complete_Guide.html",
    "icon": "🪞"
  },
  {
    "q": 130,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Satellite Geodesy & Orbital Mechanics",
    "topic": "GPS Satellite Constellation Orbital Altitude and Medium Earth Orbit (MEO)",
    "question": "The normal altitude of GPS satellite is about:",
    "options": {
      "A": "16,200 km",
      "B": "20,200 km",
      "C": "24,400 km",
      "D": "36,100 km"
    },
    "correct_option": "B",
    "correct_text": "20,200 km (Nominal GPS MEO altitude is 20,182 km ≈ 20,200 km, semi-major axis a = 26,560 km, orbital period 11 hr 58 min)",
    "textbook_ref": "B. Hofmann-Wellenhof et al. (Ch. 2); G. Xu (GPS: Theory, Algorithms and Applications); K.M. Bangar (p. 212)",
    "file_html": "solutions/geology_2019/Q130_Normal_Altitude_Of_GPS_Satellite_20200_km_Complete_Guide.html",
    "icon": "🛰️"
  },
  {
    "q": 131,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Satellite Orbits & Earth Observation Systems",
    "topic": "Sun-Synchronous Orbit Architecture for Temporal Earth Monitoring",
    "question": "For interpolation of satellite data used for monitoring dynamic changes that occur on the earth surface, the most suitable orbit for the satellite is :",
    "options": {
      "A": "Circular orbit",
      "B": "Sun-synchronous orbit",
      "C": "Near polar orbit",
      "D": "None of these"
    },
    "correct_option": "B",
    "correct_text": "Sun-synchronous orbit (Nodal precession matches solar revolution, ensuring identical local solar time and constant illumination for change detection)",
    "textbook_ref": "T.M. Lillesand et al. (Ch. 6); Floyd F. Sabins (Ch. 2); K.M. Bangar (p. 210)",
    "file_html": "solutions/geology_2019/Q131_Monitoring_Dynamic_Changes_Sun_Synchronous_Orbit_Complete_Guide.html",
    "icon": "☀️"
  },
  {
    "q": 132,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Planetary Radiation Physics & Climatology",
    "topic": "Planetary Albedo and Global Radiation Balance",
    "question": "The ratio of the total solar radiant energy returned by a planetary body to the total radiant energy incident on the body is called :",
    "options": {
      "A": "Reflectance",
      "B": "Reflectance factor",
      "C": "Albedo",
      "D": "None of these"
    },
    "correct_option": "C",
    "correct_text": "Albedo (Specifically Bond Albedo: the fraction of total incident solar radiant energy scattered back into space across all wavelengths; Earth A ≈ 0.30)",
    "textbook_ref": "D.L. Hartmann (Global Physical Climatology); J.R. Holton (Dynamic Meteorology); K.M. Bangar (p. 209)",
    "file_html": "solutions/geology_2019/Q132_Ratio_Total_Solar_Radiant_Energy_Returned_Is_Albedo_Complete_Guide.html",
    "icon": "🌍"
  },
  {
    "q": 133,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Solar Radiation Physics & Blackbody Laws",
    "topic": "Wien's Displacement Law and the Peak Solar Emission Spectrum",
    "question": "The maximum sun’s radiation occurs around :",
    "options": {
      "A": "0.4 um wave length",
      "B": "0.55 wave length",
      "C": "0.7 um wavelength",
      "D": "None of these"
    },
    "correct_option": "B",
    "correct_text": "0.55 wave length (0.55 µm, visible green-yellow band; derived from Wien's law λ_max = 2898/T for solar surface T ≈ 5800 K)",
    "textbook_ref": "T.M. Lillesand et al. (Ch. 1); K.M. Bangar (p. 208); Floyd F. Sabins (Ch. 2)",
    "file_html": "solutions/geology_2019/Q133_Maximum_Sun_Radiation_Occurs_Around_0_55_um_Complete_Guide.html",
    "icon": "☀️"
  },
  {
    "q": 134,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Indian Remote Sensing (IRS) Systems",
    "topic": "Resourcesat-1 (IRS-P6) Sensor System Resolutions (LISS-IV, LISS-III, AWiFS)",
    "question": "The resolution (m) of LISS-IV Resourcesat—1 is:",
    "options": {
      "A": "5.8 m",
      "B": "23.5 m",
      "C": "56 m",
      "D": "70.5 m"
    },
    "correct_option": "A",
    "correct_text": "5.8 m (LISS-IV has 5.8 m spatial resolution; LISS-III is 23.5 m, AWiFS is 56 m)",
    "textbook_ref": "ISRO Resourcesat-1 Mission Specifications; T.M. Lillesand et al. (Ch. 6); K.M. Bangar (p. 210)",
    "file_html": "solutions/geology_2019/Q134_Resolution_Of_LISS_IV_Resourcesat_1_Is_5_8_m_Complete_Guide.html",
    "icon": "🇮🇳"
  },
  {
    "q": 135,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Digital Image Processing (DIP)",
    "topic": "Digital Image Processing: Rectification, Radiometric Enhancement & Classification",
    "question": "The art and science of manipulation of digital data including enhancement, classification and rectification is known as :",
    "options": {
      "A": "Orthorectification",
      "B": "Image processing",
      "C": "Rectification",
      "D": "Geometric correction"
    },
    "correct_option": "B",
    "correct_text": "Image processing (Digital Image Processing, DIP: the overarching science of processing digital image matrices)",
    "textbook_ref": "J.R. Jensen (Introductory Digital Image Processing, 4th Ed.); T.M. Lillesand et al. (Ch. 7); K.M. Bangar (p. 211)",
    "file_html": "solutions/geology_2019/Q135_Digital_Data_Manipulation_Enhancement_Image_Processing_Complete_Guide.html",
    "icon": "🖥️"
  },
  {
    "q": 136,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "GIS Data Models & Spatial Representation",
    "topic": "Continuous Field-Based Spatial Model (Goodchild's Field vs. Object View)",
    "question": "A geographic field is a phenomenon where for every point in the study area:",
    "options": {
      "A": "A value can be determined",
      "B": "A value can not be determined",
      "C": "A value is not relevant",
      "D": "A value is missing"
    },
    "correct_option": "A",
    "correct_text": "A value can be determined (A continuous field z = f(x, y) defines a measurable attribute value at every single coordinate point in space)",
    "textbook_ref": "P.A. Burrough & R.A. McDonnell (Principles of GIS, Ch. 2); Kang-tsung Chang (Ch. 1); M.F. Goodchild (1992); K.M. Bangar (p. 216)",
    "file_html": "solutions/geology_2019/Q136_Geographic_Field_Phenomenon_Value_Can_Be_Determined_Complete_Guide.html",
    "icon": "🌐"
  },
  {
    "q": 137,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Spatial Statistics & Geostatistics",
    "topic": "Spatial Autocorrelation, Tobler's First Law of Geography & Semivariograms",
    "question": "Interpolation is made possible by a principle called :",
    "options": {
      "A": "Spatial Autocorrelation",
      "B": "Spatial auto-correction",
      "C": "Thematic Autocorrelation",
      "D": "Thematic auto-correction"
    },
    "correct_option": "A",
    "correct_text": "Spatial Autocorrelation (Tobler's First Law: near things are more related than distant things, making distance-based interpolation valid)",
    "textbook_ref": "Waldo Tobler (1970); Kang-tsung Chang (Ch. 15); P.A. Burrough & R.A. McDonnell (Ch. 6); K.M. Bangar (p. 217)",
    "file_html": "solutions/geology_2019/Q137_Interpolation_Made_Possible_By_Spatial_Autocorrelation_Complete_Guide.html",
    "icon": "📊"
  },
  {
    "q": 138,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Geoinformatics & Spatial Infrastructure",
    "topic": "Spatial Data Infrastructure (SDI) Components: Policies, Technologies, Standards & People",
    "question": "In Gis application, SDI stands for:",
    "options": {
      "A": "Spatial Data Interface",
      "B": "Spatial Data Infrastructure",
      "C": "Spatial Data Intention",
      "D": "Spatial Data international"
    },
    "correct_option": "B",
    "correct_text": "Spatial Data Infrastructure (The coordinated framework of geographic data, metadata, standards, clearinghouse networks, and policies)",
    "textbook_ref": "Ian Masser (Building European Spatial Data Infrastructures); G. Rajabifard et al.; Kang-tsung Chang (Ch. 1); K.M. Bangar (p. 217)",
    "file_html": "solutions/geology_2019/Q138_In_GIS_Application_SDI_Stands_For_Spatial_Data_Infrastructure_Complete_Guide.html",
    "icon": "🏛️"
  },
  {
    "q": 139,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Spatial Analysis & Surface Modeling",
    "topic": "Spatial Interpolation Methodologies: Deterministic (IDW, Spline) vs. Geostatistical (Kriging)",
    "question": "The process of using data points with known values to estimate values at unknown points in any given area is called :",
    "options": {
      "A": "Spatial Prediction",
      "B": "Spatial interpolation",
      "C": "Spatial Adjustment",
      "D": "Spatial Reflection"
    },
    "correct_option": "B",
    "correct_text": "Spatial interpolation (The mathematical procedure of estimating unknown values from sample control points across a spatial domain)",
    "textbook_ref": "Kang-tsung Chang (Ch. 15); P.A. Burrough & R.A. McDonnell (Ch. 6); E.H. Isaaks & R.M. Srivastava; K.M. Bangar (p. 217)",
    "file_html": "solutions/geology_2019/Q139_Process_Using_Known_Data_Points_Spatial_Interpolation_Complete_Guide.html",
    "icon": "📈"
  },
  {
    "q": 140,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Cartography & Scale Generalization",
    "topic": "Cartographic Generalization and Geometric Primitives (Point, Line, Polygon) as a Function of Map Scale",
    "question": "How a large city generally appears on a 1: 25,000 scale map:?",
    "options": {
      "A": "As a single point",
      "B": "As a cluster of points, lines and polygons",
      "C": "As a polygon",
      "D": "As a cluster of points"
    },
    "correct_option": "C",
    "correct_text": "As a polygon (At large scales like 1:25,000, cities are mapped as extensive areal polygons showing urban layout; at small scales they collapse to points)",
    "textbook_ref": "A.H. Robinson et al. (Elements of Cartography); Kang-tsung Chang (Ch. 1 & 3); K.M. Bangar (p. 216)",
    "file_html": "solutions/geology_2019/Q140_Large_City_Appears_On_1_25000_Scale_Map_As_A_Polygon_Complete_Guide.html",
    "icon": "🏙️"
  },
  {
    "q": 141,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Cartographic Mathematics & Scale",
    "topic": "Representative Fraction (RF) 1:50,000 Metric Distance Calculation (1 mm = 50 m)",
    "question": "What does 1 mm on a map drawn at a scale of 1: 50,000 represent on the ground ?",
    "options": {
      "A": "50 centimetres",
      "B": "5 metres",
      "C": "50 metres",
      "D": "500 centimetres"
    },
    "correct_option": "C",
    "correct_text": "50 metres (1 mm × 50,000 = 50,000 mm = 5,000 cm = 50 metres)",
    "textbook_ref": "Kang-tsung Chang (Ch. 1); Survey of India Topographical Guidelines; K.M. Bangar (p. 216)",
    "file_html": "solutions/geology_2019/Q141_Map_Scale_1_50000_1_mm_Represents_50_Metres_Complete_Guide.html",
    "icon": "📏"
  },
  {
    "q": 142,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "GIS Database Architecture",
    "topic": "Database Management Systems (DBMS) in Geographic Information Systems (RDBMS, Spatial SQL, Geodatabase)",
    "question": "What does the abbreviation DBMS stand for ?",
    "options": {
      "A": "Digital Base Mapping System",
      "B": "Data Borrowing and Movement Software",
      "C": "Database Management System",
      "D": "Database Manipulation Software"
    },
    "correct_option": "C",
    "correct_text": "Database Management System (Software package for defining, managing, querying, and updating structured tabular and spatial databases)",
    "textbook_ref": "A. Silberschatz et al. (Database System Concepts); Kang-tsung Chang (Ch. 3); K.M. Bangar (p. 217)",
    "file_html": "solutions/geology_2019/Q142_Abbreviation_DBMS_Stands_For_Database_Management_System_Complete_Guide.html",
    "icon": "🗄️"
  },
  {
    "q": 143,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "GIS Spatial Analysis & Proximity Operations",
    "topic": "Proximity Analysis and Vector Buffering of Points, Lines, and Polygons",
    "question": "For which of the following applications, the buffer operation can be used in GIS ?",
    "options": {
      "A": "Calculating the distance from one point to another",
      "B": "Calculating the area of overlap between two polygon data layers",
      "C": "Determining the area within a set distance from a point, line or area feature",
      "D": "Calculating the number of observations within a set distance of a point line or area feature"
    },
    "correct_option": "C",
    "correct_text": "Determining the area within a set distance from a point, line or area feature (Buffer generates a polygon zone enclosing all territory within distance r)",
    "textbook_ref": "Kang-tsung Chang (Ch. 11); P.A. Burrough & R.A. McDonnell (Ch. 5); K.M. Bangar (p. 219)",
    "file_html": "solutions/geology_2019/Q143_Buffer_Operation_Used_In_GIS_Area_Within_Set_Distance_Complete_Guide.html",
    "icon": "⭕"
  },
  {
    "q": 144,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "GIS Historical Foundations & Definitions",
    "topic": "Peter Burrough's Classic 1986 Definition of GIS and Five Core Functional Subsystems",
    "question": "A GIS is \"a set of tools for collecting, storing, retrieving, transforming and displaying spatial data from the real world for a particular use\" as defined by:",
    "options": {
      "A": "David Rhind (1991)",
      "B": "Peter Burrough (1986)",
      "C": "Mike Goodchild (1997)",
      "D": "Roger Chorley (1987)"
    },
    "correct_option": "B",
    "correct_text": "Peter Burrough (1986) (Principles of Geographical Information Systems for Land Resources Assessment, Oxford Univ. Press, p. 6)",
    "textbook_ref": "P.A. Burrough (1986); P.A. Burrough & R.A. McDonnell (1998); Kang-tsung Chang (Ch. 1); K.M. Bangar (p. 216)",
    "file_html": "solutions/geology_2019/Q144_GIS_Definition_Set_Of_Tools_Peter_Burrough_1986_Complete_Guide.html",
    "icon": "📖"
  },
  {
    "q": 145,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "GIS Spatial Analysis & Raster Operations",
    "topic": "Raster Reclassification, Value Slicing & Attribute Recoding in GIS",
    "question": "What is reclassification ?",
    "options": {
      "A": "The process of combining one or more data ranges into a new data range to create a new data layer",
      "B": "An analytical technique based on point data",
      "C": "The process of simplifying data in a data layer",
      "D": "The process of combining two or more data layers"
    },
    "correct_option": "A",
    "correct_text": "The process of combining one or more data ranges into a new data range to create a new data layer (Local raster operation remapping input values/ranges)",
    "textbook_ref": "Kang-tsung Chang (Ch. 12); P.A. Burrough & R.A. McDonnell (Ch. 5); C. Dana Tomlin; K.M. Bangar (p. 219)",
    "file_html": "solutions/geology_2019/Q145_What_Is_Reclassification_Combining_Data_Ranges_Complete_Guide.html",
    "icon": "🔄"
  },
  {
    "q": 146,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Vector Spatial Analysis & Topological Overlays",
    "topic": "Point-in-Polygon Topological Overlay Mechanics & Ray-Casting Algorithm",
    "question": "What is ‘point-in-polygon’ overlay ?",
    "options": {
      "A": "A method interpolating point data",
      "B": "An overlay method used to determine the distance between a point and its nearest neighbouring polygon",
      "C": "An overlay method used to reclassify polygon data",
      "D": "An overlay method used to determine as to which points lie within the boundary of a polygon"
    },
    "correct_option": "D",
    "correct_text": "An overlay method used to determine as to which points lie within the boundary of a polygon (Topological containment testing via ray-casting)",
    "textbook_ref": "Kang-tsung Chang (Ch. 11); P.A. Burrough & R.A. McDonnell (Ch. 5); K.M. Bangar (p. 219)",
    "file_html": "solutions/geology_2019/Q146_Point_In_Polygon_Overlay_Points_Within_Boundary_Complete_Guide.html",
    "icon": "📍"
  },
  {
    "q": 147,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "GIS Data Structures & Spatial Modeling",
    "topic": "Raster Data Model: Grid Cell Resolution, Matrix Row-Column Coordinate System & Pixel Values",
    "question": "A matrix of cells organized into rows and columns containing a value representing some information is called:",
    "options": {
      "A": "Crystal",
      "B": "Raster",
      "C": "Segment",
      "D": "Polygon"
    },
    "correct_option": "B",
    "correct_text": "Raster (A regular orthogonal cellular grid matrix of rows and columns where every cell stores a numeric or categorical attribute value)",
    "textbook_ref": "Kang-tsung Chang (Ch. 4); P.A. Burrough & R.A. McDonnell (Ch. 2); K.M. Bangar (p. 216)",
    "file_html": "solutions/geology_2019/Q147_Matrix_Of_Cells_Organized_Into_Rows_And_Columns_Raster_Complete_Guide.html",
    "icon": "▦"
  },
  {
    "q": 148,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Cartography & Map Projections",
    "topic": "Developable Surface Projections (Cylindrical, Conic, Azimuthal) vs. Geographic Coordinates (GCS)",
    "question": "Which of the following is not a type of map projection ?",
    "options": {
      "A": "Cylindrical",
      "B": "Conic",
      "C": "Azimuthal",
      "D": "Geographic"
    },
    "correct_option": "D",
    "correct_text": "Geographic (Geographic is a 3D spherical/ellipsoidal angular coordinate system in degrees, NOT a 2D map projection onto a developable surface)",
    "textbook_ref": "J.P. Snyder (Map Projections: A Working Manual, USGS Paper 1395); Kang-tsung Chang (Ch. 2); K.M. Bangar (p. 216)",
    "file_html": "solutions/geology_2019/Q148_Not_A_Type_Of_Map_Projection_Geographic_Complete_Guide.html",
    "icon": "🗺️"
  },
  {
    "q": 149,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "GIS Spatial Modeling & Map Algebra",
    "topic": "C. Dana Tomlin's Cartographic Modeling and Map Algebra (Local, Focal, Zonal, Global Operations)",
    "question": "Cartographic modeling is :",
    "options": {
      "A": "The sequence of modeling of real world entities in a GIS database",
      "B": "A way of expressing and organizing methods by which spatial operations are selected and used to develop a GIS model",
      "C": "A generic method of creating a GIS map data structure",
      "D": "The modeling of map inputs to a GIS, using programming language"
    },
    "correct_option": "B",
    "correct_text": "A way of expressing and organizing methods by which spatial operations are selected and used to develop a GIS model (C. Dana Tomlin's 1990 classic Map Algebra methodology)",
    "textbook_ref": "C. Dana Tomlin (GIS and Cartographic Modeling, Prentice Hall, 1990); Kang-tsung Chang (Ch. 12); K.M. Bangar (p. 219)",
    "file_html": "solutions/geology_2019/Q149_Cartographic_Modeling_Expressing_Organizing_Methods_Complete_Guide.html",
    "icon": "🔀"
  },
  {
    "q": 150,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "GIS Data Acquisition & Workflow Processing",
    "topic": "The GIS Data Stream: Complete Pipeline from Raw Acquisition to Integrated Spatial Database",
    "question": "Data stream means :",
    "options": {
      "A": "The process by which raw spatial data is processed into an integrated GIS database",
      "B": "The flow of data from one user to another",
      "C": "The process by which maps are transferred between GIS platforms",
      "D": "The flow of data from user to GIS platform"
    },
    "correct_option": "A",
    "correct_text": "The process by which raw spatial data is processed into an integrated GIS database (The end-to-end data pipeline: acquisition, georeferencing, cleaning, and geodatabase integration)",
    "textbook_ref": "Jeffrey Star & John Estes (Geographic Information Systems: An Introduction); P.A. Burrough & R.A. McDonnell (Ch. 1); K.M. Bangar (p. 216)",
    "file_html": "solutions/geology_2019/Q150_Data_Stream_Raw_Spatial_Data_Processed_Integrated_GIS_Complete_Guide.html",
    "icon": "💾"
  }
]

# Read existing data
with open(DATA_PATH, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

existing_dict = {item["q"]: item for item in existing_data}

# Add or update batch 10 items
for item in batch10_items:
    existing_dict[item["q"]] = item

sorted_data = [existing_dict[k] for k in sorted(existing_dict.keys())]

# Write back
with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(sorted_data, f, indent=2, ensure_ascii=False)

print(f"Updated {DATA_PATH} successfully! Total questions: {len(sorted_data)}")
missing = [n for n in range(1, 151) if n not in existing_dict]
print("Missing question numbers:", missing or "None! Complete 1 to 150!")
