import trimesh
import pyglet

# load the STL file
stl_mesh = trimesh.load('UMS5.stl')

# check for holes
if stl_mesh.is_watertight:
    print("The mesh is watertight and has no holes.")
else:
    print("The mesh has holes.")

# if the mesh has holes, fix them
if not stl_mesh.is_watertight:
    stl_mesh.fill_holes()

# create a Pyglet viewer window
window = pyglet.window.Window(width=800, height=600, visible=False)

# create a Trimesh viewer scene
scene = trimesh.viewer.Scene(geometry=[stl_mesh])

# add the scene to the viewer
viewer = trimesh.viewer.SceneViewer(scene=scene, window=window)

# show the viewer window
viewer.show()
