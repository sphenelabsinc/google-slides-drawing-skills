# Shapes Properties Digest

Key `Page.ShapeProperties` fields from `googleSlidesAPI_v1/shapes.md` that you tweak when styling nodes.

- **Shape background**: `shapeBackgroundFill` holds the `SolidFill`, gradient, or picture fill. If you leave it unset, the placeholder/parent shape supplies the value.
- **Outline**: `outline` defines stroke color (`outlineFill`), weight, and dash style. The outline is inherited unless you override it per shape.
- **Shadow/link**: `shadow` adds depth, while `link` attaches click behavior.
- **Content alignment**: `contentAlignment` (START/CENTER/END) moves text inside the shape, and `autofit` (NONE/SHRINK_TO_FIT/RESIZE_SHAPE) controls wrapping behavior.
- **Placeholder inheritance**: `shapeProperties` may be overridden by parent placeholders; check `PropertyState` when you want to know whether a value is inherited or user-specified.

Use this digest to remember which fill/outline/shadow field to set when you style a shape.
