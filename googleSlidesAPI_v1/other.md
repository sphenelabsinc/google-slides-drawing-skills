# Other

### AffineTransform


AffineTransform uses a 3x3 matrix with an implied last row of \[ 0 0 1 \] to transform source coordinates (x,y) into destination coordinates (x', y') according to:

     [ x']   [  scaleX  shearX  translateX  ] [ x ]
     [ y'] = [  shearY  scaleY  translateY  ] [ y ]
     [ 1 ]   [      0       0         1     ] [ 1 ]


After transformation,

     x' = scaleX * x + shearX * y + translateX;
     y' = scaleY * y + shearY * x + translateY;


This message is therefore composed of these six matrix elements.

| JSON representation |
|---|
| ``` { "scaleX": number, "scaleY": number, "shearX": number, "shearY": number, "translateX": number, "translateY": number, "unit": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Unit`) } ``` |

| Fields ||
|---|---|
| `scaleX` | `number` The X coordinate scaling element. |
| `scaleY` | `number` The Y coordinate scaling element. |
| `shearX` | `number` The X coordinate shearing element. |
| `shearY` | `number` The Y coordinate shearing element. |
| `translateX` | `number` The X coordinate translation element. |
| `translateY` | `number` The Y coordinate translation element. |
| `unit` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Unit`)`` The units for translate elements. |

### OpaqueColor


A themeable solid color value.

| JSON representation |
|---|
| ``` { "rgbColor": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.RgbColor`) }, "themeColor": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.ThemeColorType`) } ``` |

| Fields ||
|---|---|
| Union field `kind`. The kind of color value. `kind` can be only one of the following: ||
| `rgbColor` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.RgbColor`)`` An opaque RGB color. |
| `themeColor` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.ThemeColorType`)`` An opaque theme color. |

### RgbColor


An RGB color.

| JSON representation |
|---|
| ``` { "red": number, "green": number, "blue": number } ``` |

| Fields ||
|---|---|
| `red` | `number` The red component of the color, from 0.0 to 1.0. |
| `green` | `number` The green component of the color, from 0.0 to 1.0. |
| `blue` | `number` The blue component of the color, from 0.0 to 1.0. |

### ThemeColorType


Theme color types.


`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page.PageProperties`
contain a
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page.ColorScheme`
that defines a mapping of these theme color types to concrete colors.

| Enums ||
|---|---|
| `THEME_COLOR_TYPE_UNSPECIFIED` | Unspecified theme color. This value should not be used. |
| `DARK1` | Represents the first dark color. |
| `LIGHT1` | Represents the first light color. |
| `DARK2` | Represents the second dark color. |
| `LIGHT2` | Represents the second light color. |
| `ACCENT1` | Represents the first accent color. |
| `ACCENT2` | Represents the second accent color. |
| `ACCENT3` | Represents the third accent color. |
| `ACCENT4` | Represents the fourth accent color. |
| `ACCENT5` | Represents the fifth accent color. |
| `ACCENT6` | Represents the sixth accent color. |
| `HYPERLINK` | Represents the color to use for hyperlinks. |
| `FOLLOWED_HYPERLINK` | Represents the color to use for visited hyperlinks. |
| `TEXT1` | Represents the first text color. |
| `BACKGROUND1` | Represents the first background color. |
| `TEXT2` | Represents the second text color. |
| `BACKGROUND2` | Represents the second background color. |

### Link


A hypertext link.

| JSON representation |
|---|
| ``` { "url": string, "relativeLink": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.RelativeSlideLink`), "pageObjectId": string, "slideIndex": integer } ``` |

| Fields ||
|---|---|
| Union field `kind`. The kinds of links. `kind` can be only one of the following: ||
| `url` | `string` If set, indicates this is a link to the external web page at this URL. |
| `relativeLink` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.RelativeSlideLink`)`` If set, indicates this is a link to a slide in this presentation, addressed by its position. |
| `pageObjectId` | `string` If set, indicates this is a link to the specific page in this presentation with this ID. A page with this ID may not exist. |
| `slideIndex` | `integer` If set, indicates this is a link to the slide at this zero-based index in the presentation. There may not be a slide at this index. |

### RelativeSlideLink


The kinds of relative links.

| Enums ||
|---|---|
| `RELATIVE_SLIDE_LINK_UNSPECIFIED` | An unspecified relative slide link. |
| `NEXT_SLIDE` | A link to the next slide. |
| `PREVIOUS_SLIDE` | A link to the previous slide. |
| `FIRST_SLIDE` | A link to the first slide in the presentation. |
| `LAST_SLIDE` | A link to the last slide in the presentation. |

### PropertyState


The possible states of a property.

| Enums ||
|---|---|
| `RENDERED` | If a property's state is RENDERED, then the element has the corresponding property when rendered on a page. If the element is a placeholder shape as determined by the `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/shapes#Page.Shape.FIELDS.placeholder` field, and it inherits from a placeholder shape, the corresponding field may be unset, meaning that the property value is inherited from a parent placeholder. If the element does not inherit, then the field will contain the rendered value. This is the default value. |
| `NOT_RENDERED` | If a property's state is NOT_RENDERED, then the element does not have the corresponding property when rendered on a page. However, the field may still be set so it can be inherited by child shapes. To remove a property from a rendered element, set its propertyState to NOT_RENDERED. |
| `INHERIT` | If a property's state is INHERIT, then the property state uses the value of corresponding `propertyState` field on the parent shape. Elements that do not inherit will never have an INHERIT property state. |

### SolidFill


A solid color fill. The page or page element is filled entirely with the specified color value.


If any field is unset, its value may be inherited from a parent placeholder if it exists.

| JSON representation |
|---|
| ``` { "color": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.OpaqueColor`) }, "alpha": number } ``` |

| Fields ||
|---|---|
| `color` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.OpaqueColor`)`` The color value of the solid fill. |
| `alpha` | `number` The fraction of this `color` that should be applied to the pixel. That is, the final pixel color is defined by the equation: pixel color = alpha \* (color) + (1.0 - alpha) \* (background color) This means that a value of 1.0 corresponds to a solid color, whereas a value of 0.0 corresponds to a completely transparent color. |

### Outline


The outline of a
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page.PageElement`.


If these fields are unset, they may be inherited from a parent placeholder if it exists. If there is no parent, the fields will default to the value used for new page elements created in the Slides editor, which may depend on the page element kind.

| JSON representation |
|---|
| ``` { "outlineFill": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.OutlineFill`) }, "weight": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`) }, "dashStyle": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.DashStyle`), "propertyState": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.PropertyState`) } ``` |

| Fields ||
|---|---|
| `outlineFill` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.OutlineFill`)`` The fill of the outline. |
| `weight` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`)`` The thickness of the outline. |
| `dashStyle` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.DashStyle`)`` The dash style of the outline. |
| `propertyState` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.PropertyState`)`` The outline property state. Updating the outline on a page element will implicitly update this field to `RENDERED`, unless another value is specified in the same request. To have no outline on a page element, set this field to `NOT_RENDERED`. In this case, any other outline fields set in the same request will be ignored. |

### OutlineFill


The fill of the outline.

| JSON representation |
|---|
| ``` { "solidFill": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.SolidFill`) } } ``` |

| Fields ||
|---|---|
| Union field `kind`. The kind of outline fill. `kind` can be only one of the following: ||
| `solidFill` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.SolidFill`)`` Solid color fill. |

### DashStyle


The kinds of dashes with which linear geometry can be rendered. These values are based on the "ST_PresetLineDashVal" simple type described in section 20.1.10.49 of "Office Open XML File Formats - Fundamentals and Markup Language Reference", part 1 of
[ECMA-376 5th edition](https://ecma-international.org/publications-and-standards/standards/ecma-376/).

| Enums ||
|---|---|
| `DASH_STYLE_UNSPECIFIED` | Unspecified dash style. |
| `SOLID` | Solid line. Corresponds to ECMA-376 ST_PresetLineDashVal value 'solid'. This is the default dash style. |
| `DOT` | Dotted line. Corresponds to ECMA-376 ST_PresetLineDashVal value 'dot'. |
| `DASH` | Dashed line. Corresponds to ECMA-376 ST_PresetLineDashVal value 'dash'. |
| `DASH_DOT` | Alternating dashes and dots. Corresponds to ECMA-376 ST_PresetLineDashVal value 'dashDot'. |
| `LONG_DASH` | Line with large dashes. Corresponds to ECMA-376 ST_PresetLineDashVal value 'lgDash'. |
| `LONG_DASH_DOT` | Alternating large dashes and dots. Corresponds to ECMA-376 ST_PresetLineDashVal value 'lgDashDot'. |

### Shadow


The shadow properties of a page element.


If these fields are unset, they may be inherited from a parent placeholder if it exists. If there is no parent, the fields will default to the value used for new page elements created in the Slides editor, which may depend on the page element kind.

| JSON representation |
|---|
| ``` { "type": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Type_2`), "transform": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.AffineTransform`) }, "alignment": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.RectanglePosition`), "blurRadius": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`) }, "color": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.OpaqueColor`) }, "alpha": number, "rotateWithShape": boolean, "propertyState": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.PropertyState`) } ``` |

| Fields ||
|---|---|
| `type` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Type_2`)`` The type of the shadow. This property is read-only. |
| `transform` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.AffineTransform`)`` Transform that encodes the translate, scale, and skew of the shadow, relative to the alignment position. |
| `alignment` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.RectanglePosition`)`` The alignment point of the shadow, that sets the origin for translate, scale and skew of the shadow. This property is read-only. |
| `blurRadius` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Dimension`)`` The radius of the shadow blur. The larger the radius, the more diffuse the shadow becomes. |
| `color` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.OpaqueColor`)`` The shadow color value. |
| `alpha` | `number` The alpha of the shadow's color, from 0.0 to 1.0. |
| `rotateWithShape` | `boolean` Whether the shadow should rotate with the shape. This property is read-only. |
| `propertyState` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.PropertyState`)`` The shadow property state. Updating the shadow on a page element will implicitly update this field to `RENDERED`, unless another value is specified in the same request. To have no shadow on a page element, set this field to `NOT_RENDERED`. In this case, any other shadow fields set in the same request will be ignored. |

### Type


The shadow types.

| Enums ||
|---|---|
| `SHADOW_TYPE_UNSPECIFIED` | Unspecified shadow type. |
| `OUTER` | Outer shadow. |

### RectanglePosition


Defines reference positions in a rectangle.

| Enums ||
|---|---|
| `RECTANGLE_POSITION_UNSPECIFIED` | Unspecified. |
| `TOP_LEFT` | Top left. |
| `TOP_CENTER` | Top center. |
| `TOP_RIGHT` | Top right. |
| `LEFT_CENTER` | Left center. |
| `CENTER` | Center. |
| `RIGHT_CENTER` | Right center. |
| `BOTTOM_LEFT` | Bottom left. |
| `BOTTOM_CENTER` | Bottom center. |
| `BOTTOM_RIGHT` | Bottom right. |

### ContentAlignment


The types of content alignment.


Derived from a subset of the values of the "ST_TextAnchoringType" simple type in section 20.1.10.60 of "Office Open XML File Formats - Fundamentals and Markup Language Reference", part 1 of
[ECMA-376 5th edition](https://ecma-international.org/publications-and-standards/standards/ecma-376/).

| Enums ||
|---|---|
| `CONTENT_ALIGNMENT_UNSPECIFIED` | An unspecified content alignment. The content alignment is inherited from the parent if it exists. |
| `CONTENT_ALIGNMENT_UNSUPPORTED` | An unsupported content alignment. |
| `TOP` | An alignment that aligns the content to the top of the content holder. Corresponds to ECMA-376 ST_TextAnchoringType 't'. |
| `MIDDLE` | An alignment that aligns the content to the middle of the content holder. Corresponds to ECMA-376 ST_TextAnchoringType 'ctr'. |
| `BOTTOM` | An alignment that aligns the content to the bottom of the content holder. Corresponds to ECMA-376 ST_TextAnchoringType 'b'. |

### Placeholder


The placeholder information that uniquely identifies a placeholder shape.

| JSON representation |
|---|
| ``` { "type": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Type_3`), "index": integer, "parentObjectId": string } ``` |

| Fields ||
|---|---|
| `type` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Type_3`)`` The type of the placeholder. |
| `index` | `integer` The index of the placeholder. If the same placeholder types are present in the same page, they would have different index values. |
| `parentObjectId` | `string` The object ID of this shape's parent placeholder. If unset, the parent placeholder shape does not exist, so the shape does not inherit properties from any other shape. |

### Type


The type of a placeholder shape.


Many of these placeholder types correspond to placeholder IDs from the ECMA-376 standard. For more information, see the description of the "ST_PlaceholderType" type in section 19.7.10 of "Office Open XML File Formats - Fundamentals and Markup Language Reference", part 1 of
[ECMA-376 5th edition](https://ecma-international.org/publications-and-standards/standards/ecma-376/).

| Enums ||
|---|---|
| `NONE` | Default value, signifies it is not a placeholder. |
| `BODY` | Body text. |
| `CHART` | Chart or graph. |
| `CLIP_ART` | Clip art image. |
| `CENTERED_TITLE` | Title centered. |
| `DIAGRAM` | Diagram. |
| `DATE_AND_TIME` | Date and time. |
| `FOOTER` | Footer text. |
| `HEADER` | Header text. |
| `MEDIA` | Multimedia. |
| `OBJECT` | Any content type. |
| `PICTURE` | Picture. |
| `SLIDE_NUMBER` | Number of a slide. |
| `SUBTITLE` | Subtitle. |
| `TABLE` | Table. |
| `TITLE` | Slide title. |
| `SLIDE_IMAGE` | Slide image. |

### ImageProperties


The properties of the
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/images#Page.Image`.

| JSON representation |
|---|
| ``` { "cropProperties": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.CropProperties`) }, "transparency": number, "brightness": number, "contrast": number, "recolor": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Recolor`) }, "outline": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Outline`) }, "shadow": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Shadow`) }, "link": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Link`) } } ``` |

| Fields ||
|---|---|
| `cropProperties` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.CropProperties`)`` The crop properties of the image. If not set, the image is not cropped. This property is read-only. |
| `transparency` | `number` The transparency effect of the image. The value should be in the interval \[0.0, 1.0\], where 0 means no effect and 1 means completely transparent. This property is read-only. |
| `brightness` | `number` The brightness effect of the image. The value should be in the interval \[-1.0, 1.0\], where 0 means no effect. This property is read-only. |
| `contrast` | `number` The contrast effect of the image. The value should be in the interval \[-1.0, 1.0\], where 0 means no effect. This property is read-only. |
| `recolor` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Recolor`)`` The recolor effect of the image. If not set, the image is not recolored. This property is read-only. |
| `outline` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Outline`)`` The outline of the image. If not set, the image has no outline. |
| `shadow` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Shadow`)`` The shadow of the image. If not set, the image has no shadow. This property is read-only. |
| `link` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Link`)`` The hyperlink destination of the image. If unset, there is no link. |

### CropProperties


The crop properties of an object enclosed in a container. For example, an
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/images#Page.Image`.


The crop properties is represented by the offsets of four edges which define a crop rectangle. The offsets are measured in percentage from the corresponding edges of the object's original bounding rectangle towards inside, relative to the object's original dimensions.

- If the offset is in the interval (0, 1), the corresponding edge of crop rectangle is positioned inside of the object's original bounding rectangle.
- If the offset is negative or greater than 1, the corresponding edge of crop rectangle is positioned outside of the object's original bounding rectangle.
- If the left edge of the crop rectangle is on the right side of its right edge, the object will be flipped horizontally.
- If the top edge of the crop rectangle is below its bottom edge, the object will be flipped vertically.
- If all offsets and rotation angle is 0, the object is not cropped.


After cropping, the content in the crop rectangle will be stretched to fit its container.

| JSON representation |
|---|
| ``` { "leftOffset": number, "rightOffset": number, "topOffset": number, "bottomOffset": number, "angle": number } ``` |

| Fields ||
|---|---|
| `leftOffset` | `number` The offset specifies the left edge of the crop rectangle that is located to the right of the original bounding rectangle left edge, relative to the object's original width. |
| `rightOffset` | `number` The offset specifies the right edge of the crop rectangle that is located to the left of the original bounding rectangle right edge, relative to the object's original width. |
| `topOffset` | `number` The offset specifies the top edge of the crop rectangle that is located below the original bounding rectangle top edge, relative to the object's original height. |
| `bottomOffset` | `number` The offset specifies the bottom edge of the crop rectangle that is located above the original bounding rectangle bottom edge, relative to the object's original height. |
| `angle` | `number` The rotation angle of the crop window around its center, in radians. Rotation angle is applied after the offset. |

### Recolor


A recolor effect applied on an image.

| JSON representation |
|---|
| ``` { "recolorStops": [ { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.ColorStop`) } ], "name": enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Name`) } ``` |

| Fields ||
|---|---|
| `recolorStops[]` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.ColorStop`)`` The recolor effect is represented by a gradient, which is a list of color stops. The colors in the gradient will replace the corresponding colors at the same position in the color palette and apply to the image. This property is read-only. |
| `name` | ``enum (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Name`)`` The name of the recolor effect. The name is determined from the `recolorStops` by matching the gradient against the colors in the page's current `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page.PageProperties.FIELDS.color_scheme`. This property is read-only. |

### ColorStop


A color and position in a gradient band.

| JSON representation |
|---|
| ``` { "color": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.OpaqueColor`) }, "alpha": number, "position": number } ``` |

| Fields ||
|---|---|
| `color` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.OpaqueColor`)`` The color of the gradient stop. |
| `alpha` | `number` The alpha value of this color in the gradient band. Defaults to 1.0, fully opaque. |
| `position` | `number` The relative position of the color stop in the gradient band measured in percentage. The value should be in the interval \[0.0, 1.0\]. |

### Name


The recolor effect names.

| Enums ||
|---|---|
| `NONE` | No recolor effect. The default value. |
| `LIGHT1` | A recolor effect that lightens the image using the page's first available color from its color scheme. |
| `LIGHT2` | A recolor effect that lightens the image using the page's second available color from its color scheme. |
| `LIGHT3` | A recolor effect that lightens the image using the page's third available color from its color scheme. |
| `LIGHT4` | A recolor effect that lightens the image using the page's fourth available color from its color scheme. |
| `LIGHT5` | A recolor effect that lightens the image using the page's fifth available color from its color scheme. |
| `LIGHT6` | A recolor effect that lightens the image using the page's sixth available color from its color scheme. |
| `LIGHT7` | A recolor effect that lightens the image using the page's seventh available color from its color scheme. |
| `LIGHT8` | A recolor effect that lightens the image using the page's eighth available color from its color scheme. |
| `LIGHT9` | A recolor effect that lightens the image using the page's ninth available color from its color scheme. |
| `LIGHT10` | A recolor effect that lightens the image using the page's tenth available color from its color scheme. |
| `DARK1` | A recolor effect that darkens the image using the page's first available color from its color scheme. |
| `DARK2` | A recolor effect that darkens the image using the page's second available color from its color scheme. |
| `DARK3` | A recolor effect that darkens the image using the page's third available color from its color scheme. |
| `DARK4` | A recolor effect that darkens the image using the page's fourth available color from its color scheme. |
| `DARK5` | A recolor effect that darkens the image using the page's fifth available color from its color scheme. |
| `DARK6` | A recolor effect that darkens the image using the page's sixth available color from its color scheme. |
| `DARK7` | A recolor effect that darkens the image using the page's seventh available color from its color scheme. |
| `DARK8` | A recolor effect that darkens the image using the page's eighth available color from its color scheme. |
| `DARK9` | A recolor effect that darkens the image using the page's ninth available color from its color scheme. |
| `DARK10` | A recolor effect that darkens the image using the page's tenth available color from its color scheme. |
| `GRAYSCALE` | A recolor effect that recolors the image to grayscale. |
| `NEGATIVE` | A recolor effect that recolors the image to negative grayscale. |
| `SEPIA` | A recolor effect that recolors the image using the sepia color. |
| `CUSTOM` | Custom recolor effect. Refer to `recolorStops` for the concrete gradient. |