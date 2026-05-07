# Interface Settings

## Table Styles

Styles define the appearance of tables in the Excel file: fonts, colors, alignment.

### Where to find it

**Styles** tab in the main window.

### Built-in styles

The program includes several ready-made styles:

| Style | Description |
|---|---|
| `default` | Standard style (Arial, 10pt, black-and-white with colored accents) |
| `black_and_white` | Black and white style |
| `orange` | Style with orange accents |
| `red_and_blue` | Style with red and blue accents |

### Style elements

Each style consists of a set of elements corresponding to parts of the table:

| Element | Description |
|---|---|
| `info` | Information row (filter, split) |
| `td.basedata` | Base data (number of respondents) |
| `td.basedata_low` | Base data with low base (marker) |
| `td.basetext` | "Base" / "Total" text |
| `td.corner` | Corner cell (intersection of rows and columns) |
| `td.data` | Main table data (percentages, counts) |
| `td.meandata` | Statistics data (mean, median, etc.) |
| `td.meantext` | Statistics text ("Mean", "Median", etc.) |
| `td.q1alt` | Question alternatives in rows (Left) |
| `td.q1text` | Question text in rows (Left) |
| `td.q1total` | Total row for rows |
| `td.q2alt` | Question alternatives in columns (Top) |
| `td.q2text` | Question text in columns (Top) |
| `td.q2total` | Total column for columns |
| `td.stat` | Statistics rows |
| `td.totaldata` | Data in Total row/column |
| `td.totalstat` | Statistics in Total row/column |
| `td.signifabc` | Column letter labels (A, B, C...) |
| `td.signif` | Significance cells |
| `td.signif_more` | Significantly higher (green highlight) |
| `td.signif_less` | Significantly lower (pink highlight) |

### Parameters for each element

Each style element can be configured with:

| Parameter | Values |
|---|---|
| **FontName** | `Calibri`, `Arial`, `Tahoma`, `Verdana` |
| **FontSize** | Font size (number) |
| **FontBold** | Bold: `true` / `false` |
| **FontItalic** | Italic: `true` / `false` |
| **FontColor** | Text color (format `$RRGGBB`) |
| **HorizontalAlign** | `left`, `center`, `justify`, `right` |
| **VerticalAlign** | `top`, `middle`, `bottom` |
| **BackgroundColor** | Background color (format `$RRGGBB`) |
| **WordWrap** | Word wrap: `true` / `false` |

### Creating a new style

1. Click the **New Style** button (➕)
2. Enter a style name (only letters `a-z`, `0-9` and `_`)
3. Configure each element by double-clicking in the elements list

### Copying a style

1. Select a style from the list
2. Click the **Copy Style** button (📋)
3. Enter a new name

### Deleting a style

1. Select a style (not `default`)
2. Click the **Delete Style** button (🗑)

> ⚠️ The `default` style cannot be deleted.

### Editing a style element

1. Select an element in the left list
2. Double-click → the edit window opens
3. Change font, color, alignment parameters
4. Click **OK** to save

A table preview with the current style is displayed to the right of the elements list.

### Style files

Styles are stored in the `styles/` folder in INI format:

```ini
[td.data]
FontName=arial
FontSize=10
FontBold=false
FontItalic=false
HorizontalAlign=center
VerticalAlign=middle
FontColor=$000000
BackgroundColor=$FFFFFF
WordWrap=true
```

---

## Localization

The program supports two interface languages:

| Language | Code |
|---|---|
| 🇺🇦 Ukrainian | `uk` |
| 🇺🇸 English | `en` |

### How to change language

Menu **Language** → select the desired language.

Localization files are stored in the `lang/` folder:

- `DataTable2.uk.po` / `DataTable2.uk.mo` — Ukrainian
- `DataTable2.en.po` / `DataTable2.en.mo` — English
- `DataTable2.pot` — template for new translations

---

## Saving and Loading Settings

### Automatic saving

Array settings (filter, weight, split, table parameters, transform, style) are automatically saved in an XML file next to the FRM array.

### Manual save/load

Menu **Settings**:

- **Save settings** — saves current settings
- **Load settings** — restores saved settings

### What is saved

| Parameter | Description |
|---|---|
| `Left_Signs` | List of variables in rows |
| `Top_Signs` | List of variables in columns |
| `Weight_Sign` | Weighting variable |
| `Filter_Formula` | Filter formula |
| `Split_Sign` | Split variable |
| `TabOptions` | All table settings (statistics, significance, boxes, sorting, etc.) |
| `Transform` | Transform text |
| `StylesName` | Selected style name |
| `SavedFilters` | Saved filters |
| `Lang` | Interface language |

---

## Main Window Tabs

| Tab | Description |
|---|---|
| **Signs** | Array question list, alternative preview, quick filter |
| **Table Settings** | Rows/columns, statistics, significance, boxes, sorting |
| **Filters** | Filter formula input, saved filters |
| **Transform** | Create new variables by formula |
| **Output** | View built tables (Excel), file list |
| **Styles** | Table style management |

---

## Log

At the bottom of the window there is a log panel displaying:

- Information messages (white background)
- Warnings (yellow background)
- Errors (red background)

The log helps track operation execution and diagnose errors.
