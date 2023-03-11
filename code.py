import random
import bpy

# Set the number of rows and columns in the grid.
num_rows = 3
num_columns = 3

# Set the size of each cell in the grid.
cell_size = 2.0

# Define a function to create a box with a random-sized child object.
def create_box_with_child():
    # Create a new box object.
    box = bpy.ops.mesh.primitive_cube_add()

    # Set the position of the box object.
    box_location = (0.0, 0.0, 0.0)
    bpy.context.scene.cursor.location = box_location
    box_scale = (1.0, 1.0, 1.0)
    bpy.ops.object.transform_apply(scale=True)
    box_location = (cell_size / 2, cell_size / 2, 0.0) + box_location
    bpy.context.scene.cursor.location = box_location

    # Scale the box object to match the cell size.
    bpy.ops.transform.resize(value=(cell_size, cell_size, cell_size))

    # Create a new sphere object as a child of the box object.
    sphere_scale = (random.uniform(0.5, 1.5), random.uniform(0.5, 1.5), random.uniform(0.5, 1.5))
    sphere_location = (0.0, 0.5 * sphere_scale[1], 0.0)
    sphere = bpy.ops.mesh.primitive_uv_sphere_add()
    bpy.context.scene.cursor.location = sphere_location
    bpy.ops.transform.resize(value=sphere_scale)

    # Set the sphere object as a child of the box object.
    sphere.parent = box

    # Create a new cylinder object as a child of the box object.
    cylinder_scale = (random.uniform(0.5, 1.5), random.uniform(0.5, 1.5), random.uniform(0.5, 1.5))
    cylinder_location = (0.0, -0.5 * cylinder_scale[1], 0.0)
    cylinder = bpy.ops.mesh.primitive_cylinder_add()
    bpy.context.scene.cursor.location = cylinder_location
    bpy.ops.transform.resize(value=cylinder_scale)

    # Set the cylinder object as a child of the box object.
    cylinder.parent = box

    return box, sphere_scale[1] + cylinder_scale[1]

# Create a list to hold the box objects and their child sizes.
boxes = []

# Create the grid of boxes.
for row in range(num_rows):
    boxes.append([])
    for col in range(num_columns):
        box, child_size = create_box_with_child()
        boxes[row].append((box, child_size))

# Check the sizes of the child objects and change the color of the parent box if necessary.
for row in range(num_rows):
    for col in range(num_columns):
        box, child_size = boxes[row][col]
        parent_color = (1.0, 1.0, 1.0)
        if child_size > 1.0:
            parent_color = (1.0, 0.0, 0.0)
            box.children.clear()
        box.color = parent_color
