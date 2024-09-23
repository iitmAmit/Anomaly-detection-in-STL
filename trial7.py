import trimesh
import numpy as np

# Load the STL file
stl_mesh = trimesh.load('UMS5.stl')

# Check if there are any holes in the mesh
if stl_mesh.is_watertight:
    print('No holes found.')
else:
    print('Holes found.')

    # Get the holes in the mesh
holes = stl_mesh.holes()

    # Print the number of holes found
print('Number of holes:', len(holes))

    # Print the ordered vertex list for each hole
for i, hole in enumerate(holes):
    print(f'Hole {i+1} edges:')
    for j, edge in enumerate(hole):
        print(f'{j+1}: {edge[0]} -> {edge[1]}')

    # Fill the holes using Delaunay triangulation
stl_mesh.fill_holes()

# Visualize the defected mesh
stl_mesh.show()

# Save the fixed STL file
stl_mesh.export('fixed_file.stl')

# Load the fixed STL file
stl_mesh_fixed = trimesh.load('fixed_file.stl')

# Visualize the fixed mesh
stl_mesh_fixed.show()

# Get the holes in the fixed mesh
holes_fixed = stl_mesh_fixed.holes()

# Print the ordered vertex list for each hole in the fixed mesh
for i, hole in enumerate(holes_fixed):
    print(f'Fixed Hole {i+1} edges:')
    for j, edge in enumerate(hole):
        print(f'{j+1}: {edge[0]} -> {edge[1]}')

    # Get the triangle list for each hole in the fixed mesh
tris = trimesh.triangulate.faces(hole)

    # Create a mesh for the hole and add it to the fixed mesh
hole_mesh = trimesh.Trimesh(vertices=hole, faces=tris)
stl_mesh_fixed += hole_mesh

# Visualize the fixed mesh with triangulated holes
stl_mesh_fixed.show()
