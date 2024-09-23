import trimesh
import pyrender

# Load defected STL file
defected_mesh = trimesh.load('UMS5.stl')

# Detect and fix holes
if defected_mesh.is_watertight:
    print("No holes detected in the defected mesh.")
else:
    defected_mesh.fill_holes()

# Load fixed STL file
fixed_mesh = trimesh.load('fixed.stl')

# Create PyRender scene
scene = pyrender.Scene()

# Add defected mesh to the scene in red color
defected_node = pyrender.Mesh.from_trimesh(defected_mesh, smooth=False)
defected_node.primitive.color = (1.0, 0.0, 0.0)
scene.add(defected_node)

# Add fixed mesh to the scene in green color
fixed_node = pyrender.Mesh.from_trimesh(fixed_mesh, smooth=False)
fixed_node.primitive.color = (0.0, 1.0, 0.0)
scene.add(fixed_node)

# Create camera and set its position
camera = pyrender.PerspectiveCamera(yfov=60.0, aspectRatio=1.0)
camera_pose = [2.0, 2.0, 2.0]
scene.add(camera, pose=camera_pose)

# Create light and set its position
light = pyrender.PointLight(color=[1.0, 1.0, 1.0], intensity=2.0)
light_pose = [1.0, 1.0, 1.0]
scene.add(light, pose=light_pose)

# Create viewer and show the scene
viewer = pyrender.Viewer(scene, use_raymond_lighting=True)
