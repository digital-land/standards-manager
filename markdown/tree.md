This dataset is about trees. These are individual trees that are under a TPO.

The dataset must contain at least one entry (row) for each tree.

It must containing the following fields (columns):

### reference

A reference or ID for each tree that is:

-   unique within your dataset
-   permanent - it doesn't change when the dataset is updated

If you don't use a reference already, you will need to create one. This can be a short set of letters or numbers.

Example: `T1`

### name

This will be the title of the page hosting data about this TPO on our website. This can be:

-   name
-   reference
-   address
-   blank

### point

The approximate location of the centre of the tree.

You must provide a point or geometry for each tree. You may provide both.

### tree-preservation-order

The reference for the tree preservation order that affects this tree.

Example: `TPO1`

### geometry

The boundary of the tree as a single polygon or multipolygon value. Points must be in the WGS84 coordinate reference system.

This should be in GeoJSON format.

You must provide a point or geometry for each tree. You may provide both.

Example:
`MULTIPOLYGON (((1.188829 51.23478,1.188376 51.234909,1.188381 51.234917,1.187912 51.235022...`

### uprn

If the tree has one, you can provide the Unique Property Reference Number (UPRN). [Find the UPRN on GeoPlace](https://www.geoplace.co.uk/addresses-streets/location-data/the-uprn).

If you provide the UPRN, you must also provide the address text.

### address-text

If the tree has one, you can provide the address, written as text.

If you provide the address text, you must also provide the UPRN.

Example: `100 High Street, Bath`

### notes

Optional text on how this data was made or produced, or how it can be interpreted.

### start-date

The date from which the tree preservation order affects the tree, written in `YYYY-MM-DD` format.

Example: `1984-03-28`

### end-date

If applicable, the date from which the tree preservation order no longer affects the tree, written in `YYYY-MM-DD` format. If it's still in effect, leave the cell blank.

Example: `1999-01-20`

entry-date

The date this dataset was created or last updated, written in `YYYY-MM-DD` format.

Example: `2022-12-20`
