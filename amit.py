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

    # Output the hole information
hole_count = len(stl_mesh.holes)
print('Number of holes: {}'.format(hole_count))
for i, hole in enumerate(stl_mesh.holes):
    print('Hole {}:'.format(i+1))
    print('  Edge loop: {}'.format(hole.tolist()))
    print('  Triangulation: {}'.format(stl_mesh.holes_closed[i]))

# Save the fixed STL file
# stl_mesh.export('output.stl')

# Visualize the defected and fixed mesh
# trimesh.Scene([stl_mesh, trimesh.load('output.stl')]).show()
