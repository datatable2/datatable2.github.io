# Filters and Weighting

## Filters

Filters allow you to restrict analysis to only those questionnaires that match a given condition. A filter is defined by a formula in a special syntax.

### How to set a filter

1. Go to the **Filters** tab
2. Enter the filter formula in the `Filter formula` field
3. Click the **Filter ON** button (▶)
4. The status bar will show the number of filtered questionnaires

### How to remove a filter

Click the **Filter OFF** button (⏹) — the filter will be removed and all questionnaires will be available again.

---

## Filter Formula Syntax

### Referencing variables (questions)

Variable number is specified in square brackets `[N]`, where `N` is the variable number or its name (vName).

| Syntax | Description |
|---|---|
| `[5]` | Value of variable #5 (PassportValue for `qn`, numeric value for `qm`) |
| `[5]=3` | Variable #5 equals alternative with PassportValue=3 (for `qn`) |
| `[5,3]` | Alternative 3 is selected in multi-variant variable #5 (for `qj`). Also works for `qn` and `qm` |
| `[age]` | Reference by variable name (vName) instead of number |

### Comparison operators

| Operator | Description |
|---|---|
| `=` | Equal to |
| `<>` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

### Logical operators

| Operator | Description |
|---|---|
| `and` | Logical AND |
| `or` | Logical OR |
| `not` | Logical NOT |

### Special functions

| Function | Description |
|---|---|
| `NA(N)` | Returns `true` if variable #N has "No Answer" value |
| `Caj(N)` | Returns the number of selected alternatives for variable #N. For `qm`/`qn`: 0 if NA, 1 otherwise. For `qj`: number of selected options |
| `NF` | Returns the current questionnaire number |
| `true` | Always true (all questionnaires) |
| `false` | Always false (no questionnaires) |

### Parentheses

Use parentheses `()` to group conditions and change operation priority.

---

## Filter Examples

### Simple filters

```
[1]=1
```
Variable #1 equals alternative 1 (e.g., gender = male).

```
[3]>=18
```
Variable #3 (e.g., age) is greater than or equal to 18.

```
[10,5]
```
In multi-variant variable #10, alternative 5 is selected.

### Compound filters

```
[1]=1 and [3]>=18
```
Males aged 18 and over.

```
[1]=1 or [1]=2
```
Variable #1 equals 1 or 2.

```
([1]=1 or [1]=2) and [3]>=25
```
Variable #1 equals 1 or 2, AND age from 25.

```
not NA(5)
```
Only questionnaires where variable #5 has an answer.

```
Caj(10)>=3
```
Only questionnaires where multi-variant variable #10 has 3 or more options selected.

### Filter by variable name

```
[gender]=1 and [age]>=18
```
Same as `[1]=1 and [3]>=18`, if vName of variable #1 = `gender` and variable #3 = `age`.

---

## Saved Filters

Filters can be saved for reuse:

1. Enter the filter formula
2. Click the **Save Filter** button (💾)
3. Enter the filter name
4. The filter will appear in the saved filters list

Saved filters are bound to the array and stored in the XML settings file.

To apply a saved filter — click on it in the list.

---

## Deleting Filtered Questionnaires

You can physically delete questionnaires that match the filter:

1. Set the filter
2. Click the **Delete filtered questionnaires** button (🗑)
3. Confirm deletion

> ⚠️ **Warning!** This operation is irreversible. Deleted questionnaires cannot be restored. It is recommended to save a copy of the array before deletion.

---

## Weighting

Weighting allows you to assign an individual weight to each questionnaire to correct the sample.

### How to enable weighting

1. Select a metric variable (`qm`) in the **Weight** dropdown
2. The program will automatically assign each questionnaire a weight equal to the value of the selected variable

> 💡 **Tip:** The program automatically highlights variables whose text contains the word `weight` or `вес`.

### How to disable weighting

Select `None` in the **Weight** dropdown. All weights will be set to 1.

### How weighting works

- Weight is taken from a metric variable (type `qm`)
- If a questionnaire has NA (no answer) for the variable, weight = 0
- Weighting affects all calculations: totals, percentages, means, etc.
- The status bar displays `Weight ON #N#` or `Weight OFF`

---

## Splits

Splits allow you to automatically break table building by groups (e.g., a separate table for each city).

### How to enable a split

1. Select a nominal (`qn`) or multi-variant (`qj`) variable in the **Split** dropdown
2. When building tables, the program will automatically create separate tables for each alternative of the selected variable

### How splits work

- For `qn` variables: a filter `[N]=alt` is created for each alternative
- For `qj` variables: a filter `[N,alt]` is created for each alternative
- If a filter is also active, the split is combined with it: `(filter) and (split)`
- In the output Excel file, a row with split information is displayed before each table

### How to disable a split

Select `None` in the **Split** dropdown.
