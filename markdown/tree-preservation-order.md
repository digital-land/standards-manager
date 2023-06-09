This dataset is about tree preservation orders (TPOs). These are orders made by local planning authorities to protect specific trees, groups of trees or woodlands.

The dataset must contain at least one entry (row) for each TPO.

It must containing the following fields (columns):

### reference

A reference or ID for each tree preservation order that is:

-   unique within your dataset
-   permanent - it doesn't change when the dataset is updated

If you don't use a reference already, you will need to create one. This can be a short set of letters or numbers.

Example: `TPO1`

### name

This will be the title of the page hosting data about this TPO on our website. This can be:

-   name
-   reference
-   address
-   blank

### document-url

The URL of an authoritative order or notice designating the tree preservation order.

Example: `http://www.LPAwebsite.org.uk/tpo1.pdf`

### documentation-url

The URL of the webpage citing the document.

Each document should be linked to on a documentation webpage that includes a short description of the data. The website URL should be unique for each tree preservation order, either by creating a separate page or a separate anchor (fragment identifier) for each one.

Example: `http://www.LPAwebsite.org.uk/data#tpo1`

### notes

Optional text on how this data was made or produced, or how it can be interpreted.

### start-date

The date that the TPO came into force, written in `YYYY-MM-DD` format.

Example: `1984-03-28`

### end-date

If applicable, the date that the TPO was no longer in effect, written in `YYYY-MM-DD` format. If it's still in effect, leave the cell blank.

Example: `1999-01-20`

### entry-date

The date this dataset was created or last updated, written in `YYYY-MM-DD` format.

Example: `2022-12-20`
