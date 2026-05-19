# Advanced Features

## Transform (Creating New Variables)

Transform allows you to create new questions (variables) by recoding existing data.

### Where to find it

**Transform** tab → text input field.

### Transform Syntax

Each new variable is described by a block of lines separated by an empty line:

```
New question name
ALT1 {filter_condition} Alternative text 1
ALT2 {filter_condition} Alternative text 2
...
NA {filter_condition}
```

Where:

- **First line** — text of the new question
- **Following lines** — recoding rules:
    - `ALT` — number of the new alternative (integer) or `NA` (to set "No Answer")
    - `{condition}` — filter formula in curly braces (same syntax as filters)
    - Text after `}` — alternative name

> 💡 If curly braces are empty `{}`, the condition applies to **all** questionnaires that have not yet received a value.

### Example: recoding from one variable

```
Age groups
1 {[3]>=18 and [3]<=24} 18-24
2 {[3]>=25 and [3]<=34} 25-34
3 {[3]>=35 and [3]<=44} 35-44
4 {[3]>=45 and [3]<=54} 45-54
5 {[3]>=55} 55+
NA {[3]<18}
```

Creates a new nominal variable (`qn`) with 5 alternatives based on metric variable #3 (age).

### Example: program sample (Paste Sample)

```
New Var
1 {[2]=1 or [2]=2} One
2 {[2]=3} Two
3 {[2]=4 and [2]=5} Three
4 {[2]=6} Four
4 {[2]=1} Five
NA {[2]=6}
7 {[2]=9} Seven
8 {} Eight
```

### Important rules

- If a questionnaire matches **multiple** conditions, it will receive **multiple** alternatives → the new variable type will be `qj` (multi-variant)
- If each questionnaire matches only **one** condition — the type will be `qn` (nominal)
- The `NA {condition}` line forcibly sets "No Answer" for questionnaires matching the condition
- Empty curly braces `{}` means "everything else" (questionnaires without a value)
- Multiple transforms are separated by an **empty line**

### Save and load

- Right-click menu → **Save transform** — saves text to file
- Right-click menu → **Load transform** — loads text from file
- Right-click menu → **Paste sample** — inserts a transform example

---

## Recoding Alternatives (Recode)

For quick regrouping of alternatives of an existing variable without writing a transform:

The `RecodeIntoNewVar` function creates a new variable by combining alternatives of the source variable.

Alternative structure is defined by lines:

```
1+2
3
4+5+6
7-10
```

- `1+2` — alternatives 1 and 2 are combined into one new alternative
- `3` — alternative 3 remains as is
- `4+5+6` — alternatives 4, 5 and 6 are combined
- `7-10` — range of alternatives from 7 to 10

---

## Significance Testing

Significance testing determines whether the difference between values in table columns is statistically significant.

### Significance settings

On the **Table Settings** tab in the **Significance** section:

#### Test type

| Option | Description |
|---|---|
| ✅ Percentage significance | Tests difference between percentages in columns |
| ✅ Mean significance | Tests difference between means |

#### Comparison

| Option | Description |
|---|---|
| With Total | Each column is compared with the Total column |
| With previous column | Each column is compared with the previous one |
| Between columns | Columns are compared pairwise (letter notation A, B, C...) |

#### Significance level (Z₀)

| Level | Z-value |
|---|---|
| 1% | Strictest level |
| 5% | Standard level |
| 10% | Most lenient level |

#### Significance output

| Option | Description |
|---|---|
| In Count column | Markers added to count cells |
| In Col% column | Markers added to percentage cells |
| In separate column | Separate column for each significance marker |

#### Significance markers

Different symbols can be chosen for marking significant differences:

| Style | Higher | Lower |
|---|---|---|
| Triangles | ▲ | ▼ |
| Arrows | ⮝ | ⮟ |
| Arrows (Unicode) | ↑ | ↓ |
| Asterisks | ** | * |

#### Additional options

- **Use unweighted base** — unweighted base (BaseUW) is used for significance calculation

---

## TopBox and BottomBox

TopBoxes allow you to combine top or bottom scale alternatives into one group.

### What is TopBox / BottomBox?

- **TopBox** — sum of top alternatives (e.g., ratings 9+10 on a 10-point scale)
- **BottomBox** — sum of bottom alternatives (e.g., ratings 1+2)

### How to add TopBox/BottomBox

1. On the **Table Settings** tab in the **Boxes** section
2. Right-click
3. Choose a preset or create your own:

| Preset | Alternatives |
|---|---|
| Bottom 1+2 | Alternatives 1, 2 |
| Bottom 1+2+3 | Alternatives 1, 2, 3 |
| Top 4+5 | Alternatives 4, 5 |
| Top 9+10 | Alternatives 9, 10 |
| Top 8+9+10 | Alternatives 8, 9, 10 |

Boxes can be added separately to rows (Left) and columns (Top).

### Box properties

- **Caption** — box name in the table
- **Alternatives** — set of PassportValue alternatives included in the box
- **Hide** — hide individual alternatives included in the box
- Boxes participate in mean statistics

---

## Export to SPSS (.sav)

The program allows exporting an FRM array to SPSS `.sav` format for further analysis.

### How to export

1. Menu **FRM → Export to SPSS**
2. Choose encoding:
    - **UTF-8** — for modern SPSS versions
    - **CP1251** — for older SPSS versions

### What is created during export

| File | Description |
|---|---|
| `array_name.sav` | SPSS data file |
| `array_name_spss11.mdg` | MDG file for SPSS 11 |
| `array_name_spss12.mdg` | MDG file for SPSS 12+ |

### Export specifics

- Metric variables (`qm`) → SPSS numeric variables (Measure = Scale)
- Nominal variables (`qn`) → SPSS numeric variables (Measure = Nominal) with value labels
- Multi-variant variables (`qj`) → set of dichotomous variables (v5_1, v5_2, ...) + MDG set
- Missing value for all variables = -99
- Variable names: `v1`, `v2`, `v3`... (for `qj`: `v5_1`, `v5_2`, ...)

> ⚠️ **Requirement:** SPSS export requires the IBM SPSS I/O Modules library (`spssio64.dll` / `libspssdio.so.1`), which must be in the `lib/win64/` or `lib/lin64/` folder.

---

## Table Merging

Tables can be merged:

| Mode | Description |
|---|---|
| No Merging | Each table separately (default) |
| by Column | Tables are merged horizontally (by columns) |
| by Row | Tables are merged vertically (by rows) |
