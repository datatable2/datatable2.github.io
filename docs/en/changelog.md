# Changelog

- 🟩 Added
- 🟥 Removed
- 🟨 Changed

## v2.1 Build 74
- 🟨 Changed settings storage method. Now everything is saved in an XML file
- 🟩 `[Tables]` Redesigned Weight, Split, Filter
- 🟩 `[Tables]` Redesigned table settings
- 🟩 `[Output]` New table output. Tables are now created directly as Excel files, not HTML, and displayed in tsWorksheetGrid component
- 🟩 `[Output]` Table style creation and management
- 🟩 Rewritten for win64
- 🟩 Added Linux version
- 🟥 Removed multi-language passport support
- 🟩 `[Tables]` Ability to display unweighted totals and bases (TotalUW, BaseUW)
- 🟩 `[Tables]` Ability to display multiple-response questions with percentages summing to 100% (analog of SPSS: Responses, Column Responses %)
- 🟩 `[Tables]` Ability to display empty tables as tables with zeros
- 🟩 `[Tables]` Added statistics: median, sum, min, max
- 🟩 `[Tables]` Added ability to calculate significance with previous column
- 🟨 `[Output]` Significance marker colors
- 🟨 `[Tables]` Redesigned TopBoxes. Different definition, participate in mean statistics.
- 🟩 `[Tables]` Means are now calculated by PassportValue instead of CountValue
- 🟩 `[Output]` Table files are now sorted in reverse order (newest on top)
- 🟨 Accelerated deletion of filtered questionnaires
- 🟨 Changed program and array settings storage
- 🟥 Removed script functionality (Scripts tab)

## v2.1 Build 66
- 🟥 Removed expiration date protection
- 🟥 Removed chart functionality (Charts tab)

## v2.1 Build 65
- 🟩 Program ported to Lazarus

## v2.1 Build 64
- 🟩 Added variable name support. Filters can now use variable number or name
- 🟩 `[Tables]` Added Table% column
- 🟨 Quick variable filtering is now truly fast
- 🟨 Fixed errors in Script section
- 🟩 `[Chart]` Started development of new charts section

## v2.1 Build 63
- 🟥 ANQ no longer used
- 🟨 Russian language changed to Ukrainian
- 🟩 Ukrainian language

## v2.1 Build 62
- 🟩 `[Tables]` Added "Hide zero cells" setting
- 🟩 `[Output]` Added button to delete all HTM table files

## v2.1 Build 61
- 🟩 Added NoAnswer cleanup for selected variables
- 🟩 Questions with #skip# in text are grayed out in the list

## v2.1 Build 60
- 🟩 Added SPSS export. Creates .sav file and MDG files in two formats
- 🟨 Fixed minor error in multi-variant question creation during transform

## v2.1 Build 59
- 🟩 Multi-language passport support. Maximum three languages.

## v2.1 Build 58
- 🟩 `[Output]` Significance level information displayed
- 🟩 `[Chart]` Added ability to display chart series in rows or columns
- 🟩 `[Filter]` Added `nf` function — questionnaire sequence number
- 🟨 `[Transform]` Improved transformation
- 🟨 Fixed large question list loading for table building

## v2.1 Build 57
- 🟩 `[Tables]` Added ability to calculate significance of weighted percentages by unweighted base
- 🟩 `[Chart]` Added presentation template selection before building charts
- 🟨 Fixed error in question text and alternatives editing

## v2.1 Build 56
- 🟩 Added drag-and-drop array files from file manager
- 🟩 `[Filter]` Added button to delete filtered questionnaires
- 🟩 `[Filter]` Added `caj()` function — count of selected alternatives in multi-variant question
- 🟩 `[Transform]` Added ability to create multiple new variables at once
- 🟨 Fixed minor inaccuracy in mean significance coloring when comparing with total

## v2.1 Build 55
- 🟩 `[Tables]` Added question and alternative text editing

## v2.1 Build 54
- 🟩 `[Tables]` Added Count Unweighted statistic

## v2.1 Build 53
- 🟩 `[Chart]` Chart building now respects weighting and filter
- 🟩 `[Chart]` Added means and topboxes in breakdown charts
- 🟩 `[Chart]` Added button for all variables in one chart
- 🟨 `[Tables]` Minor fixes
- 🟩 `[Chart]` Added title insertion choice — chart title or slide title
- 🟨 `[Tables]` TopBox alternatives can use dash notation (e.g., 1-10)
- 🟩 `[Tables]` Mean significance vs Total coloring with two colors
- 🟩 `[Output]` Added table coloring scheme selection
- 🟥 `[Output]` Removed row highlighting due to browser performance

## v2.1 Build 52
- 🟨 `[Filters]` Rewritten filter checking — faster, shows weighted filtered count
- 🟩 `[Output]` Added row highlighting in output tables
- 🟩 `[Output]` Table building time displayed
- 🟨 `[Tables]` Fixed progress bar errors
- 🟨 `[Tables]` Fixed metric question display with extra decimal places
- 🟩 `[Tables]` Improved TopBox support for multi-variant questions
- 🟨 `[Tables]` Redesigned settings for more flexible row structure
- 🟨 `[Tables]` Fixed mean statistics output with TopBoxes

## v2.1 Build 51
- 🟩 Added chart building in MS PowerPoint 2010
- 🟩 Significance vs Total percentage coloring with two colors
- 🟩 Added variable list swap button between tables and breakdowns
- 🟨 Fixed significant and minor errors

## v2.1 Build 50
- 🟩 Can hide alternatives marked with #skip#
- 🟩 Save and load transform scripts
- 🟩 Quick frequency view when Output tab is active
- 🟨 Changed Settings tab
- 🟩 Rewritten mean output, added standard deviation and standard error
- 🟩 Mean significance testing (experimental)

## v2.1 Build 49
- 🟨 Fixed "Rows: Into one table" and "Columns: Into one table" settings
- 🟨 Optimized CSV export
- 🟨 Fixed "Don't show alternatives" setting for means

## v2.1 Build 48
- 🟩 Export selected variable data to CSV format

## v2.1 Build 47
- 🟩 Variable filter
- 🟩 Added table building stop button

## v2.1 Build 46
- 🟩 Added English interface

## v2.1 Build 45
- 🟨 Program renamed to DataTable
- 🟩 Now works with ANQ passport
- 🟩 Array saving
- 🟩 Creating new variables with recoding
- 🟩 Loading table settings from clipboard

## v2.1 Build 44
- 🟨 BugFix
- 🟩 Loading and saving table INI files (syntax analog):
```
filter : `[10]`=1
count
col%
significance
left_sign : 13,14,15,16,17,18
top_sign : 18
```
- 🟩 Settings now save and auto-apply weights and filters
- 🟩 Filter management — save, delete
- 🟩 Means for metric variables
- 🟩 Tables display current filter and weight
- 🟨 Splits during filter — previously calculated incorrectly

## v2.1 Build 43
- 🟨 Percentage significance testing
- 🟩 Breakdowns with splits

## v2.1 Build 41
- 🟨 Improved percentage significance testing

## v2.1 Build 40
- 🟩 Empty row check in TopBoxes
- 🟩 Double-click sends variables to table list, Alt+Double-click to breakdowns
- 🟩 Added formatting for percentage significance cells

## v2.1 Build 39
- 🟨 Improved variable list management for table building

## v2.1 (19.03.2008)
- 🟩 Second version

## v1 (2006)
- 🟩 First version
