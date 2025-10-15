# Changelog
All notable changes to this project will be documented in this file.

---
## [0.3.1] - 2025-10-10
### Added
- Warning light now visible.
- Extra parameters for Section instance creation in the "Settings" window.
- Toggle to open the destination folder after exporting section.
- Save and load session capabilities.

### Fixed
- Mouse coordinates in Station plot would not show.
- Icon path changed to resource_path method.
- update coordinates in airfoil instance would leave upper and lower attributes empty.

### Changed
- DPI font commented out because it may cause small fonts in high resolutions.
- Eliminated two themes.
- File extension changed to "*.edf".

## [0.3.0] - 2025-10-07
### Added
- Settings dialog to change themes.
- Graph showing the top view of the blade in the "Blade" tab.
- Four different themes and a loader method.
- Icons for future use in the "icons" folder.
- Completely redesigned the UI.
- More safeguards displayed in the message bar.

### Fixed
- QSS priorities changed to increase style consistency.
- Stations table was only creating one new row even if the input was greater.
- Interpolation dictionaries were created based on the number of stations rather than the number of interpolations.
- Path in "themeLoader" module being undefined.

### Changed
- Charts code transitioned from python to qml. Improvement in performance.
- Introduced bridge connections to interact with qml files.
- Eliminated the windows style "Fusion".
- All tables now fill the width with the contents.

## [0.2.3] - 2025-10-02
### Added
- Added an introduction in the Home page for new users.
- Added input validators to avoid wrong inputs.
- Added radio buttons for blade parameters "olp_sta" and "olp_len".
- Added export type selection, for either csv or json files.
- Added a table showing the interpolation values for the saved stations in the "Blade Parameters" tab.
- Added full implementation of the jiggle method from the section class.
- Added a guide image to understand the Section class parameters.
- Examples (A and B) and a user guide.
- Stations can be deleted and modified in the "Interactive" tab.

### Fixed
- Fixed correct implementation of blade parameters for different interpolation orders.
- Fixed "section.py" in cases where offset curves change the starting point of the coordinate array.
- Fixed "airfoil.py" in the importCoords method when the files are not ordered from TE to LE.
- Fixed the list sections to export to select multiple sections.
- Fixed an issue when clicking the "Export Stations" button did not trigger the signal.
- Wrong signal when the toggle for the skin overlap length was sent.
- Stations table in the "Advanced" tab was not updating when a stations was modified or deleted.

### Changed
- Changed chart in the Airfoil Creator tab from QSS to matplotlib.
- Changed chart in Skin tab from QSS to matplotlib.
- Deactivated the Spar page until further implementation.
- Simplified the hide methods in the skin tab.

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