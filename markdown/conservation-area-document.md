This dataset is about conservation areas. These are areas where extra planning controls apply due to their special architectural and historic interest.

The dataset must contain at least one entry (row) for each conservation area.

It must containing the following fields (columns):

### reference
A reference or ID for each conservation area that is:

-   unique within your dataset
-   permanent - it doesn't change when the dataset is updated

If you don't use a reference already, you will need to create one. This can be a short set of letters or numbers.

Example: `CA01`

### name

The official name of the conservation area.

Example: `Old Market`

### geometry

The boundary for the conservation area as a single polygon or multipolygon value. Points must be in the WGS84 coordinate reference system.

This should be in GeoJSON format.

Example: `MULTIPOLYGON (((1.188829 51.23478,1.188376 51.234909,1.188381 51.234917,1.187912 51.235022...`

### documentation-url

An optional URL of a document providing the authoritative source of the boundary. For example, a PDF containing a map of the area, indicated with a red-line boundary.

### notes

Optional text on how this data was made or produced, or how it can be interpreted.

### start-date

The date that the conservation area was officially designated, written in `YYYY-MM-DD` format.

Example: `1984-03-28`

### end-date

If applicable, the date that the conservation area was no longer in effect, written in `YYYY-MM-DD` format. If this does not apply, leave the cell blank.

Example: `1999-01-20`

### entry-date

The date this dataset was created or last updated, written in `YYYY-MM-DD` format.

Example: `2022-12-20`
