# Images

### Image


A
`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages#Page.PageElement`
kind representing an image.

| JSON representation |
|---|
| ``` { "contentUrl": string, "imageProperties": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.ImageProperties`) }, "sourceUrl": string, "placeholder": { object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Placeholder`) } } ``` |

| Fields ||
|---|---|
| `contentUrl` | `string` An URL to an image with a default lifetime of 30 minutes. This URL is tagged with the account of the requester. Anyone with the URL effectively accesses the image as the original requester. Access to the image may be lost if the presentation's sharing settings change. |
| `imageProperties` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.ImageProperties`)`` The properties of the image. |
| `sourceUrl` | `string` The source URL is the URL used to insert the image. The source URL can be empty. |
| `placeholder` | ``object (`https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Placeholder`)`` Placeholders are page elements that inherit from corresponding placeholders on layouts and masters. If set, the image is a placeholder image and any inherited properties can be resolved by looking at the parent placeholder identified by the `https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/other#Page.Placeholder.FIELDS.parent_object_id` field. |