This dataset is about tree preservation areas. These are areas of trees that are under a TPO. You may also know them as tree preservation
zones or groups.

The dataset must contain at least one entry (row) for each tree preservation area.

It must containing the following fields (columns):

### reference

A reference or ID for each tree preservation area that is:

-   unique within your dataset
-   permanent - it doesn't change when the dataset is updated

If you don't use a reference already, you will need to create one. This can be a short set of letters or numbers.

Example: `TPA1`

### name

This will be the display name of the page hosting data about this tree preservation area on our website. This can be:

-   name
-   reference
-   address
-   blank

### tree-preservation-order

The reference for the tree preservation order that covers this area.

### geometry

The boundary for the tree preservation area as a single polygon or multipolygon value. Points must be in the WGS84 coordinate reference system.

This should be in GeoJSON format.

Example:
`MULTIPOLYGON (((1.188829 51.23478,1.188376 51.234909,1.188381 51.234917,1.187912 51.235022...`

### notes

Optional text on how this data was made or produced, or how it can be interpreted.

### start-date

The date that the TPA came into force, written in `YYYY-MM-DD` format.

Example: `1984-03-28`

### end-date

If applicable, the date that the TPA was no longer in effect, written in `YYYY-MM-DD` format. If it's still in effect, leave the cell blank.

Example: `1999-01-20`

### entry-date

The date this dataset was created or last updated, written in `YYYY-MM-DD` format.

Example: `2022-12-20`
