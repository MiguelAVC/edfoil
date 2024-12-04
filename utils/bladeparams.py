from scipy.interpolate import splrep, splev

def norm_olp(coords:tuple[tuple[float,float],...],
             x_target:list[float,],
             order:int,
             ) -> list[list,list]:
    
    # Unzip coordinates of measurements
    x, y = zip(*coords)
    
    # Linear and quadratic splines
    tck = [splrep(x, y, k=i) for i in range(1,order+1)]
    
    # Extrapolate x_target values
    y_target = [splev(x_target, x).tolist() for x in tck]
    
    return y_target, tck

if __name__ == '__main__':
    
    # Define the tuple of 3 tuples with coordinates
    coords_overlap_start = (
        (1500, 0.033),
        (2400, 0.039),
        (4200, 0.047),
    )
    
    coords_overlap_length = (
        (1500, 0.065),
        (2400, 0.066),
        (4200, 0.081),
    )
    
    # List of x-values to extrapolate
    x_values_to_extrapolate = [
        1200,
        1300,
        1500,
        1600,
        1800,
        2000,
        3000,
        4000,
        5000,
        6000,
        6250,
    ]
    
    olp_sta = norm_olp(
        coords = coords_overlap_start, 
        x_target = x_values_to_extrapolate,
        order = 2,
    )
    print('Overlap start:')
    print('- Linear')
    print(olp_sta[0][0])
    print('- Quadratic')
    print(olp_sta[0][1])
    
    olp_len = norm_olp(
        coords = coords_overlap_length,
        x_target = x_values_to_extrapolate,
        order = 2,
    )
    print('Overlap length:')
    print('- Linear')
    print(olp_len[0][0])
    print('- Quadratic')
    print(olp_len[0][1])
    
# # Separate the tuple of tuples into two lists: x and y coordinates
# x, y = zip(*coordinates)

# # Generate a spline from the coordinates
# # 'k=1' ensures a linear spline is used, which can extrapolate reasonably well
# tck_lin = splrep(x, y, k=1)
# tck_qua = splrep(x, y, k=2)

# # Extrapolate y-values for the provided x-values
# extrapolated_y_values_lin = splev(x_values_to_extrapolate, tck_lin)
# extrapolated_y_values_qua = splev(x_values_to_extrapolate, tck_qua)

# # Output the extrapolated y-values
# print(f"Linear y-values for x-values: {extrapolated_y_values_lin}")
# print(f"Quadratic y-values for x-values: {extrapolated_y_values_qua}")

# # Plot the original points, the spline, and the extrapolated points
# x_new = np.linspace(min(x_values_to_extrapolate), max(x_values_to_extrapolate), 100)
# y_new_lin = splev(x_new, tck_lin)
# y_new_qua = splev(x_new, tck_qua)

# # Plot
# saveFig = True
# fig, ax = plt.subplots(figsize=[6,5])

# ax.plot(x_new, y_new_lin, '-', label=None)
# ax.plot(x_new, y_new_qua, '-', label=None)
# ax.plot(x_values_to_extrapolate, extrapolated_y_values_lin, 'x', label='Interpolated values (lin)')
# ax.plot(x_values_to_extrapolate, extrapolated_y_values_qua, 'x', label='Interpolated values (quad)')
# ax.plot(x, y, 'bo', label='Measured points')

# ax.set_xlabel('Station [$mm$]')
# ax.set_ylabel('Normalised overlap distance [-]')
# ax.legend(loc='best')
# ax.minorticks_on()
# ax.tick_params(axis="both", which="both", direction="in",
#                 top=True, right=True, labelsize='large')

# plt.tight_layout()