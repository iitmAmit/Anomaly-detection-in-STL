import trimesh

# Load the STL file
stl_mesh = trimesh.load('UMS5.stl')

# Check if there are any holes in the mesh
if stl_mesh.is_watertight:
    print('No holes found.')
else:
    print('Holes found. Attempting to fix...')
    
# Get the list of holes
holes = stl_mesh.geometry.holes
    
    # Print the number of holes
print(f'{len(holes)} holes found:')
    
for i, hole in enumerate(holes):
# Print the edge loop for the current hole
    print(f'Edge loop {i + 1}: {hole}')
        
        # Triangulate the current hole
    hole_tris = trimesh.triangulate.triangulate(hole.reshape((-1, 2)))
        
        # Add the triangulated hole to the mesh
    stl_mesh = stl_mesh + trimesh.Trimesh(vertices=hole, faces=hole_tris)

# Visualize the defected mesh
stl_mesh.show()

# Save the fixed STL file
stl_mesh.export('fixed_file.stl')

# Load the fixed STL file
stl_mesh2 = trimesh.load('fixed_file.stl')

# Visualize the fixed mesh
stl_mesh2.show()
