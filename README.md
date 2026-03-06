# Blender Collection Render Key Tool

A lightweight **Blender Add-on** that allows you to **set, clear, and
control render visibility keyframes for all objects inside a
collection**.

This tool is useful for **scene management, animation visibility
control, and render setup workflows**.

------------------------------------------------------------------------

## Features

-   Set **Render Visibility Keyframes** for all objects in a collection
-   Clear all **Render Visibility Keyframes**
-   Enable render visibility for an entire collection
-   Disable render visibility for an entire collection
-   Safe handling of objects without animation data
-   Simple UI inside the **Blender Sidebar**

------------------------------------------------------------------------

## UI Location

3D Viewport → Press **N** → **Render Keys** → *Collection Render Tool*

------------------------------------------------------------------------

## Installation

1.  Download the add-on script.

2.  Open **Blender**

3.  Go to:

Edit → Preferences → Add-ons

4.  Click **Install**

5.  Select the file:

`collection_render_key_tool.py`

6.  Enable the add-on.

------------------------------------------------------------------------

## Usage

### 1. Select a Collection

Choose the collection containing the objects you want to control.

------------------------------------------------------------------------

### 2. Set Render Key

Press **Set Render Key**

This will insert a **render visibility keyframe (`hide_render`)** for
all objects in the collection at the current frame.

------------------------------------------------------------------------

### 3. Clear Render Keys

Press **Clear Render Keys**

This removes all render visibility animation from objects in the
collection.

------------------------------------------------------------------------

### 4. Render Enable

Press **Render Enable**

This sets:

`hide_render = False`

for all objects in the collection.

------------------------------------------------------------------------

### 5. Render Disable

Press **Render Disable**

This sets:

`hide_render = True`

for all objects in the collection.

------------------------------------------------------------------------

## Example Workflow

Collection structure:

Train ├ Wheel_01 ├ Wheel_02 ├ Brake_System └ Suspension

Steps:

1.  Select collection **Train**
2.  Move timeline to **Frame 50**
3.  Click **Set Render Key**

All objects inside the collection receive a render visibility keyframe.

------------------------------------------------------------------------

## Requirements

-   Blender **4.0+**

------------------------------------------------------------------------

## Future Improvements

Possible upcoming features:

-   Recursive support for **sub-collections**
-   **Viewport visibility keyframes**
-   **Frame range visibility tools**
-   **Batch visibility manager**
-   Integration with **shot management workflows**

------------------------------------------------------------------------

## Author

**Swapnil Nare**\
Technical Artist\
Pune, India
