import trimesh

# Load the STL file
stl_mesh = trimesh.load('UMS5.stl')

# Check if there are any holes in the mesh
if stl_mesh.is_watertight:
    print('No holes found.')
else:
    print('Holes found. Attempting to fix...')

    # Fill the holes using Delaunay triangulation
    stl_mesh.fill_holes()

# Visualize the defected mesh
stl_mesh.show()


    # Check if there are any remaining holes in the mesh
if stl_mesh.is_watertight:
    print('Holes fixed successfully.')
else:
    print('Could not fix all holes.')

# Save the fixed STL file
stl_mesh.export('fixed_file.stl')

# Visualize the fixed mesh
stl_mesh.show()
