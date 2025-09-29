# Changelog
All notable changes to this project will be documented in this file.

---

## [Unreleased]
### Added
- Added an introduction in the Home page for new users.
- Added input validators to avoid wrong inputs.
- Added radio buttons for blade parameters "olp_sta" and "olp_len".
- Added export type selection, for either csv or json files.
- Added a table showing the interpolation values for the saved stations in the "Blade Parameters" tab.
- Added full implementation of the jiggle method from the section class.
- Added a guide image to understand the Section class parameters.

### Fixed
- Fixed correct implementation of blade parameters for different interpolation orders.
- Fixed "section.py" in cases where offset curves change the starting point of the coordinate array.
- Fixed "airfoil.py" in the importCoords method when the files are not ordered from TE to LE.
- Fixed the list sections to export to select multiple sections.
- Fixed an issue when clicking the "Export Stations" button did not trigger the signal.

### Changed
- Changed chart in the Airfoil Creator tab from QSS to matplotlib.
- Changed chart in Skin tab from QSS to matplotlib.
- Deactivated the Spar page until further implementation.

---

## [0.2.0] - 2024-09-25
### Added
- Included a .spec file to compile the software into an installer.

### Fixed
- Crash when importing CSV with empty header.
- Wrong ordering of coordinates when y_mirror or x_mirror where changed.
- Relative paths when started in different computers or environments.

### Changed
- Changed the name to "EdFoil".
- Updated logos and icons to the new software theme.
- Reorganised the folder structure for readibility and accessibility.

---

## [0.1.0] - 2024-09-29
### Added
- Initial development version of EdFoil GUI.
- Airfoil import, plotting, and section creation.
- CSV station import functionality.