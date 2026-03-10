# Method: presentations.create

- [HTTP request](https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/create#body.HTTP_TEMPLATE)
- [Request body](https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/create#body.request_body)
  - [JSON representation](https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/create#body.request_body.SCHEMA_REPRESENTATION)
- [Response body](https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/create#body.response_body)
- [Authorization scopes](https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/create#body.aspect)
- [Try it!](https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/create#try-it)

Creates a blank presentation using the title given in the request. If a `presentationId` is provided, it is used as the ID of the new presentation. Otherwise, a new ID is generated. Other fields in the request, including any provided content, are ignored. Returns the created presentation.

### HTTP request

`POST https://slides.googleapis.com/v1/presentations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Request body

The request body contains data with the following structure:

| JSON representation |
|---|
| ``` { "presentationId": string, "pageSize": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Size`) }, "slides": [ { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page`) } ], "title": string, "masters": [ { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page`) } ], "layouts": [ { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page`) } ], "locale": string, "revisionId": string, "notesMaster": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page`) } } ``` |

| Fields ||
|---|---|
| `presentationId` | `string` The ID of the presentation. |
| `pageSize` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/Size`)`` The size of pages in the presentation. |
| `slides[]` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page`)`` The slides in the presentation. A slide inherits properties from a slide layout. |
| `title` | `string` The title of the presentation. |
| `masters[]` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page`)`` The slide masters in the presentation. A slide master contains all common page elements and the common properties for a set of layouts. They serve three purposes: - Placeholder shapes on a master contain the default text styles and shape properties of all placeholder shapes on pages that use that master. - The master page properties define the common page properties inherited by its layouts. - Any other shapes on the master slide appear on all slides using that master, regardless of their layout. |
| `layouts[]` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page`)`` The layouts in the presentation. A layout is a template that determines how content is arranged and styled on the slides that inherit from that layout. |
| `locale` | `string` The locale of the presentation, as an IETF BCP 47 language tag. |
| `revisionId` | `string` Output only. The revision ID of the presentation. Can be used in update requests to assert the presentation revision hasn't changed since the last read operation. Only populated if the user has edit access to the presentation. The revision ID is not a sequential number but a nebulous string. The format of the revision ID may change over time, so it should be treated opaquely. A returned revision ID is only guaranteed to be valid for 24 hours after it has been returned and cannot be shared across users. If the revision ID is unchanged between calls, then the presentation has not changed. Conversely, a changed ID (for the same presentation and user) usually means the presentation has been updated. However, a changed ID can also be due to internal factors such as ID format changes. |
| `notesMaster` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page`)`` The notes master in the presentation. It serves three purposes: - Placeholder shapes on a notes master contain the default text styles and shape properties of all placeholder shapes on `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page.SlideProperties.FIELDS.notes_page`. Specifically, a `SLIDE_IMAGE` placeholder shape contains the slide thumbnail, and a `BODY` placeholder shape contains the speaker notes. - The notes master page properties define the common page properties inherited by all `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page.SlideProperties.FIELDS.notes_page`. - Any other shapes on the notes master appear on all `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page.SlideProperties.FIELDS.notes_page`. The notes master is read-only. |

### Response body

If successful, the response body contains a newly created instance of `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations#Presentation`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/drive.file`
- `https://www.googleapis.com/auth/presentations`

For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).