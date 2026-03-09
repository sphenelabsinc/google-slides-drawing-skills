# Responses

## Response


A single response from an update.

| JSON representation |
|---|
| ``` { "createSlide": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#CreateSlideResponse`) }, "createShape": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#CreateShapeResponse`) }, "createTable": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#CreateTableResponse`) }, "replaceAllText": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#ReplaceAllTextResponse`) }, "createImage": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#CreateImageResponse`) }, "createVideo": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#CreateVideoResponse`) }, "createSheetsChart": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#CreateSheetsChartResponse`) }, "createLine": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#CreateLineResponse`) }, "replaceAllShapesWithImage": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#ReplaceAllShapesWithImageResponse`) }, "duplicateObject": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#DuplicateObjectResponse`) }, "replaceAllShapesWithSheetsChart": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#ReplaceAllShapesWithSheetsChartResponse`) }, "groupObjects": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#GroupObjectsResponse`) } } ``` |

| Fields ||
|---|---|
| Union field `kind`. The kind of reply. May have no fields set if the request had no response. `kind` can be only one of the following: ||
| `createSlide` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#CreateSlideResponse`)`` The result of creating a slide. |
| `createShape` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#CreateShapeResponse`)`` The result of creating a shape. |
| `createTable` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#CreateTableResponse`)`` The result of creating a table. |
| `replaceAllText` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#ReplaceAllTextResponse`)`` The result of replacing text. |
| `createImage` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#CreateImageResponse`)`` The result of creating an image. |
| `createVideo` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#CreateVideoResponse`)`` The result of creating a video. |
| `createSheetsChart` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#CreateSheetsChartResponse`)`` The result of creating a Google Sheets chart. |
| `createLine` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#CreateLineResponse`)`` The result of creating a line. |
| `replaceAllShapesWithImage` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#ReplaceAllShapesWithImageResponse`)`` The result of replacing all shapes matching some criteria with an image. |
| `duplicateObject` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#DuplicateObjectResponse`)`` The result of duplicating an object. |
| `replaceAllShapesWithSheetsChart` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#ReplaceAllShapesWithSheetsChartResponse`)`` The result of replacing all shapes matching some criteria with a Google Sheets chart. |
| `groupObjects` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/response#GroupObjectsResponse`)`` The result of grouping objects. |

## CreateSlideResponse


The result of creating a slide.

| JSON representation |
|---|
| ``` { "objectId": string } ``` |

| Fields ||
|---|---|
| `objectId` | `string` The object ID of the created slide. |

## CreateShapeResponse


The result of creating a shape.

| JSON representation |
|---|
| ``` { "objectId": string } ``` |

| Fields ||
|---|---|
| `objectId` | `string` The object ID of the created shape. |

## CreateTableResponse


The result of creating a table.

| JSON representation |
|---|
| ``` { "objectId": string } ``` |

| Fields ||
|---|---|
| `objectId` | `string` The object ID of the created table. |

## ReplaceAllTextResponse


The result of replacing text.

| JSON representation |
|---|
| ``` { "occurrencesChanged": integer } ``` |

| Fields ||
|---|---|
| `occurrencesChanged` | `integer` The number of occurrences changed by replacing all text. |

## CreateImageResponse


The result of creating an image.

| JSON representation |
|---|
| ``` { "objectId": string } ``` |

| Fields ||
|---|---|
| `objectId` | `string` The object ID of the created image. |

## CreateVideoResponse


The result of creating a video.

| JSON representation |
|---|
| ``` { "objectId": string } ``` |

| Fields ||
|---|---|
| `objectId` | `string` The object ID of the created video. |

## CreateSheetsChartResponse


The result of creating an embedded Google Sheets chart.

| JSON representation |
|---|
| ``` { "objectId": string } ``` |

| Fields ||
|---|---|
| `objectId` | `string` The object ID of the created chart. |

## CreateLineResponse


The result of creating a line.

| JSON representation |
|---|
| ``` { "objectId": string } ``` |

| Fields ||
|---|---|
| `objectId` | `string` The object ID of the created line. |

## ReplaceAllShapesWithImageResponse


The result of replacing shapes with an image.

| JSON representation |
|---|
| ``` { "occurrencesChanged": integer } ``` |

| Fields ||
|---|---|
| `occurrencesChanged` | `integer` The number of shapes replaced with images. |

## DuplicateObjectResponse


The response of duplicating an object.

| JSON representation |
|---|
| ``` { "objectId": string } ``` |

| Fields ||
|---|---|
| `objectId` | `string` The ID of the new duplicate object. |

## ReplaceAllShapesWithSheetsChartResponse


The result of replacing shapes with a Google Sheets chart.

| JSON representation |
|---|
| ``` { "occurrencesChanged": integer } ``` |

| Fields ||
|---|---|
| `occurrencesChanged` | `integer` The number of shapes replaced with charts. |

## GroupObjectsResponse


The result of grouping objects.

| JSON representation |
|---|
| ``` { "objectId": string } ``` |

| Fields ||
|---|---|
| `objectId` | `string` The object ID of the created group. |