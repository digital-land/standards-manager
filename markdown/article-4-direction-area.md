This dataset is about the geometry that each article 4 direction refers to.

The dataset must contain at least one entry (row) for each article 4 direction area.

It must containing the following fields (columns):

### reference

A reference or ID for each article 4 direction area that is:

- unique within your dataset
- permanent - it doesn’t change when the dataset is updated

If you don’t use a reference already, you will need to create one. This can be a short set of letters or numbers.

Example: `A4Da1`

### name

The official name of the article 4 direction.
Example: Old Market
geometry

The boundary for the article 4 direction area as a single polygon or multipolygon value. Points must be in the WGS84 coordinate reference system.

This should be in GeoJSON format.

Example: `MULTIPOLYGON (((1.188829 51.23478,1.188376 51.234909,1.188381 51.234917,1.187912 51.235022...`

### uprn

If the geometry is the boundary of a building, you can provide the Unique Property Reference Number (UPRN). Find the UPRN on GeoPlace.

If you provide the UPRN, you must also provide the address text.

### address-text

If the geometry is the boundary of a building, you can provide the address of the article 4 direction, written as text.

If you provide the address text, you must also provide the UPRN.

Example: `100 High Street, Bath`

### article-4-direction

The reference for the article 4 direction used in the article 4 direction dataset.

Example: `A4D1`
